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
    'Name': 'Mainnet', 
    'InstanceId': 'i-mainnet', 
    'Status': 'mining', 
    'Date': '', 
    'Faucet': [], 
    'Operator': '', 
    'OperatorPassword': '', 
    'Staking': {
      'WithdrawalDelay': '10', 
      'SeigPerBlock': '1.5', 
      'PwertTONRoundTime': '60'
      }, 
      'IsScriptSet': 'true', 
      'IsMansgerDeployed': 'true', 
      'IsPowerTONDeployed': 'true', 
      'IsPowerTONStarted': 'true', 
      'IsManagerExported': 'true', 
      'Managers': {
        'TON': '0xe3a87a9343D262F5f11280058ae807B45aa34669', 
        'WTON': '0xcDB18cd1f6763a93287d20598427A50d3Ba9977f', 
        'DepositManager': '0xa8f67b988f3227158146da1C1c4854d2DCcdE67D', 
        'RootChainRegistry': '0xeE0aF430528311d2b48880E9055FB9f26fd64022', 
        'SeigManager': '0x2104cEC955b6FaBF603d8B2Ee0c28EA88886fa8C', 
        'PowerTON': '0x8a5A36F16dd9eD0032cfce1a0496e543B6c72098'
      }, 
      'Managers2': '', 
      'IpAddress': '13.231.50.44'
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
    'Name': 'rinkeby-test', 
    'ChainID': '2009', 
    'Epoch': '4096', 
    'PreAsset': 'true', 
    'RootChain': {
      'Name': 'Rinkeby', 
      'IpAddress': '13.231.233.189', 
      'InstanceId': 'i-rinkeby'
    }, 
    'InstanceId': 'i-04029f270b1e465e6', 
    'Status': 'pending', 
    'Date': 'Tue, 28 Apr 2020 10:59:09 GMT', 
    'RootchainId': 'i-rinkeby', 
    'NodeKey': 'e854e2f029be6364f0f961bd7571fd4431f99355b51ab79d23c56506f5f1a7c3',
    'OperatorAccount': '0x71562b71999873DB5b286dF957af199Ec94617F7', 
    'OperatorAccountKey': 'b71c71a67e1177ad4e901695e1b4b9ee17ae16c6668d313eac2f96dbcda3f291','OperatorPassword': '', 
    'StaminaOperatorAmount': '1', 
    'StaminaMinDeposit': '0.5', 
    'StaminaRecoverEpochLength': '120960', 
    'StaminaWithdrawalDelay': '362880', 
    'Dashboard': {
      'OperatorName': 'rinkeby-test', 
      'Website': 'tokamak.network', 
      'Description': 'Tokamak Network is a platform that assures decentralized and secure property same as Ethereum Main chain while supporting high level of scalability and extendability.', 
      'ApiServer': '13.124.77.81:9001'
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
    'Name': 'Mainnet', 
    'InstanceId': 'i-mainnet', 
    'Status': 'mining', 
    'Date': '', 
    'Faucet': [], 
    'Operator': '', 
    'OperatorPassword': '', 
    'Staking': {
      'WithdrawalDelay': '10', 
      'SeigPerBlock': '1.5', 
      'PwertTONRoundTime': '60'
      }, 
      'IsScriptSet': 'true', 
      'IsMansgerDeployed': 'true', 
      'IsPowerTONDeployed': 'true', 
      'IsPowerTONStarted': 'true', 
      'IsManagerExported': 'true', 
      'Managers': {
        'TON': '0xe3a87a9343D262F5f11280058ae807B45aa34669', 
        'WTON': '0xcDB18cd1f6763a93287d20598427A50d3Ba9977f', 
        'DepositManager': '0xa8f67b988f3227158146da1C1c4854d2DCcdE67D', 
        'RootChainRegistry': '0xeE0aF430528311d2b48880E9055FB9f26fd64022', 
        'SeigManager': '0x2104cEC955b6FaBF603d8B2Ee0c28EA88886fa8C', 
        'PowerTON': '0x8a5A36F16dd9eD0032cfce1a0496e543B6c72098'
      }, 
      'Managers2': '', 
      'IpAddress': '13.231.50.44'
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
      'Name': 'Mainnet', 
      'IpAddress': '13.231.50.44', 
      'InstanceId': 'i-mainnet'
    }, 
    'Operator': {
      'Name': 'rinkeby-test', 
      'IpAddress': '13.231.10.253', 
      'InstanceId': 'i-04029f270b1e465e6', 
      'Genesis': '', 
      'ChainID': '2009'
    }, 
    'InstanceId': 'i-0e4472d7c5a5670a9', 
    'Status': 'pending', 
    'Date': 'Tue, 12 May 2020 07:54:53 GMT', 
    'Enode': '4966a7e4621c2c0b1b1b3295b4a35ccc4224ba1d529bf5aa2323e4650f6075bd5eb6618372b2579965819347307f1f97315ce91b09ca342d60c2e98ad88db9f3', 
    'IsInitialized': '', 
    'IpAddress': '52.197.85.100'
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
    'Name': 'Mainnet', 
    'InstanceId': 'i-mainnet', 
    'Status': 'mining', 
    'Date': '', 
    'Faucet': [], 
    'Operator': '', 
    'OperatorPassword': '', 
    'Staking': {
      'WithdrawalDelay': '10', 
      'SeigPerBlock': '1.5', 
      'PwertTONRoundTime': '60'
      }, 
      'IsScriptSet': 'true', 
      'IsMansgerDeployed': 'true', 
      'IsPowerTONDeployed': 'true', 
      'IsPowerTONStarted': 'true', 
      'IsManagerExported': 'true', 
      'Managers': {
        'TON': '0xe3a87a9343D262F5f11280058ae807B45aa34669', 
        'WTON': '0xcDB18cd1f6763a93287d20598427A50d3Ba9977f', 
        'DepositManager': '0xa8f67b988f3227158146da1C1c4854d2DCcdE67D', 
        'RootChainRegistry': '0xeE0aF430528311d2b48880E9055FB9f26fd64022', 
        'SeigManager': '0x2104cEC955b6FaBF603d8B2Ee0c28EA88886fa8C', 
        'PowerTON': '0x8a5A36F16dd9eD0032cfce1a0496e543B6c72098'
      }, 
      'Managers2': '', 
      'IpAddress': '13.231.50.44'
    },
    ...
]
[
  {
    'Type': 'operator', 
    'Name': 'rinkeby-test', 
    'ChainID': '2009', 
    'Epoch': '4096', 
    'PreAsset': 'true', 
    'RootChain': {
      'Name': 'Rinkeby', 
      'IpAddress': '13.231.233.189', 
      'InstanceId': 'i-rinkeby'
    }, 
    'InstanceId': 'i-04029f270b1e465e6', 
    'Status': 'pending', 
    'Date': 'Tue, 28 Apr 2020 10:59:09 GMT', 
    'RootchainId': 'i-rinkeby', 
    'NodeKey': 'e854e2f029be6364f0f961bd7571fd4431f99355b51ab79d23c56506f5f1a7c3',
    'OperatorAccount': '0x71562b71999873DB5b286dF957af199Ec94617F7', 
    'OperatorAccountKey': 'b71c71a67e1177ad4e901695e1b4b9ee17ae16c6668d313eac2f96dbcda3f291','OperatorPassword': '', 
    'StaminaOperatorAmount': '1', 
    'StaminaMinDeposit': '0.5', 
    'StaminaRecoverEpochLength': '120960', 
    'StaminaWithdrawalDelay': '362880', 
    'Dashboard': {
      'OperatorName': 'rinkeby-test', 
      'Website': 'tokamak.network', 
      'Description': 'Tokamak Network is a platform that assures decentralized and secure property same as Ethereum Main chain while supporting high level of scalability and extendability.', 
      'ApiServer': '13.124.77.81:9001'
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
    'Name': 'rinkeby-test', 
    'ChainID': '2009', 
    'Epoch': '4096', 
    'PreAsset': 'true', 
    'RootChain': {
      'Name': 'Rinkeby', 
      'IpAddress': '13.231.233.189', 
      'InstanceId': 'i-rinkeby'
    }, 
    'InstanceId': 'i-04029f270b1e465e6', 
    'Status': 'pending', 
    'Date': 'Tue, 28 Apr 2020 10:59:09 GMT', 
    'RootchainId': 'i-rinkeby', 
    'NodeKey': 'e854e2f029be6364f0f961bd7571fd4431f99355b51ab79d23c56506f5f1a7c3',
    'OperatorAccount': '0x71562b71999873DB5b286dF957af199Ec94617F7', 
    'OperatorAccountKey': 'b71c71a67e1177ad4e901695e1b4b9ee17ae16c6668d313eac2f96dbcda3f291','OperatorPassword': '', 
    'StaminaOperatorAmount': '1', 
    'StaminaMinDeposit': '0.5', 
    'StaminaRecoverEpochLength': '120960', 
    'StaminaWithdrawalDelay': '362880', 
    'Dashboard': {
      'OperatorName': 'rinkeby-test', 
      'Website': 'tokamak.network', 
      'Description': 'Tokamak Network is a platform that assures decentralized and secure property same as Ethereum Main chain while supporting high level of scalability and extendability.', 
      'ApiServer': '13.124.77.81:9001'
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
    'Name': 'rinkeby-test', 
    'ChainID': '2009', 
    'Epoch': '4096', 
    'PreAsset': 'true', 
    'RootChain': {
      'Name': 'Rinkeby', 
      'IpAddress': '13.231.233.189', 
      'InstanceId': 'i-rinkeby'
    }, 
    'InstanceId': 'i-04029f270b1e465e6', 
    'Status': 'pending', 
    'Date': 'Tue, 28 Apr 2020 10:59:09 GMT', 
    'RootchainId': 'i-rinkeby', 
    'NodeKey': 'e854e2f029be6364f0f961bd7571fd4431f99355b51ab79d23c56506f5f1a7c3',
    'OperatorAccount': '0x71562b71999873DB5b286dF957af199Ec94617F7', 
    'OperatorAccountKey': 'b71c71a67e1177ad4e901695e1b4b9ee17ae16c6668d313eac2f96dbcda3f291','OperatorPassword': '', 
    'StaminaOperatorAmount': '1', 
    'StaminaMinDeposit': '0.5', 
    'StaminaRecoverEpochLength': '120960', 
    'StaminaWithdrawalDelay': '362880', 
    'Dashboard': {
      'OperatorName': 'rinkeby-test', 
      'Website': 'tokamak.network', 
      'Description': 'Tokamak Network is a platform that assures decentralized and secure property same as Ethereum Main chain while supporting high level of scalability and extendability.', 
      'ApiServer': '13.124.77.81:9001'
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
/staking/info/<instanceid>
```
#### Success Response
```
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
