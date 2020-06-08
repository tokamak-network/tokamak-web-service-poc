#!/usr/bin/env bash
source /home/ubuntu/variables.list

kill -9 `ps aux | grep geth | awk '{print $2}'`

rm -r $DATADIR
rm user.log
rm init.user.log
rm user.scripts.tar
