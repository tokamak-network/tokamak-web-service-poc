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
        <config-input v-model="configInput" />        
      </div>
      <div class="form-group row">
        <div class="col-sm-10">
          <button type="submit" class="btn btn-primary">CREATE</button>
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
import BaseTab from '@/components/BaseTab.vue';
import ConfigInput from '@/components/ConfigInput.vue'
import PemInput from '@/components/PemInput.vue'

export default {
  components: {
    'base-tab': BaseTab,
    'config-input': ConfigInput,
    'pem-input': PemInput
  },
  data() {
    return {
      tab: 'left',
      configInput: '',
      pemInput: ''
    };
  },
  methods: {
    changeTab (tab) {
      this.tab = tab;
    }
  }
};
</script>
