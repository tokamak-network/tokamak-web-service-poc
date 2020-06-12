<template>
  <div class="config-container">
    <div class="row-reverse">
      <base-tab
        :left-label="'config.ini'"
        :right-label="'.pem file'"
        :tab="tab"
        @tab-changed="changeTab"
      />
    </div>
    <form v-if="tab === 'left'">
      <div class="column">
        <fieldset class="fieldset-container">
          <legend>AWS Access</legend>
          <string-input v-model="accessKey" label="ACCESS KEY" />
          <string-input v-model="secretKey" label="SECRET KEY"/>
        </fieldset>
        <fieldset class="fieldset-container">
          <legend>AWS Instance</legend>
          <string-input v-model="imageID" label="IMAGE ID" />
          <string-input v-model="instanceType" label="INSTANCE TYPE"/>
          <string-input v-model="securityGroupID" label="SECURITY GROUP ID"/>
          <string-input v-model="keyName" label="KEY NAME"/>
          <string-input v-model="region" label="REGION"/>
        </fieldset>
        <fieldset class="fieldset-container">
          <legend>SSH</legend>
          <string-input v-model="sshUserName" label="SSH USERNAME" />
          <string-input v-model="sshPemFile" label="SSH PEMFILE"/>
        </fieldset>
        <fieldset class="fieldset-container">
          <legend>Server</legend>
          <string-input v-model="debug" label="DEBUG" />
          <string-input v-model="dbSecretKey" label="SECRET KEY"/>
          <string-input v-model="dbUserName" label="USER NAME"/>
          <string-input v-model="dbPassword" label="PASSWORD"/>
        </fieldset>
        <fieldset class="fieldset-container">
          <legend>Database</legend>
          <string-input v-model="dbName" label="DATABASE NAME" />
        </fieldset>
      </div>
      <div class="form-group row">
        <div class="col-sm-10">
          <div class="button-container" style="margin-top: 16px;"><base-button :label="'CREATE'" :func="resetConfig" /></div>
        </div>
      </div>
      <!-- <div>
        <p> {{ getConfig }}</p>
      </div> -->
    </form>
    <form v-else>
      <div class="column">
        <pem-input v-model="pemInput" />
      </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
import BaseButton from '@/components/BaseButton.vue';
import BaseTab from '@/components/BaseTab.vue';
import StringInput from '@/components/StringInput.vue';
import PemInput from '@/components/PemInput.vue';
import { getConfig, setConfig } from '@/api/index.js';

export default {
  components: {
    'base-button': BaseButton,
    'base-tab': BaseTab,
    'string-input': StringInput,
    'pem-input': PemInput,
  },
  data () {
    return {
      tab: 'left',
      configInput: '',
      pemInput: '',
      accessKey: '',
      secretKey: '',
      imageID: '',
      instanceType: '',
      securityGroupID: '',
      keyName: '',
      region: '',
      sshUserName: '',
      sshPemFile: '',
      debug: '',
      dbSecretKey: '',
      dbUserName: '',
      dbPassword: '',
      dbName: '',
      params: {},
    };
  },
  computed: {
    newConfig: function () {
      return {
        accessKey: this.accessKey,
        secretKey: this.secretKey,
        imageID: this.imageID,
        instanceType: this.instanceType,
        securityGroupID: this.securityGroupID,
        keyName: this.keyName,
        region: this.region,
        sshUserName: this.sshUserName,
        sshPemFile: this.sshPemFile,
        debug: this.debug,
        dbSecretKey: this.dbSecretKey,
        dbUserName: this.dbUserName,
        dbPassword: this.dbPassword,
        dbName: this.dbName,
      };
    },
  },
  created () {
    this.currentConfig();
  },
  methods: {
    changeTab (tab) {
      this.tab = tab;
    },
    async currentConfig () {
      const config = await getConfig();
      const self = this;

      self.accessKey = config.aws_access_key;
      self.secretKey = config.aws_secret_key;
      self.imageID = config.basic_image_id;
      self.instanceType = config.instance_type;
      self.securityGroupID = config.security_group_id;
      self.keyName = config.key_name;
      self.region = config.region_name;
      self.sshUserName = config.ssh_username;
      self.sshPemFile = config.ssh_pemfile;
      self.debug = config.debug;
      self.dbSecretKey = config.secret_key;
      self.dbUserName = config.username;
      self.dbPassword = config.password;
      self.dbName = config.database;
    },
    async resetConfig () {
      const self = this;
      this.params = {
        'AccessKey': this.accessKey,
        'AwsSecretKey' : this.secretKey,
        'ImageID' : this.imageID,
        'InstanceType' : this.instanceType,
        'SecurityGroupID' : this.securityGroupID,
        'KeyName' : this.keyName,
        'RegionName' : this.region,
        'SshUsername' : this.sshUserName,
        'SshPemfile' : this.sshPemFile,
        'Debug' : this.debug,
        'SecretKey' : this.dbSecretKey,
        'Username' : this.dbUserName,
        'Password' : this.dbPassword,
        'Database' : this.dbName,
      };
      const config = await setConfig(this.params);
    },
  },
};
</script>


<style scoped>
.fieldset-container {
  display: flex;
  flex-direction: column;
  border-radius: 6px;
  border: solid 1px #ced6d9;
  background-color: #ffffff;
}

.name-container {
  padding-top: 12px;
  padding-bottom: 12px;
  margin-left: 16px;
}

.row {
  display: flex;
  flex-direction: row;
  align-items: center;
}

.name {
  width: 200px;
  padding-left: 16px;
  padding-right: 8px;
  font-family: Roboto;
  font-size: 16px;
  font-weight: bold;
  font-stretch: normal;
  font-style: normal;
  letter-spacing: normal;
  color: #161819;
  word-break: break-all;
}

.button {
  color: #ffffff;
  background-color: #35496b;
  border: 1px solid #35496b;
  text-align: center;
  font-size: 14px;
  border-radius: 4px;
  height: 22px;
  width: 40px;
  margin-right: 16px;
}

.button-container {
  color: #ffffff;
  background-color: #6fc4b3;
  border: 1px solid #6fc4b3;
  text-align: center;
  font-size: 10px;
  padding-top: 4px;
  padding-bottom: 4px;
  margin-left: 16px;
  margin-right: 16px;
  border-radius: 6px;
}

.button-container:hover {
  -webkit-filter: opacity(.8);
  filter: opacity(.8);
}

</style>
