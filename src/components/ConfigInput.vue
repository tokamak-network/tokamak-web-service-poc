<template>
  <div class="config-input">
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
              <input type="text" class="form-control" id="debug" name="Debug" />
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
  </div>
</template>


<style scoped>
.config-input {
  width: 100%;

  display: flex;
  flex-direction: row;
  border-top: solid 1px #ced6d9;
  border-bottom: solid 1px #ced6d9;
  padding-top: 0.6px;
  padding-bottom: 0.6px;
}

.label-container {
  display: flex;
  justify-content: center;
  align-items: center;
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
}

input {
  display: table-cell;
  width: 100%;
  height: 100%;
  font-size: 14px;
  text-align: right;
  border: none;
  border-left: solid 1px #ced6d9;
  border-right: solid 1px #ced6d9;
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