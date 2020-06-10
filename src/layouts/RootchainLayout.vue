<template>
  <div class="rootchain-layout">
    <container-header :title="'ROOTCHAIN Controller'"/>
    <rootchain-container />
  </div>
</template>

<script>
import ContainerHeader from '@/containers/ContainerHeader.vue';
import RootchainContainer from '@/containers/RootchainContainer.vue';

export default {
  components: {
    'container-header': ContainerHeader,
    'rootchain-container': RootchainContainer,
  },
};

</script>

<style scoped>
.rootchain-layout {
  border: solid 1px #ced6d9;
  background-color: #ffffff;
  border-radius: 6px;
}
</style>
