<template>
  <div class="operator-container">
    <div class="row-reverse">
      <base-tab
        :left-label="'List'"
        :right-label="'Create'"
        :tab="tab"
        @tab-changed="changeTab"
      />
    </div>
    <div v-if="tab === 'left'">
      <operator-table />
    </div>
    <div v-else>
      <div class="column">
        <fieldset class="fieldset">
          <legend>Chain Info</legend>
          <string-input v-model="operatorName" label="Operator Name" />
          <select-input v-model="rootchainName" :items="rootList" v-bind="rootList" label="Rootchain Name"/>
          <int-input v-model="chainID" label="Chain ID" />
          <int-input v-model="epoch" label="Epoch" />
        </fieldset>
        <fieldset>
          <legend>Operator Info</legend>
          <string-input v-model="nodeKeyHex" label="Nodekey Hex" />
          <string-input v-model="operatorAddress" label="Operator Address" />
          <string-input v-model="operatorKey" label="Operator Key" />
          <password-input v-model="operatorPassword" label="Operator Password"/>
        </fieldset>
        <fieldset>
          <legend>Gasprice Info</legend>
          <int-input v-model="deployGasprice" label="Deploy Gasprice" />
          <int-input v-model="commitGasprice" label="Commit Gasprice" />
        </fieldset>
        <fieldset>
          <legend>Stamina Info</legend>
          <int-input v-model="operatorAmount" label="Operator Amount" />
          <int-input v-model="minDeposit" label="Min Deposit" />
          <int-input v-model="recoverLength" label="Recover Epoch Length" />
          <int-input v-model="withdrawalDelay" label="Withdrawal Delay" />
        </fieldset>
        <fieldset>
          <legend>Staking Info</legend>
          <string-input v-model="website" label="Website" />
          <string-input v-model="description" label="Description" />
          <string-input v-model="apiServer" label="Api Server" />
        </fieldset>
        <div class="form-group row">
          <div class="col-sm-10">
            <button :func="createOperator" type="button" @click="createOperator()">CREATE</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { createOperatorNode, getRootchains } from '@/api/index.js';

import BaseTab from '@/components/BaseTab.vue';
import OperatorTable from '@/components/table/OperatorTable.vue';
import StringInput from '@/components/StringInput.vue';
import IntInput from '@/components/IntInput.vue';
import PasswordInput from '@/components/PasswordInput.vue';

export default {
  components: {
    'base-tab': BaseTab,
    'operator-table': OperatorTable,
    'string-input': StringInput,
    'int-input': IntInput,
    'password-input': PasswordInput,
  },
  data () {
    return {
      tab: 'left',
      operatorName: '',
      rootchainName: '',
      chainID: 16,
      epoch: 4096,
      nodeKeyHex: 'e854e2f029be6364f0f961bd7571fd4431f99355b51ab79d23c56506f5f1a7c3',
      operatorAddress: '0x71562b71999873DB5b286dF957af199Ec94617F7',
      operatorKey: 'b71c71a67e1177ad4e901695e1b4b9ee17ae16c6668d313eac2f96dbcda3f291',
      operatorPassword: '',
      deployGasprice: 10000000000,
      commitGasprice: 10000000000,
      operatorAmount: 1,
      minDeposit: 0.5,
      recoverLength: 120960,
      withdrawalDelay: 362880,
      website: '',
      description: '',
      apiServer: '',
      rootList: [],
    };
  },
  computed: {
    // newOperatorConfig: function() {
    //   return {
    //     operatorName: this.operatorName,
    //     rootchainName: this.rootchainName,
    //     chainID: this.chainID,
    //     epoch: this.epoch,
    //     nodeKeyHex: this.nodeKeyHex,
    //     operatorAddress: this.operatorAddress,
    //     operatorKey: this.operatorKey,
    //     operatorPassword: this.operatorPassword,
    //     deployGasprice: this.deployGasprice,
    //     commitGasprice: this.commitGasprice,
    //     operatorAmount: this.operatorAmount,
    //     midDeposit: this.midDeposit,
    //     recoverLength: this.recoverLength,
    //     withdrawalDelay: this.withdrawalDelay,
    //     website: this.website,
    //     description: this.description,
    //     apiServer: this.apiServer,
    //   },
    // }
  },
  created () {
    this.rootchainList();
  },
  methods: {
    changeTab (tab) {
      this.tab = tab;
    },
    async createOperator () {
      const self = this;
      this.params = {
        'operatorName': this.operatorName,
        'rootchainName': this.rootchainName,
        'chainID': this.chainID,
        'epoch': this.epoch,
        'nodeKeyHex': this.nodeKeyHex,
        'operatorAddress': this.operatorAddress,
        'operatorKey': this.operatorKey,
        'operatorPassword': this.operatorPassword,
        'deployGasprice': this.deployGasprice,
        'commitGasprice': this.commitGasprice,
        'operatorAmount': this.operatorAmount,
        'minDeposit': this.minDeposit,
        'recoverLength': this.recoverLength,
        'withdrawalDelay': this.withdrawalDelay,
        'website': this.website,
        'description': this.description,
        'apiServer': this.apiServer,
      };
      const oper = await createOperatorNode(this.params);
    },
    async rootchainList () {
      const root = await getRootchains();
      for (let i=0;i<Object.keys(root).length;i++) {
        await this.rootList.push(root[i]);
      }
    },
  },
};
</script>

<style scoped>
.column {
  border: solid 1px #ced6d9;
  background-color: #ffffff;
  border-radius: 6px;
}
</style>
