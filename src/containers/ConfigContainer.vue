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
        <fieldset>
          <legend>AWS Access</legend>
          <string-input v-model="accessKey" label="ACCESS KEY" />
          <string-input v-model="secretKey" label="SECRET KEY"/>
        </fieldset>
        <fieldset>
          <legend>AWS Instance</legend>
          <string-input v-model="imageID" label="IMAGE ID" />
          <string-input v-model="instanceType" label="INSTANCE TYPE"/>
          <string-input v-model="securityGroupID" label="SECURITY GROUP ID"/>
          <string-input v-model="keyName" label="KEY NAME"/>
          <string-input v-model="region" label="REGION"/>
        </fieldset>
        <fieldset>
          <legend>SSH</legend>
          <string-input v-model="sshUserName" label="SSH USERNAME" />
          <string-input v-model="sshPemFile" label="SSH PEMFILE"/>
        </fieldset>
        <fieldset>
          <legend>Server</legend>
          <string-input v-model="debug" label="DEBUG" />
          <string-input v-model="dbSecretKey" label="SECRET KEY"/>
          <string-input v-model="dbUserName" label="USER NAME"/>
          <string-input v-model="dbPassword" label="PASSWORD"/>
        </fieldset>
        <fieldset>
          <legend>Database</legend>
          <string-input v-model="dbName" label="DATABASE NAME" />
        </fieldset>
      </div>
      <div class="form-group row">
        <div class="col-sm-10">
          <button :func="resetConfig" type="button" @click="resetConfig()">CREATE</button>
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
import BaseTab from '@/components/BaseTab.vue';
import StringInput from '@/components/StringInput.vue';
import PemInput from '@/components/PemInput.vue';
import { getConfig, setConfig } from '@/api/index.js';

export default {
  components: {
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
      console.log(config);
    },
  },
};
</script>
