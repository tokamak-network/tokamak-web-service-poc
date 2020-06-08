source /home/ubuntu/variables.list

plasma-evm $ build/bin/geth --nousb staking stake-ton $AMOUNT \
            --datadir $DATADIR \
            --rootchain.url ws://$ROOTCHAIN_IP:8546 \
            --unlock $OPERATOR \
            --password /home/ubuntu/pwd.pass \
            --rootchain.sender $OPERATOR \
            --rootchain.gasprice $GASPRICE