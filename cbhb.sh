#!/bin/bash
password=$1
url=$2
mysql_pass=$3
date=$(date +%Y%m%d)
phone_auth_file=phone_auth_$date.txt
weixin_auth_file=weixinwifi_auth_$date.txt
wget ftp://$2/opt/client_data/$phone_auth_file --ftp-user=cbhb_user --ftp-password=$1
wget ftp://$2/opt/client_data/$weixinwifi_auth_$date.txt --ftp-user=cbhb_user --ftp-password=$1
mysql -uroot -p cbhb_auth < 'LOAD DATA INFILE '$phone_auth_file' INTO phone_auth'
mysql -uroot -p cbhb_auth < 'LOAD DATA INFILE '$weixin_auth_file' INTO weixin_auth'
