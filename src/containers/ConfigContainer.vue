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
          <button type="button" @click="newConfig()">CREATE</button>
        </div>
      </div>
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
import StringInput from '@/components/StringInput.vue'
import PemInput from '@/components/PemInput.vue'

export default {
  components: {
    'base-tab': BaseTab,
    'string-input': StringInput,
    'pem-input': PemInput
  },
  data() {
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
      dbName: ''
    };
  },
  created() {
    this.currentConfig()
  },
  methods: {
    changeTab (tab) {
      this.tab = tab;
    },
    currentConfig: function () {
      const self = this;
      axios.get('http://127.0.0.1:8000/config').then(function (response) {
        self.accessKey = response.data.aws_access_key;
        self.secretKey = response.data.aws_secret_key;
        self.imageID = response.data.basic_image_id;
        self.instanceType = response.data.instance_type;
        self.securityGroupID = response.data.security_group_id;
        self.keyName = response.data.key_name;
        self.region = response.data.region_name;
        self.sshUserName = response.data.ssh_username;
        self.sshPemFile = response.data.ssh_pemfile;
        self.debug = response.data.debug;
        self.dbSecretKey = response.data.secret_key;
        self.dbUserName = response.data.username;
        self.dbPassword = response.data.password;
        self.dbName = response.data.database;
      })
    },
    setConnfig: function () {
      const self = this;
      axios.post('http://127.0.0.1:8000/config').then(function (response) {
        AccessKey = this.accessKey,
        AwsSecretKey = this.secretKey,
        ImageID = this.imageID,
        InstanceType = this.instanceType,
        SecurityGroupID = this.securityGroupID,
        KeyName = this.keyName,
        RegionName = this.region,
        SshUsername = this.sshUserName,
        SshPemfile = this.sshPemFile,
        Debug = this.debug,
        SecretKey = this.dbSecretKey,
        Username = this.dbUserName,
        Password = this.dbPassword,
        Database = this.dbName
      })
    }
  },
  computed: {
    newConfig: function() {
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
        dbName: this.dbName
      }
    }
  }
};
</script>
