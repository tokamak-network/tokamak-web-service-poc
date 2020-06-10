<template>
  <div class="usernode-layout">
    <container-header :title="'USERNODE Controller'"/>
    <usernode-container />
  </div>
</template>

<script>
import ContainerHeader from '@/containers/ContainerHeader.vue';
import UsernodeContainer from '@/containers/UsernodeContainer.vue';

export default {
  components: {
    'container-header': ContainerHeader,
    'usernode-container': UsernodeContainer,
  },
};

</script>

<style scoped>
.usernode-layout {
  border: solid 1px #ced6d9;
  background-color: #ffffff;
  border-radius: 6px;
}
</style>
