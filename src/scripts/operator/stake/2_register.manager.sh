source /home/ubuntu/variables.list

/home/ubuntu/plasma-evm/build/bin/geth --nousb \
    manage-staking register \
    --datadir $DATADIR \
    --rootchain.url ws://$ROOTCHAIN_IP:8546 \
    --unlock $OPERATOR \
    --password /home/ubuntu/pwd.pass \
    --rootchain.sender $OPERATOR
