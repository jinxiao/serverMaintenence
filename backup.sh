#!/bin/bash
UDISKPATH=/backuppath1
LOCALPATH=/backuppath2
datestamp=$(date +%Y-%m-%d)
backup(){
#       sleep 60
        asbackup -n push -d $LOCALPATH/asbackup_$datestamp -f 3
        tar -I pigz -cvf $LOCALPATH/asbackup_$datestamp.tar.gz $LOCALPATH/asbackup_$datestamp/ --remove-file
        cp $LOCALPATH/asbackup_$datestamp.tar.gz $UDISKPATH/
}
PROCESS_NUM=`ps -ef | grep asbackup | grep -v "grep" | wc -l`
#echo $PROCESS_NUM
if [ $PROCESS_NUM -eq 1 ]; then
        echo "a backup process is already running"
else
        backup
fi

tar -I pigz -cvf $LOCALPATH/asbackup_$datestamp.tar.gz $LOCALPATH/asbackup_$datestamp/ --remove-file

/root/bakcup/mongodump -h 10.10.32.126 -u dev -p gryNxGjw1gOYYH  -d mpush -o $LOCALPATH/mongodb_$datestamp

tar -zcvf $LOCALPATH/mongodb_$datestamp.tar.gz $LOCALPATH/mongodb_$datestamp/ --remove-file

cp $LOCALPATH/asbackup_$datestamp.tar.gz $UDISKPATH/
cp $LOCALPATH/mongodb_$datestamp.tar.gz $UDISKPATH/
