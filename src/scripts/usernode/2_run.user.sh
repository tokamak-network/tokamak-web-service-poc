#!/usr/bin/env bash
source /home/ubuntu/variables.list

nohup /home/ubuntu/plasma-evm/build/bin/geth \
    --nousb \
    --datadir $DATADIR \
    --syncmode="full" \
    --networkid $NETWORK_ID \
    --rootchain.url ws://$ROOTCHAIN_IP:8546 \
    --rpc \
    --rpcaddr '0.0.0.0' \
    --rpcport 8547 \
    --rpcapi eth,net,debug \
    --rpccorsdomain "*" \
    --rpcvhosts=$HOST_IP \
    --ws \
    --wsorigins '*' \
    --wsaddr '0.0.0.0' \
    --wsport 8548 \
    --bootnodes $BOOT_NODE \
    --port 30307 \
    --nat extip:$HOST_IP \
    --maxpeers 50 >> user.log &
sleep 2
echo "usernode runs now!"
