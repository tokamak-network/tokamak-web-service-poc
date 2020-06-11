kill -9 `ps aux | grep geth | awk '{print $2}'`

rm -r /home/ubuntu/datadir
rm -r /home/ubuntu/datadir2
rm rootnode.log
rm pwd.pass
rm manager.json
rm rootchain.scripts.tar
