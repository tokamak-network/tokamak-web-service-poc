#!/usr/bin/env bash
source /home/ubuntu/variables.list

nohup /home/ubuntu/plasma-evm/build/bin/geth \
    --nousb \
    --datadir /home/ubuntu/chaindata-oper\
    --syncmode="full" \
    --networkid $CHAIN_ID \
    --rootchain.url ws://$ROOTCHAIN_IP:8546 \
    --operator $OPERATOR \
    --port 30306 \
    --maxpeers 50 \
    --unlock $OPERATOR \
    --password /home/ubuntu/pwd.pass \
    --nodekeyhex $NODE_KEY_HEX \
    --nat extip:$(curl ifconfig.me) \
    --mine \
    --miner.gastarget 7500000 \
    --miner.gaslimit 10000000 >> operator.log &

sleep 2
echo "operater node runs!"
