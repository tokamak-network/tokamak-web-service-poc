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
    AccessKey : params.accessKey,
    AwsSecretKey : params.secretKey,
    ImageID : params.imageID,
    InstanceType : params.instanceType,
    SecurityGroupID : params.securityGroupID,
    KeyName : params.keyName,
    RegionName : params.region,
    SshUsername : params.sshUserName,
    SshPemfile : params.sshPemFile,
    Debug : params.debug,
    SecretKey : params.dbSecretKey,
    Username : params.dbUserName,
    Password : params.dbPassword,
    Database : params.dbName,
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
