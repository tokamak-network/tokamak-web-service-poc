# Tokamak Web Service PoC

<p>
  <a href="https://discord.gg/HjJCwm5">
      <img src="https://img.shields.io/discord/696270789472682034?logo=discord"
          alt="chat on Discord">
  </a>
</p>

## Planning
[Planning Document](https://docs.google.com/presentation/d/18nSOzgvrDsUZb36V0VLtWatB8jJCmhgX5dUBctVnkXo/edit?usp=sharing)
\*@onther.io required

## Installation

```
$git clone https://github.com/Onther-Tech/tokamak-web-service-poc
$cd tokamak-web-service-poc
$virtualenv venv && source venv/bin/activate
$pip install -r requirements.txt
```

### config.ini

```
[AWS]
AWS_ACCESS_KEY = <aws access key>
AWS_SECRET_KEY = <aws secret key>

[INSTANCE]
BASIC_IMAGE_ID = <basic image>

INSTANCE_TYPE = <instance type --> e.q. t2.small>
SECURITY_GROUP_ID = <security group id>
KEY_NAME = <aws's ssh key file name>

REGION_NAME = <Instance Region --> e.q. ap-northeast-1>

[SSH]
SSH_USERNAME = <instance username --> e.q. ubuntu>
SSH_PEMFILE = <.pem file name>

[SERVER]
DEBUG = <is debug flag>
SECRET_KEY = <server secret key>
USERNAME = <server username>
PASSWORD = <server password>

[DATABASE]
DATABASE = <database file name>
```

### .pem file

In order to run this server, you need .pem file. If you create .pem file by this server, it will be stored on .pem directory. 

## API

### Home
This endpoint visualize geth and plasma-evm node.

#### HTTP Request
```
/
```

#### Success Response
```
[
  {
    'source': 6, 
    'target': 0
  }, 
]
```

#### Error Response

None


### Show Current Config
This endpoint retrieve current config.ini

#### URL
```
/config
```

#### Success Response
```
<ACCESS KEY>
<SECRET KEY>
ami-00b4ba6aa66260654
t2.small
launch-wizard-7
test3
ap-northeast-1
ubuntu
./.pem/test3.pem
True
pxKCFg7Tk1LpOSW/BcldvAJ7VpVi/n04I8kaRLLH
db.json
db.json
db.json
```

#### Error Response
None



### Pem List
This endpoint retireve all of the pem file in tws.
#### URL
```
/config/pem/form
```

#### Success Response
```
[
  {
    'Type': 'pem', 
    'Name': 'test1', 
    'FingerPrint': 'ab:cd:7f:62:9e:ae:4c:e3:e1:06:ca:b4:63:6a:c6:bc:df:a3:39:cd'
  }, 
]
```
#### Error Response
None



### Create Pem
This endpoint create new pem file for tws.

#### URL
```
POST /config/pem/form/create
```

#### Success Response
```
redirect to /config/pem/form
```
#### Error Response
```
An error occurred (InvalidKeyPair.Duplicate) when calling the CreateKeyPair operation: The keypair '<file name>' already exists.
```



### Pem Delete
This endpoint

#### URL
```
DELETE /config/pem/form/delete
```
#### Success Response
```
redirect to /config/pem/form
```
#### Error Response
```
```




### Set Config
This endpoint set config.ini

#### URL
```
POST /config/ini/set
```
#### Success Response
```
redirect to /config
```
#### Error Response
```
```




### Get Rootchain List
This endpoint retrive rootchain.

#### URL
```
/rootchain
```
#### Success Response
```
[
  {
    'Type': 'rootchain', 
    'Name': '<rootchain name>', 
    'InstanceId': '<rootchain instance id>', 
    'Status': '<status of rootchain>', 
    'Date': '', 
    'Faucet': [], 
    'Operator': '', 
    'OperatorPassword': '', 
    'Staking': {
      'WithdrawalDelay': '<withdrawal delay>', 
      'SeigPerBlock': '<seigniorage per block>', 
      'PwertTONRoundTime': '<round time>'
      }, 
      'IsScriptSet': '', 
      'IsMansgerDeployed': '', 
      'IsPowerTONDeployed': '', 
      'IsPowerTONStarted': '', 
      'IsManagerExported': '', 
      'Managers': {
        'TON': '<TON contract address>', 
        'WTON': '<WTON contract address>', 
        'DepositManager': '<deposit manager contract address>', 
        'RootChainRegistry': '<rootchain registry contract addresss>', 
        'SeigManager': '<seigniorage manager contract address>', 
        'PowerTON': '<power ton contract address>'
      }, 
      'Managers2': '', 
      'IpAddress': '<ip address>'
    },
    ...
]
```
#### Error Response
```
```




### Start Rootchain
This endpoint run new rootchain node

#### URL
```
POST /rootchain/startnode
```
#### Success Response
```
redirect to /rootchain
```
#### Error Response
```
```




### Reset Rootchain
This endpoint reset rootchain

#### URL
```
POST /rootchain/reset
```
#### Success Response
```
redirect for /rootchain
```
#### Error Response
```
```




### Form Rootchian
This endpoint render rootchain create 

#### URL
```
/rootchain/form
```
#### Success Response
```
render rootchain/rootchain_creat.html
```
#### Error Response
```
```




### Rootchain Create
This endpoint create new rootchain

#### URL
```
POST /rootchain/form/create
```
#### Success Response
```
redirect to /rootchain
```
#### Error Response
```
```




### Deploy Manager
This endpoint deploy deploy seigniorage manager

#### URL
```
/rootchain/deploy/manager/<instanceid>
```
#### Success Response
```
redirect to /rootchain
```
#### Error Response
```
```




### Deploy Power Ton
This endpoint deploy power ton contract

#### URL
```
/rootchain/deploy/powerton/<instanceid>
```
#### Success Response
```
redirect to /rootchain
```
#### Error Response
```
```




### Start Power Ton
This endpoint

#### URL
```
/rootchain/start/powerton/<instanceid>
```
#### Success Response
```
redirect to /rootchain
```
#### Error Response
```
```




### Export Manager
This endpoint export seig manger contract address

#### URL
```
/rootchain/export/manager/<instanceid>
```
#### Success Response
```
redirect to /rootchain
```
#### Error Response
```
```




### Operator List
This endpoint get operator list and render it.

#### URL
```
/operator
```
#### Success Response
```
[
  {
    'Type': 'operator', 
    'Name': '<operator instance name>', 
    'ChainID': '<plasma chain's chain id>', 
    'Epoch': '<epoch length>', 
    'PreAsset': 'true', 
    'RootChain': {
      'Name': '<rootchain name>', 
      'IpAddress': '<rootchain instance ip address>', 
      'InstanceId': '<rootchain instance id>'
    }, 
    'InstanceId': '<operator instance id>', 
    'Status': '', 
    'Date': '', 
    'RootchainId': '<rootchain instance id>', 
    'NodeKey': '<nodekey>',
    'OperatorAccount': '<operator address>', 
    'OperatorAccountKey': '<operator's private key>',
    'OperatorPassword': '', 
    'StaminaOperatorAmount': '<amount of depositted stamina>', 
    'StaminaMinDeposit': '<minimum amount of stamina>', 
    'StaminaRecoverEpochLength': '<recovery epoch length>', 
    'StaminaWithdrawalDelay': '<withdrawal delay>', 
    'Dashboard': {
      'OperatorName': '<operator name>', 
      'Website': '<operator website>', 
      'Description': '<introduce about operator>', 
      'ApiServer': '<staking dashboard api server address>'
    }, 
    'IsSet': '', 
    'IsDeployed': '', 
    'Genesis': '', 
    'IsExported': '', 
    'IsInitialized': '', 
    'IsManagersImported': '', 
    'IsManagersSet': '', 
    'IsMansgersRegistered': '', 
    'IsOperatorRegistered': ''
  },
  ...
]

and render operator/operator_list.html
```
#### Error Response
```
```




### Opeartor Create Form
This endpoint show create operator form

#### URL
```
/operator/form
```
#### Success Response
```
[
  {
    'Type': 'rootchain', 
    'Name': '<rootchain name>', 
    'InstanceId': '<rootchain instance id>', 
    'Status': '<status of rootchain>', 
    'Date': '', 
    'Faucet': [], 
    'Operator': '', 
    'OperatorPassword': '', 
    'Staking': {
      'WithdrawalDelay': '<withdrawal delay>', 
      'SeigPerBlock': '<seigniorage per block>', 
      'PwertTONRoundTime': '<round time>'
      }, 
      'IsScriptSet': '', 
      'IsMansgerDeployed': '', 
      'IsPowerTONDeployed': '', 
      'IsPowerTONStarted': '', 
      'IsManagerExported': '', 
      'Managers': {
        'TON': '<TON contract address>', 
        'WTON': '<WTON contract address>', 
        'DepositManager': '<deposit manager contract address>', 
        'RootChainRegistry': '<rootchain registry contract addresss>', 
        'SeigManager': '<seigniorage manager contract address>', 
        'PowerTON': '<power ton contract address>'
      }, 
      'Managers2': '', 
      'IpAddress': '<ip address>'
    },
    ...
]

and render operator_create form
```
#### Error Response
```
```




### Create New Operator
This endpoint create operator

#### URL
```
POST /operator/form/create
```
#### Success Response
```
redirect to /operator
```
#### Error Response
```
```




### Set Variable
This endpoint set variable of operator

#### URL
```
POST /operator/set/variable
```
#### Success Response
```
redirect to /operator
```
#### Error Response
```
```




### deploy
This endpoint deploy rootchain contract to its rootchain

#### URL
```
POST /operator/deploy/rootchain
```
#### Success Response
```
redirect to /operator
```
#### Error Response
```
```




### Export Genesis
This endpoint export operator's genesis file.

#### URL
```
POST /operator/export/genesis
```
#### Success Response
```
redirect to /operator
```
#### Error Response
```
```




### Init Operator
This endpoint init operator node

#### URL
```
POST /operator/initialize
```
#### Success Response
```
redirect to /operator
```
#### Error Response
```
```




### Import Manager
This endpoint get seigniorage manager contract address.

#### URL
```
/operator/set/managers/<instanceid>
```
#### Success Response
```
redirect to /operator
```
#### Error Response
```
```




### Register Rootchain
This endpoint register staking manager.

#### URL
```
/operator/register/managers/<instanceid>
```
#### Success Response
```
redirect to /operator
```
#### Error Response
```
```




### Register to Dashboard
This endpoint register operator node to staking dashboatd

#### URL
```
/operator/register/rootchain/<instanceid>
```
#### Success Response
```
redirect to /operator
```
#### Error Response
```
```




### Start Operator
This endpoint start operator node.

#### URL
```
POST /operator/runnode
```
#### Success Response
```
redirect to /operator
```
#### Error Response
```
```




### Usernode List
This endpoint show usernodes.

#### URL
```
/usernode
```
#### Success Response
```
[
  {
    'Type': 'usernode', 
    'Name': '', 
    'RootChain': {
      'Name': '<rootchain name>', 
      'IpAddress': '<rootchain ip address>', 
      'InstanceId': '<instance id of rootchain>'
    }, 
    'Operator': {
      'Name': '<operator instance name>', 
      'IpAddress': '<operator ip address>', 
      'InstanceId': '<operator instance id>', 
      'Genesis': '', 
      'ChainID': '<operator's chain id>'
    }, 
    'InstanceId': '<usernode instance id>', 
    'Status': '', 
    'Date': '', 
    'Enode': '<enode value>', 
    'IsInitialized': '', 
    'IpAddress': '<usernode ip address>'
  }
]


and render usernode/usernode_list.html
```
#### Error Response
```
```




### Usernode Create Form
This endpoint show usernode create form.

#### URL
```
/usernode/form
```
#### Success Response
```
[
  {
    'Type': 'rootchain', 
    'Name': '<rootchain name>', 
    'InstanceId': '<rootchain instance id>', 
    'Status': '<status of rootchain>', 
    'Date': '', 
    'Faucet': [], 
    'Operator': '', 
    'OperatorPassword': '', 
    'Staking': {
      'WithdrawalDelay': '<withdrawal delay>', 
      'SeigPerBlock': '<seigniorage per block>', 
      'PwertTONRoundTime': '<round time>'
      }, 
      'IsScriptSet': '', 
      'IsMansgerDeployed': '', 
      'IsPowerTONDeployed': '', 
      'IsPowerTONStarted': '', 
      'IsManagerExported': '', 
      'Managers': {
        'TON': '<TON contract address>', 
        'WTON': '<WTON contract address>', 
        'DepositManager': '<deposit manager contract address>', 
        'RootChainRegistry': '<rootchain registry contract addresss>', 
        'SeigManager': '<seigniorage manager contract address>', 
        'PowerTON': '<power ton contract address>'
      }, 
      'Managers2': '', 
      'IpAddress': '<ip address>'
    },
    ...
]
[
  {
    'Type': 'operator', 
    'Name': '<operator instance name>', 
    'ChainID': '<plasma chain's chain id>', 
    'Epoch': '<epoch length>', 
    'PreAsset': 'true', 
    'RootChain': {
      'Name': '<rootchain name>', 
      'IpAddress': '<rootchain instance ip address>', 
      'InstanceId': '<rootchain instance id>'
    }, 
    'InstanceId': '<operator instance id>', 
    'Status': '', 
    'Date': '', 
    'RootchainId': '<rootchain instance id>', 
    'NodeKey': '<nodekey>',
    'OperatorAccount': '<operator address>', 
    'OperatorAccountKey': '<operator's private key>',
    'OperatorPassword': '', 
    'StaminaOperatorAmount': '<amount of depositted stamina>', 
    'StaminaMinDeposit': '<minimum amount of stamina>', 
    'StaminaRecoverEpochLength': '<recovery epoch length>', 
    'StaminaWithdrawalDelay': '<withdrawal delay>', 
    'Dashboard': {
      'OperatorName': '<operator name>', 
      'Website': '<operator website>', 
      'Description': '<introduce about operator>', 
      'ApiServer': '<staking dashboard api server address>'
    }, 
    'IsSet': '', 
    'IsDeployed': '', 
    'Genesis': '', 
    'IsExported': '', 
    'IsInitialized': '', 
    'IsManagersImported': '', 
    'IsManagersSet': '', 
    'IsMansgersRegistered': '', 
    'IsOperatorRegistered': ''
  },
  ...
]
and render usernode/usernode_create.html

```
#### Error Response
```
```




### Usernode Create
This endpoint create user node.

#### URL
```
POST /usernode/form/create
```
#### Success Response
```
redirect to /usernode
```
#### Error Response
```
```





### Init Usernode
This endpoint init usernode

#### URL
```
POST /usernode/initialize
```
#### Success Response
```
redirect to usernode
```
#### Error Response
```
```




### Run Usernode
This endpoint start usernode

#### URL
```
POST /usernode/runnode
```
#### Success Response
```
redirect /usernode
```
#### Error Response
```
```




### Get Instance
This endpoint retrieve instance by given instanceid

#### URL
```
/instance/<instanceid>
```
#### Success Response
```
[
  {
    'Type': 'operator', 
    'Name': '<operator instance name>', 
    'ChainID': '<plasma chain's chain id>', 
    'Epoch': '<epoch length>', 
    'PreAsset': 'true', 
    'RootChain': {
      'Name': '<rootchain name>', 
      'IpAddress': '<rootchain instance ip address>', 
      'InstanceId': '<rootchain instance id>'
    }, 
    'InstanceId': '<operator instance id>', 
    'Status': '', 
    'Date': '', 
    'RootchainId': '<rootchain instance id>', 
    'NodeKey': '<nodekey>',
    'OperatorAccount': '<operator address>', 
    'OperatorAccountKey': '<operator's private key>',
    'OperatorPassword': '', 
    'StaminaOperatorAmount': '<amount of depositted stamina>', 
    'StaminaMinDeposit': '<minimum amount of stamina>', 
    'StaminaRecoverEpochLength': '<recovery epoch length>', 
    'StaminaWithdrawalDelay': '<withdrawal delay>', 
    'Dashboard': {
      'OperatorName': '<operator name>', 
      'Website': '<operator website>', 
      'Description': '<introduce about operator>', 
      'ApiServer': '<staking dashboard api server address>'
    }, 
    'IsSet': '', 
    'IsDeployed': '', 
    'Genesis': '', 
    'IsExported': '', 
    'IsInitialized': '', 
    'IsManagersImported': '', 
    'IsManagersSet': '', 
    'IsMansgersRegistered': '', 
    'IsOperatorRegistered': ''
  }
]
```
#### Error Response
```
```

### Staking Main
This endpoint show main page of staking

#### URL
```
/staking
```
#### Success Response
```
[
  {
    'Type': 'operator', 
    'Name': '<operator instance name>', 
    'ChainID': '<plasma chain's chain id>', 
    'Epoch': '<epoch length>', 
    'PreAsset': 'true', 
    'RootChain': {
      'Name': '<rootchain name>', 
      'IpAddress': '<rootchain instance ip address>', 
      'InstanceId': '<rootchain instance id>'
    }, 
    'InstanceId': '<operator instance id>', 
    'Status': '', 
    'Date': '', 
    'RootchainId': '<rootchain instance id>', 
    'NodeKey': '<nodekey>',
    'OperatorAccount': '<operator address>', 
    'OperatorAccountKey': '<operator's private key>',
    'OperatorPassword': '', 
    'StaminaOperatorAmount': '<amount of depositted stamina>', 
    'StaminaMinDeposit': '<minimum amount of stamina>', 
    'StaminaRecoverEpochLength': '<recovery epoch length>', 
    'StaminaWithdrawalDelay': '<withdrawal delay>', 
    'Dashboard': {
      'OperatorName': '<operator name>', 
      'Website': '<operator website>', 
      'Description': '<introduce about operator>', 
      'ApiServer': '<staking dashboard api server address>'
    }, 
    'IsSet': '', 
    'IsDeployed': '', 
    'Genesis': '', 
    'IsExported': '', 
    'IsInitialized': '', 
    'IsManagersImported': '', 
    'IsManagersSet': '', 
    'IsMansgersRegistered': '', 
    'IsOperatorRegistered': ''
  },
  ...
]
```
#### Error Response
```
```

### Operator Info
This endpoint show Operator's information

#### URL
```
/staking/info/<index>
```
#### Success Response
```
[
  {
    'Type': 'operator', 
    'Name': '<operator instance name>', 
    'ChainID': '<plasma chain's chain id>', 
    'Epoch': '<epoch length>', 
    'PreAsset': 'true', 
    'RootChain': {
      'Name': '<rootchain name>', 
      'IpAddress': '<rootchain instance ip address>', 
      'InstanceId': '<rootchain instance id>'
    }, 
    'InstanceId': '<operator instance id>', 
    'Status': '', 
    'Date': '', 
    'RootchainId': '<rootchain instance id>', 
    'NodeKey': '<nodekey>',
    'OperatorAccount': '<operator address>', 
    'OperatorAccountKey': '<operator's private key>',
    'OperatorPassword': '', 
    'StaminaOperatorAmount': '<amount of depositted stamina>', 
    'StaminaMinDeposit': '<minimum amount of stamina>', 
    'StaminaRecoverEpochLength': '<recovery epoch length>', 
    'StaminaWithdrawalDelay': '<withdrawal delay>', 
    'Dashboard': {
      'OperatorName': '<operator name>', 
      'Website': '<operator website>', 
      'Description': '<introduce about operator>', 
      'ApiServer': '<staking dashboard api server address>'
    }, 
    'IsSet': '', 
    'IsDeployed': '', 
    'Genesis': '', 
    'IsExported': '', 
    'IsInitialized': '', 
    'IsManagersImported': '', 
    'IsManagersSet': '', 
    'IsMansgersRegistered': '', 
    'IsOperatorRegistered': ''
  }
]
```
#### Error Response
```
```

### Set Commission Rate
This endpoint set commition rate of operator
<!-- ToDo: tws에서 commissionion rate을 변경했을 때 dashboard에 어떻게 반영할지-->


#### URL
```
POST /staking/info/<index>/<commission_rate>
```
#### Success Response
```
{
  commission_rate: '<changed commission rate>'  
}
```
#### Error Response
```
```


### Stake TON Form
This endpoint show stake menu

#### URL
```
/staking/info/<index>/stake
```
#### Success Response
```
{
  available_amt: "<available amount ton to stake>"
}

and render staking/stake_menu.html
```
#### Error Response
```
```



### Stkae TON
This endpoint stake more or new mton.

#### URL
```
POST /staking/info/<index>/staking/<amount>
```
#### Success Response
```
{
  staked_mton: '<amount mton to stake>',
  available_mton: '<available mton to stake>'
}
```
#### Error Response
```
```


### Unstake TON Form
This endpoint show form for unstake.

#### URL
```
/staking/<index>/unstake
```
#### Success Response
```
{
  available_amt: <available mton to unstake>,
  not_withdrawable: <amount of mton to can't withdrawal>,
  withdrawable: <abount of mton to withdrawable>
}
```
#### Error Response
```
```


### Unstake TON
This endpoint send a command to unstake

#### URL
```
/staking/<index>/unstake/<amount>
```
#### Success Response
```
{
  staked_mton: <staked mton>,
  available_mton: <available mton to stake>
}
```
#### Error Response
```
```


### Withdrawal
This endpoint withdraw ton that can withdraw.

#### URL
```
/staking/<index>/unstake/<withdraw_amount>
```
#### Success Response
```
{
  available_mton: <available mton to stake>,
  withdrawable: <withdrawable mton>
}
```
#### Error Response
```
```


### Commit
This endpoint send transaction to commit to rootchain

#### URL
```
/staking/<index>/commit
```
#### Success Response
```
{
  commit_count: <number of operator's commit count>,
  reward: <amount of reward>,
  total_staked: <amount of ton staked by this operator>
}
```
#### Error Response
```
```





### Get Balance
This endpoint get PETH and MTON from logined account on Metamask. and it need `connection to metamask`

#### URL
```
/staking/<index>/<asset>/<amount>
```
#### Success Response
```
{
  mton_value: <the amount of mton held by operator>,
  eth_value: <the amount of eth held by operator>
}
```
#### Error Response
```
```


### Pem List
This endpoint

#### URL
```
```
#### Success Response
```
```
#### Error Response
```
```




### Reset Instance
This endpoint reset instance

#### URL
```
/instance/reset/<instanceid>
```
#### Success Response
```
redirect to /operator
```
#### Error Response
```
```




### Get Log
This endpoint retrieve log of instance

#### URL
```
/instance/<instanceid>/<filename>
```
#### Success Response
```
redirect to each node
```
#### Error Response
```
```




### Terminate Instance
This endpoint terminate instance

#### URL
```
POST /instance/terminate
```
#### Success Response
```
redirect to each node.
```
#### Error Response
```
```




### Check Status
This endpoint check status of instance

#### URL
```
POST /check/status
```
#### Success Response
```
redirect to each node
```
#### Error Response
```
```




### Check IP Address
This endpoint check IP of instance

#### URL
```
POST /check/ip
```
#### Success Response
```
redirect to each node.
```
#### Error Response
```
```




### Drop Data
This endpoint delete data from database.

#### URL
```
POST /dropdata
```
#### Success Response
```
redirect to each node.
```
#### Error Response
```
```



<!-- 
### Pem List
This endpoint

#### URL
```
```
#### Success Response
```
```
#### Error Response
```
``` -->
