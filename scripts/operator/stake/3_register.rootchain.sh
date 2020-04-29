source /home/ubuntu/variables.list

GENESIS="$(cat /home/ubuntu/genesis.json)"
ROOTCHAIN_REGISTRY=$(jq -n \
                   --arg genesis $GENESIS \
                   --arg name "$NAME" \
                   --arg website "$WEBSITE" \
                   --arg description "$DESCRIPTION" \
                   '{genesis: $genesis, name: $name, website: $website, description: $description}')

curl -X POST \
     -H "Content-Type: application/json" \
     --data "$ROOTCHAIN_REGISTRY" \
     "$API_SERVER/operators"