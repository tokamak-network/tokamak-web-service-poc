source /home/ubuntu/account.variable

/home/ubuntu/plasma-evm/build/bin/geth --nousb manage-staking deploy-powerton $ROUND_TIME \
            --datadir $DATADIR2 \
            --rootchain.url ws://127.0.0.1:8546 \
            --unlock $OPERATOR \
            --password /home/ubuntu/pwd.pass \
            --rootchain.sender $OPERATOR
