#!/bin/bash

source /etc/profile

STATUS_LOG=/tmp/SLAVE_slave_status.log   #数据库复制状态监控日志，根据实际填写
USER=root      #数据库连接用户名，根据实际填写
PASSWORD=byb0309     #数据库连接用户密码，根据实际填写
PORT=3306      #数据库连接端口，根据实际填写

OWNPID=$$
EXIST_NUM=$(ps -ef | grep -vw $OWNPID | grep set_backup.sh | grep -v grep | awk '{print $2}' | wc -l)

#判断进程是否已经被调用，防止重复调用
#if [ $EXIST_NUM -gt 1 ];then
#    echo "$(date +\"%Y%m%d-%H:%M:%S\")" >> $STATUS_LOG
#    echo "Script set_backup.sh already exists!" >> $STATUS_LOG
    #如果进程未完全停止，会不停的调用chk_mysql.sh脚本
#    exit 0
#fi

#从库打开read_only，防止意外写入
mysql  -P$PORT -u$USER -p$PASSWORD -e "start slave;set sql_log_bin=0; set innodb_lock_wait_timeout=3; set lock_wait_timeout=3; set global read_only=1; set global super_read_only=1;"

while true
do
    STATUS_FILE=/tmp/SLAVE_slave_status_$(date "+%y%m%d-%H%M").txt
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

    #当首次成为BACKUP或者原master重新加入集群后，先关闭半同步复制，防止因为主从数据不同步导致主库业务无法写入
    #等追平主库数据后，打开半同步复制
    if [ "$Master_Log_File" == "$Relay_Master_Log_File" ] && [ $Read_Master_Log_Pos -eq $Exec_Master_Log_Pos ] && [ "$Slave_IO_Running" == "Yes" ] && [ "$Slave_SQL_Running" == "Yes" ];then
        mysql  -P$PORT -u$USER -p$PASSWORD -e "set sql_log_bin=0; set innodb_lock_wait_timeout=3; set lock_wait_timeout=3; set global rpl_semi_sync_master_enabled=1; set global rpl_semi_sync_slave_enabled=1;stop slave;start slave;"
        break
    elif [ "$Master_Log_File" == "$Relay_Master_Log_File" ] && [ "$Seconds_Behind_Master" == "0" ] && [ "$Slave_IO_Running" == "Yes" ] && [ "$Slave_SQL_Running" == "Yes" ];then
        mysql  -P$PORT -u$USER -p$PASSWORD -e "set sql_log_bin=0; set innodb_lock_wait_timeout=3; set lock_wait_timeout=3; set global rpl_semi_sync_master_enabled=1; set global rpl_semi_sync_slave_enabled=1;stop slave;start slave;"
        break
    else
        mysql  -P$PORT -u$USER -p$PASSWORD -e "set sql_log_bin=0; set innodb_lock_wait_timeout=3; set lock_wait_timeout=3;set global rpl_semi_sync_slave_enabled=0;stop slave;start slave;" 2>> $STATUS_LOG
    fi
    rm -rf $STATUS_FILE
    sleep 1
done
