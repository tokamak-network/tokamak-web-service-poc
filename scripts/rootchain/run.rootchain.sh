#!/usr/bin/env bash
source account.variable

nohup /home/ubuntu/go-ethereum/build/bin/geth \
  --datadir $DATADIR\
  --dev \
  --dev.period 1 \
  --dev.faucetkey "$OPERATOR_PRIV_KEY,$KEY0,$KEY1,$KEY2,$KEY3,$CHALLENGER_KEY" \
  --miner.gastarget 7500000 \
  --miner.gasprice "10" \
  --rpc \
  --rpcport 8545 \
  --rpcapi eth,debug,net\
  --ws \
  --wsaddr "0.0.0.0"\
  --wsapi "net,web3,eth,debug"\
  --wsport 8546 >> rootnode.log &
sleep 2
echo "rootchain runs!"
