#!/bin/bash
# author: yhkl
# 0 1 * * 0 /path_to/backup.sh

db_user=postgres
db_pass=postgres
db_host=127.0.0.1
db_port=5432

backuptime=$(date +%Y-%m-%d)
backupepoch=$(date +%s)
backup_file_name=bakcp_${bakcupepoch}_${backuptime}.dmp
backup_file_path="/data/backup/"
back_db_name="postgres"

log_path="/data/bakcup/log"
logger=$log_path/db_backup_${backuptime}.log

if [ ! -d "$path"  ]; then
	mkdir -p $log_path 
fi

touch $logger

cd $backup_file_path 

echo "Start to backup ${back_db_name} SCHEMA" >> $logger
pg_dump --verbose --no-acl --no-owner  --dbname=//:${db_user}:${db_pass}@${db_host}:${db_port}/${back_db_name}-f ${back_db_name} -Fc  >> $logger 2>&1

