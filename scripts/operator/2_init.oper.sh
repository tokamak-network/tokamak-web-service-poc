#!/usr/bin/env bash
source /home/ubuntu/variables.list

nohup /home/ubuntu/plasma-evm/build/bin/geth --nousb init \
  --datadir $DATADIR \
  --rootchain.url ws://$ROOTCHAIN_IP:8546 \
  genesis.json > init.oper.log &

sleep 2
echo "operator initialized!"
