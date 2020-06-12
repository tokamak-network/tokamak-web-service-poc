import axios from 'axios';

function createInstance () {
  return axios.create({
    baseURL: 'http://localhost:8000',
  });
}

const instance = createInstance();

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

export async function getRootchains () {
  const res = await instance.get('/rootchain');
  if (res.data === '') return [];
  else return res.data;
}

export async function getOperators () {
  const res = await instance.get('/operator');
  if (res.data === '') return [];
  else return res.data;
}

export async function getUsernodes () {
  const res = await instance.get('/usernode');
  if (res.data === '') return [];
  else return res.data;
}

export async function getNodes () {
  const res = await instance.get('/home');
  if (res.data === '') return [];
  else return res.data;
}

export async function createRootchainInstance (params) {
  const res = await instance.post('/rootchain/', {
    operatorAddress: params.operatorAddress,
    operatorKey: params.operatorKey,
    operatorPassword: params.operatorPassword,
    faucet2Key: params.faucet2Key,
    faucet3Key: params.faucet3Key,
    faucet4Key: params.faucet4Key,
    faucet5Key: params.faucet5Key,
    faucet6Key: params.faucet6Key,
    withdrawalDelay: params.withdrawalDelay,
    seigPerBlock: params.seigPerBlock,
    roundTime: params.roundTime,
  });

  return res.data;
}

export async function runRootchain () {
  const res = await instance.post('/rootchain/startnode');

  return res.data;
}

