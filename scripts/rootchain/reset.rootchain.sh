kill -9 `ps aux | grep geth | awk '{print $2}'`

rm -r /home/ubuntu/datadir
rm -r /home/ubuntu/datadir2

