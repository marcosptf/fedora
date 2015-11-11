#!/bin/sh 
#
#this script try clean the cache from fedora systems each 5 minutes
#i've write this code and tested in fedora 20 version
#
#[root@localhost developer]# crontab -e
#0,5,10,15,20,25,30,35,40,45,50,55  *  *  *  * /root/developer/cacheclear.sh
sh -c "sync; echo 3 > /proc/sys/vm/drop_caches"
