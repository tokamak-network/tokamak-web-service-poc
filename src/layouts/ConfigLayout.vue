<template>
  <div class="config-layout">
    <container-header :title="'Config'" />
    <config-container />
  </div>
</template>

<script>
import { mapState } from 'vuex';
import ContainerHeader from '@/containers/ContainerHeader.vue';
import ConfigContainer from '@/containers/ConfigContainer.vue';

export default {
  components: {
    'container-header': ContainerHeader,
    'config-container': ConfigContainer,
  },
};
</script>
<style scoped>
.config-layout {
  border: solid 1px #ced6d9;
  background-color: #ffffff;
  border-radius: 6px;
}
</style>