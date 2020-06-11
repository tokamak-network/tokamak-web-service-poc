#!/usr/bin/env bash
source /home/ubuntu/variables.list

# Import Operator account
/home/ubuntu/plasma-evm/build/bin/geth --nousb account import-key $OPERATOR_KEY \
    --datadir $DATADIR \
    --password <(echo $OPERATOR_PASSPHRASE)
echo "operator account imported"

# Make pwd pass
echo "$OPERATOR_PASSPHRASE" > /home/ubuntu/pwd.pass
echo "pwd.pass created"

# Deploy contracts at rootchain
echo "Deploy rootchain contract and others"
/home/ubuntu/plasma-evm/build/bin/geth \
    --nousb \
    --datadir $DATADIR \
    --rootchain.url "ws://$ROOTCHAIN_IP:8546" \
    --unlock $OPERATOR \
    --password "pwd.pass" \
    --rootchain.sender $OPERATOR \
    --rootchain.deploygasprice $DEPLOY_GASPRICE \
    --rootchain.gasprice $COMMIT_GASPRICE \
    --stamina.operatoramount $OPERATOR_AMOUNT \
    --stamina.mindeposit $MIN_DEPOSIT \
    --stamina.recoverepochlength $RECOVER_EPOCH_LENGTH \
    --stamina.withdrawaldelay $WITHDRAWAL_DELAY \
    deploy "/home/ubuntu/genesis.json" $CHAIN_ID $PRE_ASSET $EPOCH
# deploy params : chainID, isInitialAsset, Epochlength
# you can checkout "$geth deploy --help" for more information
