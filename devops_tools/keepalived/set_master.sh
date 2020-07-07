vim /opt/set_master.sh
#!/bin/bash

source /etc/profile

STATUS_LOG=/tmp/MASTER_slave_status.log   #数据库复制状态监控日志，根据实际填写
USER=root      #数据库连接用户名，根据实际填写
PASSWORD=byb0309     #数据库连接用户密码，根据实际填写
PORT=3306      #数据库连接端口，根据实际填写

OWNPID=$$
EXIST_NUM=$(ps -ef | grep -vw $OWNPID | grep set_master.sh | grep -v grep | awk '{print $2}' | wc -l)

#判断进程是否已经被调用，防止重复调用
#if [ $EXIST_NUM -gt 1 ];then
#    echo "$(date +\"%Y%m%d-%H:%M:%S\")" >> $STATUS_LOG
#    echo "Script set_master.sh already exists!" >> $STATUS_LOG
    #如果进程未完全停止，会不停的调用chk_mysql.sh脚本
#    exit 0
#fi

mysql  -P$PORT -u$USER -p$PASSWORD -e "start slave;"

while true
do
    STATUS_FILE=/tmp/MASTER_slave_status_$(date "+%y%m%d-%H%M").txt
    mysql  -P$PORT -u$USER -p$PASSWORD -e "show slave status\G" > $STATUS_FILE
    Master_Log_File=$(grep -w Master_Log_File $STATUS_FILE | awk -F": " '{print $2}')
    Relay_Master_Log_File=$(grep -w Relay_Master_Log_File $STATUS_FILE | awk -F": " '{print $2}')
    Read_Master_Log_Pos=$(grep -w Read_Master_Log_Pos $STATUS_FILE | awk -F": " '{print $2}')
    Exec_Master_Log_Pos=$(grep -w Exec_Master_Log_Pos $STATUS_FILE | awk -F": " '{print $2}')
    Last_Errno=$(grep -w Last_Errno $STATUS_FILE | awk -F": " '{print $2}')
    Seconds_Behind_Master=$(grep -w Seconds_Behind_Master $STATUS_FILE | awk -F": " '{print $2}')
    Last_IO_Errno=$(grep -w Last_IO_Errno $STATUS_FILE | awk -F": " '{print $2}')
    Last_SQL_Errno=$(grep -w Last_SQL_Errno $STATUS_FILE | awk -F": " '{print $2}')
    Slave_SQL_Running_State=$(grep -w Slave_SQL_Running_State $STATUS_FILE | awk -F": " '{print $2}')
    Slave_IO_Running=$(grep -w Slave_IO_Running $STATUS_FILE | awk -F": " '{print $2}')
    Slave_SQL_Running=$(grep -w Slave_SQL_Running $STATUS_FILE | awk -F": " '{print $2}')
    echo "$(date +\"%Y%m%d-%H:%M:%S\")" >> $STATUS_LOG
    echo "Master_Log_File=$Master_Log_File" >> $STATUS_LOG
    echo "Relay_Master_Log_File=$Relay_Master_Log_File" >> $STATUS_LOG
    echo "Read_Master_Log_Pos=$Read_Master_Log_Pos" >> $STATUS_LOG
    echo "Exec_Master_Log_Pos=$Exec_Master_Log_Pos" >> $STATUS_LOG
    echo "Last_Errno=$Last_Errno" >> $STATUS_LOG
    echo "Seconds_Behind_Master=$Seconds_Behind_Master" >> $STATUS_LOG
    echo "Last_IO_Errno=$Last_IO_Errno" >> $STATUS_LOG
    echo "Last_SQL_Errno=$Last_SQL_Errno" >> $STATUS_LOG
    echo "Slave_SQL_Running_State=$Slave_SQL_Running_State" >> $STATUS_LOG
    echo "Slave_IO_Running=$Slave_IO_Running" >> $STATUS_LOG
    echo "Slave_SQL_Running=$Slave_SQL_Running" >> $STATUS_LOG
    echo "-----------------------------------------------------" >> $STATUS_LOG

    #首次被选为master或者从slave变为master后，如果复制无延迟，打开master半同步复制，关闭read_only，允许写入
    #如果存在延迟，必须设置set global read_only和super_read_only等于ON，否则业务可能会报错（比如查不到之前写入的数据）,同时需要
    #关闭半同步复制
    #修改半同步复制参数后，需要重新启动复制线程，否则半同步制状态不会立即更新
    if [ "$Master_Log_File" == "$Relay_Master_Log_File" ] && [ "$Read_Master_Log_Pos" == "$Exec_Master_Log_Pos" ];then
        mysql -P$PORT -u$USER -p$PASSWORD -e "set sql_log_bin=0; set innodb_lock_wait_timeout=3; set lock_wait_timeout=3; set global rpl_semi_sync_master_enabled=1; set global rpl_semi_sync_slave_enabled=1;stop slave;start slave;set global read_only=0; set global super_read_only=0;"
        break
    elif [ "$Master_Log_File" == "$Relay_Master_Log_File" ] && [ "$Seconds_Behind_Master" == "0" ];then
        mysql -P$PORT -u$USER -p$PASSWORD -e "set sql_log_bin=0; set innodb_lock_wait_timeout=3; set lock_wait_timeout=3; set global rpl_semi_sync_master_enabled=1; set global rpl_semi_sync_slave_enabled=1;stop slave;start slave;set global read_only=0; set global super_read_only=0;"
        break
    else
        mysql -P$PORT -u$USER -p$PASSWORD -e "set sql_log_bin=0; set innodb_lock_wait_timeout=3; set lock_wait_timeout=3; set global rpl_semi_sync_master_enabled=0;stop slave;start slave;set global read_only=1; set global super_read_only=1;" 2>> $STATUS_LOG
    fi
    rm -rf $STATUS_FILE
    sleep 1
done
