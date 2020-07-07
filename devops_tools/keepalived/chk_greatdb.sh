#!/bin/bash
source /etc/profile

USER=root
PASSWORD=byb0309
PORT=3306
NETDEV=enp0s3
VIP=172.16.50.222
CHKLOG=/tmp/chk_mysql.log
CHKTMPFILE=/tmp/chk_mysql.txt
echo "$(date +\"%Y%m%d-%H:%M:%S\")" >> $CHKLOG
EXIST_NUM=$(ps -ef | grep chk_mysql.sh | grep -v grep | awk '{print $2}' | wc -l)

#判断进程是否已经被调用，防止重复调用
#if [ $EXIST_NUM -gt 2 ];then
#    exit 0
#fi

counter=`ps -ef | grep -w mysqld | grep $PORT | grep -v grep | wc -l`
mysql -u$USER -p$PASSWORD -P$PORT -e "show slave status\G;" >$CHKTMPFILE 2>> $CHKLOG
mysql_stat=$?
if [ ${counter} -eq 0 ] || [ ${mysql_stat} -ne 0 ]; then
    systemctl stop keepalived
    #防止systemctl执行失败
    kill -9 $(ps -ef | grep keepalived | grep -v grep | awk '{print $2}')
    #有时候keepalived服务停止，VIP还残留在网卡上
    ip addr del $VIP/32 dev $NETDEV
    while true
    do
        counter=`ps -ef | grep -w mysqld | grep $PORT | grep -v grep | wc -l`
        echo "exit" | mysql   -u$USER -p$PASSWORD -P$PORT 2>/dev/null
        mysql_stat=$?
        if [ ${counter} -gt 0 ] && [ ${mysql_stat} -eq 0 ]; then
           systemctl start keepalived 
           break
        fi
        sleep 2
    done
else
    Slave_IO_Running=$(grep -w Slave_IO_Running $CHKTMPFILE | awk -F": " '{print $2}')
    Slave_SQL_Running=$(grep -w Slave_SQL_Running $CHKTMPFILE | awk -F": " '{print $2}')
    Seconds_Behind_Master=$(grep -w Seconds_Behind_Master $CHKTMPFILE | awk -F": " '{print $2}')
    echo "Slave_IO_Running=$Slave_IO_Running" >> $CHKLOG
    echo "Slave_SQL_Running=$Slave_SQL_Running" >> $CHKLOG
    echo "Seconds_Behind_Master=$Seconds_Behind_Master" >> $CHKLOG
    if [ "$Slave_IO_Running" != "Yes" ] || [ "$Slave_SQL_Running" != "Yes" ];then
        mysql  -u$USER -p$PASSWORD -P$PORT -e "stop slave;start slave;" >/dev/nul 2>> $CHKLOG
    fi
fi
