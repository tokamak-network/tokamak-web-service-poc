<template>
  <div class="config-input">
    <fieldset class="form-group">
      <legend class="col-form-label col-sm-2 pt-0">AWS Access</legend>
      <div>
        <div class="form-group row">
          <div class="label-container">ACCESS KEY</div>
          <div class="input-container">
            <input
              :value="newConfig.accessKey"
              @keypress="isNumber"
              @input="updateConfig"
            />
          </div>
        </div>
        <div class="form-group row">
          <div class="label-container">SECRET KEY</div>
          <div class="input-container">
            <input :value="newConfig.secretKey" @input="updateConfig" />
          </div>
        </div>
      </div>
    </fieldset>

    <fieldset class="form-group">
      <legend class="col-form-label col-sm-2 pt-0">AWS Instance</legend>
      <div>
        <div class="form-group row">
          <div class="label-container">IMAGE ID</div>
          <div class="input-container">
            <input :value="newConfig.imageId" />
          </div>
        </div>
        <div class="form-group row">
          <div class="label-container">INSTANCE TYPE</div>
          <div class="input-container">
            <input :value="newConfig.instanceType" />
          </div>
        </div>
        <div class="form-group row">
          <div class="label-container">
            SECURITY GROUP ID
          </div>
          <div class="input-container">
            <input :value="newConfig.securityGroupID" />
          </div>
        </div>
        <div class="form-group row">
          <div class="label-container">KEY NAME</div>
          <div class="input-container">
            <input :value="newConfig.keyName" />
          </div>
        </div>
        <div class="form-group row">
          <div class="label-container">REGION NAME</div>
          <div class="input-container">
            <input :value="newConfig.region" />
          </div>
        </div>
      </div>
    </fieldset>

    <fieldset class="form-group">
      <legend class="col-form-label col-sm-2 pt-0">SSH</legend>
      <div>
        <div class="form-group row">
          <div class="label-container">SSH USERNAME</div>
          <div class="input-container">
            <input :value="newConfig.sshUserName" />
          </div>
        </div>
        <div class="form-group row">
          <div class="label-container">SSH PEMFILE</div>
          <div class="input-container">
            <input :value="newConfig.sshPemFile" />
          </div>
        </div>
      </div>
    </fieldset>

    <fieldset class="form-group">
      <legend class="col-form-label col-sm-2 pt-0">Server</legend>
      <div>
        <div class="form-group row">
          <div class="label-container">DEBUG</div>
          <div class="input-container">
            <input :value="newConfig.debug" />
          </div>
        </div>
        <div class="form-group row">
          <div class="label-container">SECRET KEY</div>
          <div class="input-container">
            <input :value="newConfig.dbSecretKey" />
          </div>
        </div>
        <div class="form-group row">
          <div class="label-container">USERNAME</div>
          <div class="input-container">
            <input :value="newConfig.dbUserName" />
          </div>
        </div>
        <div class="form-group row">
          <div class="label-container">PASSWORD</div>
          <div class="input-container">
            <input :value="newConfig.dbPassword" />
          </div>
        </div>
      </div>
    </fieldset>

    <fieldset class="form-group">
      <legend class="col-form-label col-sm-2 pt-0">DATABASE</legend>
      <div class="form-group row">
        <div class="label-container">DATABASE NAME</div>
        <div class="input-container">
          <input :value="newConfig.dbName" />
        </div>        
      </div>
    </fieldset>
  </div>
</template>

<script>
export default {
  props: {
    accessKey: {
      type: String,
      default: '',
    },
  },
  data() {
    return {
      errors: [],
      newConfig: {
        accessKey: '',
        secretKey: '',
        imageId: '',
        instanceType: '',
        securityGroupID: '',
        keyName: '',
        region: '',
        sshUserName: '',
        sshPemFile: '',
        debug: '',
        dbSecretKey: '',
        dbPassword: '',
        dbName: ''
      }
    }
  },
  
  methods: {
    isNumber (evt) {
      evt = (evt) ? evt : window.event;
      const charCode = (evt.which) ? evt.which : evt.keyCode;
      if ((charCode > 31 && (charCode < 48 || charCode > 57)) && charCode !== 46) {
        evt.preventDefault();
      } else {
        return true;
      }
    },
    updateConfig () {
      this.$emit(this.newConfig);
    },
    checkForm: function (e) {
      this.errors = [];

      if (!this.newConfig.accessKey) {
        this.errors.push("Access key required.")      
      }

      e.preventDefault();
    }
  },
}
</script>

<style scoped>
.config {
  width: 100%;

  display: flex;
  flex-direction: row;
  border-top: solid 1px #ced6d9;
  border-bottom: solid 1px #ced6d9;
  padding-top: 0.6px;
  padding-bottom: 0.6px;
}
.form-group {
  margin-top: 3px;
  margin-bottom: 3px;
}
.row {
  margin-top: 3px;
  margin-bottom: 3px;
}
.label-container {
  display: flex;
  justify-content: center;
  align-items: center;
  float: left;
  width: 30%;
}

span {
  display: block;
  overflow: hidden;
  text-align: center;
  font-size: 14px;
}

.input-container {
  flex: 1;
  display: table;
  height: 100%;
  float: right;
  width: 70%;
}

input {
  display: table-cell;
  width: 95%;
  height: 100%;
  font-size: 14px;
  text-align: right;
  border: none;
  border: solid 1px #ced6d9;
  padding-right: 6px;
}

span {
  font-size: 10px;
  font-weight: normal;
  font-stretch: normal;
  font-style: normal;
  letter-spacing: normal;
  color: #161819;
}

.amount {
  margin-left: 4px;
  margin-right: 4px;
}

.unit {
  margin-left: 12px;
  margin-right: 4px;
}
</style>
