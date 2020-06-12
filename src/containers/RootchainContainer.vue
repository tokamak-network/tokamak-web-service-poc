<template>
  <div class="rootchain-container">
    <div class="row-reverse">
      <base-tab
        :left-label="'List'"
        :right-label="'Create'"
        :tab="tab"
        @tab-changed="changeTab"
      />
    </div>
    <div v-if="tab === 'left'">
      <rootchain-table />
    </div>
    <div v-else>
      <div class="column">
        <fieldset class="fieldset-container">
          <legend>Instance</legend>
          <string-input v-model="instanceName" label="Instance Name" />
        </fieldset >
        <fieldset class="fieldset-container">
          <legend>Key Setting</legend>
          <string-input v-model="operatorAddress" label="Operator Address" />
          <string-input v-model="operatorKey" label="Operator Key" />
          <password-input v-model="operatorPassword" label="Operator Password" />
          <string-input v-model="faucet2Key" label="Faucet2 key" />
          <string-input v-model="faucet3Key" label="Faucet3 key" />
          <string-input v-model="faucet4Key" label="Faucet4 key" />
          <string-input v-model="faucet5Key" label="Faucet5 key" />
          <string-input v-model="faucet6Key" label="Faucet6 key" />
        </fieldset>
        <fieldset class="fieldset-container">
          <legend>Stake Setting</legend>
          <int-input v-model="withdrawalDelay" label="Withdrawal Delay" />
          <int-input v-model="seigPerBlock" label="Seigniorage Per Block" />
          <int-input v-model="roundTime" label="Power TON Round Time" />
        </fieldset>
      </div>
      <div class="form-group row">
        <div class="button-container" style="margin-top: 16px;"><base-button :label="'CREATE'" :func="createRootchain" /></div>
      </div>
    </div>
  </div>
</template>

<script>
import { getRootchains, createRootchainNode } from '@/api/index.js';

import BaseButton from '@/components/BaseButton.vue';
import BaseTab from '@/components/BaseTab.vue';
import RootchainTable from '@/components/table/RootchainTable.vue';
import StringInput from '@/components/StringInput.vue';
import IntInput from '@/components/IntInput.vue';
import PasswordInput from '@/components/PasswordInput.vue';


export default {
  components: {
    'base-button': BaseButton,
    'base-tab': BaseTab,
    'rootchain-table': RootchainTable,
    'string-input': StringInput,
    'int-input': IntInput,
    'password-input': PasswordInput,
  },
  data () {
    return {
      tab: 'left',
      instanceName: '',
      operatorAddress: '0x71562b71999873DB5b286dF957af199Ec94617F7',
      operatorKey: 'b71c71a67e1177ad4e901695e1b4b9ee17ae16c6668d313eac2f96dbcda3f291',
      operatorPassword: '',
      faucet2Key: '',
      faucet3Key: '',
      faucet4Key: '',
      faucet5Key: '',
      faucet6Key: '',
      withdrawalDelay: 10,
      seigPerBlock: 1.5,
      roundTime: 60,
    };
  },
  computed: {
    newRootchainConfig: function () {
      return {
        instanceName: this.instanceName,
        operatorAddress: this.operatorAddress,
        operatorKey: this.operatorKey,
        operatorPassword: this.operatorPassword,
        faucet2Key: this.faucet2Key,
        faucet3Key: this.faucet3Key,
        faucet4Key: this.faucet4Key,
        faucet5Key: this.faucet5Key,
        faucet6Key: this.faucet6Key,
        withdrawalDelay: this.withdrawalDelay,
        seigPerBlock: this.seigPerBlock,
        roundTime: this.roundTime,
      };
    },
  },
  methods: {
    changeTab (tab) {
      this.tab = tab;
    },
    async createRootchain () {
      const self = this;
      this.params = {
        'instanceName': this.instanceName,
        'operatorAddress': this.operatorAddress,
        'operatorKey': this.operatorKey,
        'operatorPassword': this.operatorPassword,
        'faucet2Key': this.faucet2Key,
        'faucet3Key': this.faucet3Key,
        'faucet4Key': this.faucet4Key,
        'faucet5Key': this.faucet5Key,
        'faucet6Key': this.faucet6Key,
        'withdrawalDelay': this.withdrawalDelay,
        'seigPerBlock': this.seigPerBlock,
        'roundTime': this.roundTime,
      };

      const root = await createRootchainNode(this.params);
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
