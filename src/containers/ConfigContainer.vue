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
        <!-- ToDo: 인풋 값들 정의 해야함 -->
        <!-- <config-input v-model="configInput" /> -->
        <div class="row">
          <legend calss="">AWS Access</legend>
          <span class="access-key-label">ACCESS KEY</span>
        </div>
      </div>
      <fieldset class="form-group">
        <div class="row">
          <legend class="col-form-label col-sm-2 pt-0">AWS Access</legend>
          <div class="col-sm-10">
            <div class="form-group row">
              <label for="accessKey" class="col-sm-2 col-form-label"
                >ACCESS KEY</label
              >
              <div class="col-sm-10">
                <input
                  type="text"
                  class="form-control"
                  id="accessKey"
                  name="AccessKey"              
                />
              </div>
            </div>
            <div class="form-group row">
              <label for="awsSecretKey" class="col-sm-2 col-form-label"
                >SECRET KEY</label
              >
              <div class="col-sm-10">
                <input
                  type="text"
                  class="form-control"
                  id="awsSecretKey"
                  name="AwsSecretKey"
                />
              </div>
            </div>
          </div>
        </div>
      </fieldset>
      <fieldset class="form-group">
        <div class="row">
          <legend class="col-form-label col-sm-2 pt-0">AWS Instance</legend>
          <div class="col-sm-10">
            <div class="form-group row">
              <label for="imageID" class="col-sm-2 col-form-label"
                >IMAGE ID</label
              >
              <div class="col-sm-10">
                <input
                  type="text"
                  class="form-control"
                  id="imageID"
                  name="ImageID"                  
                />
              </div>
            </div>
            <div class="form-group row">
              <label for="instanceType" class="col-sm-2 col-form-label"
                >INSTANCE TYPE</label
              >
              <div class="col-sm-10">
                <input
                  type="text"
                  class="form-control"
                  id="instanceType"
                  name="InstanceType"                  
                />
              </div>
            </div>
            <div class="form-group row">
              <label for="securityGroupID" class="col-sm-2 col-form-label"
                >SECURITY GROUP ID</label
              >
              <div class="col-sm-10">
                <input
                  type="text"
                  class="form-control"
                  id="securityGroupID"
                  name="SecurityGroupID"                  
                />
              </div>
            </div>
            <div class="form-group row">
              <label for="keyName" class="col-sm-2 col-form-label"
                >KEY NAME</label
              >
              <div class="col-sm-10">
                <input
                  type="text"
                  class="form-control"
                  id="keyName"
                  name="KeyName"                  
                />
              </div>
            </div>
            <div class="form-group row">
              <label for="regionName" class="col-sm-2 col-form-label"
                >REGION NAME</label
              >
              <div class="col-sm-10">
                <input
                  type="text"
                  class="form-control"
                  id="regionName"
                  name="RegionName"                  
                />
              </div>
            </div>
          </div>
        </div>
      </fieldset>

      <fieldset class="form-group">
        <div class="row">
          <legend class="col-form-label col-sm-2 pt-0">SSH</legend>
          <div class="col-sm-10">
            <div class="form-group row">
              <label for="sshUsername" class="col-sm-2 col-form-label"
                >SSH USERNAME</label
              >
              <div class="col-sm-10">
                <input
                  type="text"
                  class="form-control"
                  id="sshUsername"
                  name="SshUsername"                  
                />
              </div>
            </div>
            <div class="form-group row">
              <label for="sshPemfile" class="col-sm-2 col-form-label"
                >SSH PEMFILE</label
              >
              <div class="col-sm-10">
                <input
                  type="text"
                  class="form-control"
                  id="sshPemfile"
                  name="SshPemfile"                  
                />
              </div>
            </div>
          </div>
        </div>
      </fieldset>

      <fieldset class="form-group">
        <div class="row">
          <legend class="col-form-label col-sm-2 pt-0">Server</legend>
          <div class="col-sm-10">
            <div class="form-group row">
              <label for="debug" class="col-sm-2 col-form-label">DEBUG</label>
              <div class="col-sm-10">
                <input
                  type="text"
                  class="form-control"
                  id="debug"
                  name="Debug"                  
                />
              </div>
            </div>
            <div class="form-group row">
              <label for="secretKey" class="col-sm-2 col-form-label"
                >SECRET KEY</label
              >
              <div class="col-sm-10">
                <input
                  type="text"
                  class="form-control"
                  id="secretKey"
                  name="SecretKey"                  
                />
              </div>
            </div>
            <div class="form-group row">
              <label for="username" class="col-sm-2 col-form-label"
                >USERNAME</label
              >
              <div class="col-sm-10">
                <input
                  type="text"
                  class="form-control"
                  id="username"
                  name="Username"                
                />
              </div>
            </div>
            <div class="form-group row">
              <label for="password" class="col-sm-2 col-form-label"
                >PASSWORD</label
              >
              <div class="col-sm-10">
                <input
                  type="text"
                  class="form-control"
                  id="password"
                  name="Password"                  
                />
              </div>
            </div>
          </div>
        </div>
      </fieldset>

      <fieldset class="form-group">
        <div class="row">
          <legend class="col-form-label col-sm-2 pt-0">DATABASE</legend>
          <div class="col-sm-10">
            <div class="form-group row">
              <label for="database" class="col-sm-2 col-form-label"
                >DATABASE NAME</label
              >
              <div class="col-sm-10">
                <input
                  type="text"
                  class="form-control"
                  id="database"
                  name="Database"                  
                />
              </div>
            </div>
          </div>
        </div>
      </fieldset>

      <div class="form-group row">
        <div class="col-sm-10">
          <button type="submit" class="btn btn-primary">CREATE</button>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import BaseTab from '@/components/BaseTab.vue';

export default {
  components: {
    'base-tab': BaseTab,
  },
  data() {
    return {
      tab: 'left',
      configInput: ''
    };
  },
  methods: {
    changeTab (tab) {
      this.tab = tab;
    }
  }
};
</script>
