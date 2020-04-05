source /home/ubuntu/variables.list

/home/ubuntu/plasma-evm/build/bin/geth --nousb \
    manage-staking setManagers /home/ubuntu/stake/manager.json  \
    --datadir $DATADIR
