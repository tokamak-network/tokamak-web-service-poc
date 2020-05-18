source /home/ubuntu/account.variable

echo $PASSWORD > /home/ubuntu/pwd.pass

/home/ubuntu/plasma-evm/build/bin/geth --nousb account import-key $OPERATOR_PRIV_KEY \
            --datadir $DATADIR2 \
            --password <(echo $PASSWORD)

/home/ubuntu/plasma-evm/build/bin/geth --nousb manage-staking deploy-managers $WITHDRAWAL_DELAY $SEIG_PER_BLOCK \
            --datadir $DATADIR2 \
            --rootchain.url ws://127.0.0.1:8546 \
            --unlock $OPERATOR \
            --password /home/ubuntu/pwd.pass \
            --rootchain.sender $OPERATOR
