source /home/ubuntu/variables.list

/home/ubuntu/plasma-evm/build/bin/geth --nousb \
    manage-staking set-managers /home/ubuntu/stake/manager.json  \
    --datadir $DATADIR
