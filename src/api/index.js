import axios from 'axios';

function createInstance () {
  return axios.create({
    baseURL: 'http://localhost:8000',
  });
}

const instance = createInstance();

////////////////
//ABOUT CONFIG//
////////////////
export async function getConfig () {
  const res = await instance.get('/config');
  if (res.data === '') return [];
  else return res.data;
}

export async function setConfig (params) {
  const res = await instance.post('/config/set', {
    AccessKey : params.AccessKey,
    AwsSecretKey : params.AwsSecretKey,
    ImageID : params.ImageID,
    InstanceType : params.InstanceType,
    SecurityGroupID : params.SecurityGroupID,
    KeyName : params.KeyName,
    RegionName : params.RegionName,
    SshUsername : params.SshUsername,
    SshPemfile : params.SshPemfile,
    Debug : params.Debug,
    SecretKey : params.SecretKey,
    Username : params.Username,
    Password : params.Password,
    Database : params.Database,
  });
  return res.data;
}

export async function getNodes () {
  const res = await instance.get('/home');
  if (res.data === '') return [];
  else return res.data;
}

///////////////////
//ABOUT ROOTCHAIN//
///////////////////
export async function getRootchains () {
  const res = await instance.get('/rootchain');
  if (res.data === '') return [];
  else return res.data;
}

export async function createRootchainInstance (params) {
  const res = await instance.post('/rootchain/create', {
    Name: params.instanceName,
    Key1Address: params.operatorAddress,
    Key1: params.operatorKey,
    Password: params.operatorPassword,
    Key2: params.faucet2Key,
    Key3: params.faucet3Key,
    Key4: params.faucet4Key,
    Key5: params.faucet5Key,
    Key6: params.faucet6Key,
    WithdrawalDelay: params.withdrawalDelay,
    Seigniorage: params.seigPerBlock,
    PowerTONRound: params.roundTime,
  });

  return res.data;
}

export async function runRootchain (instanceId) {
  const res = await instance.post('/rootchain/startnode', {
    InstanceId: instanceId,
  });
  return res.data;
}

export async function resetRootchain (instanceId) {
  const res = await instance.post('/rootchain/reset', {
    InstanceId: instanceId,
  });
  return res.data;
}

export async function deploySeigManger (instanceId) {
  const res = await instance.post('/rootchain/${instanceId}/manager', {
    InstanceId: instanceId,
  });
  return res.data;
}

export async function deployPowerTonContract (instanceId) {
  const res = await instance.post('/rootchain/${instanceId}/powerton/deploy', {
    InstanceId: instanceId,
  });
  return res.data;
}

export async function startPowerTonContract (instanceId) {
  const res = await instance.post('/rootchain/${instanceId}/powerton/start', {
    InstanceId: instanceId,
  });
  return res.data;
}

export async function getManagerContract (instanceId) {
  const res = await instance.get('/rootchain/${instanceId}/manager');
  return res.data;
}

//////////////////
//ABOUT OPERATOR//
//////////////////
export async function getOperators () {
  const res = await instance.get('/operator');
  if (res.data === '') return [];
  else return res.data;
}

export async function setOperatorVariable (instanceId) {
  const res = await instance.post('/operator/${instanceId}/variable');
  return res.data;
}

export async function deployRootchainContract (instanceId) {
  const res = await instance.post('/operator/${instanceId}/rootchain');
  return res.data;
}

export async function exportGenesis (instanceId) {
  const res = await instance.post('/operator/${instanceId}/genesis');
  return res.data;
}

export async function initOperator (instanceId) {
  const res = await instance.post('/operator/${instanceId}/init');
  return res.data;
}

export async function importManagerContract (instanceId) {
  const res = await instance.get('/operator/${instanceId}/managers');
  return res.data;
}

export async function registerManagerContract (instanceId) {
  const res = await instance.post('/operator/${instanceId}/managers');
  return res.data;
}

export async function registerToDashboard (instanceId) {
  const res = await instance.post('/operator/${instanceId}/dashboard');
  return res.data;
}

export async function startOperator (instanceId) {
  const res = await instance.post('/operator/${instanceId}');
  return res.data;
}

//////////////////
//ABOUT USERNODE//
//////////////////
export async function createUsernode (params) {
  const res = await instance.post('/usernonde', {
    Name: params.instanceName,
    Key1Address: params.operatorAddress,
    Key1: params.operatorKey,
    Password: params.operatorPassword,
    Key2: params.faucet2Key,
    Key3: params.faucet3Key,
    Key4: params.faucet4Key,
    Key5: params.faucet5Key,
    Key6: params.faucet6Key,
    WithdrawalDelay: params.withdrawalDelay,
    Seigniorage: params.seigPerBlock,
    PowerTONRound: params.roundTime,
  });

  return res.data;
}

export async function initUsernode (instanceId) {
  const res = await instance.post('/usernode/${instanceId}/init');
  return res.data;
}

export async function runUsernode (instanceId) {
  const res = await instance.post('/usernode/${instanceId}');
  return res.data;
}

export async function getUsernodes () {
  const res = await instance.get('/usernode');
  if (res.data === '') return [];
  else return res.data;
}

/////////////////
//ABOUT STAKING//
/////////////////
