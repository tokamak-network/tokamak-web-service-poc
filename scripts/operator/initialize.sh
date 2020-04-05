kill -9 `ps aux | grep geth | awk '{print $2}'`

rm -r chaindata-oper/
rm deploy.rootchain.log
rm init.oper.log
rm pwd.pass
rm operator.log
rm genesis.json
rm oper.scripts.tar
