<template>
  <div class="usernode-container">
    <div class="row-reverse">
      <base-tab
        :left-label="'List'"
        :right-label="'Create'"
        :tab="tab"
        @tab-changed="changeTab"
      />
    </div>
    <div v-if="tab === 'left'">
      <usernode-table />
    </div>
    <form v-else>
      <fieldset>
        <legend>Usernode Info</legend>
        <string-input v-model="usernodeName" label="Usernode Name"/>
        <string-input v-model="rootchainName" label="Rootchain"/>
        <string-input v-model="operatorName" label="Operator"/>
        <string-input v-model="enodeHex" label="Enode Hex"/>
      </fieldset>
    </form>
  </div>
</template>

<script>
import BaseTab from '@/components/BaseTab.vue';
import UsernodeTable from '@/components/table/UsernodeTable.vue';
import StringInput from '@/components/StringInput.vue';
import IntInput from '@/components/IntInput.vue';

export default {
  components: {
    'base-tab': BaseTab,
    'usernode-table': UsernodeTable,
    'string-input': StringInput,
    'int-input': IntInput,
  },
  data () {
    return {
      tab: 'left',
      usernodeInput: '',
      usernodeName: '',
      rootchainName: '',
      operatorName: '',
      enodeHex: '',
    };
  },
  computed: {
    newUsernodeConfig: function () {
      return {
        usernodeName: this.usernodeName,
        rootchainName: this.rootchainName,
        operatorName: this.operatorName,
        enodeHex: this.enodeHex,
      };
    },
  },
  methods: {
    changeTab (tab) {
      this.tab = tab;
    },
  },
};
</script>
