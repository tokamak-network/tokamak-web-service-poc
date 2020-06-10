<template>
  <div class="operator-layout">
    <container-header :title="'OPERATOR Controller'"/>
    <operator-container />
  </div>
</template>

<script>
import ContainerHeader from '@/containers/ContainerHeader.vue';
import OperatorContainer from '@/containers/OperatorContainer.vue';

export default {
  components: {
    'container-header': ContainerHeader,
    'operator-container': OperatorContainer,
  },
};

</script>

<style scoped>
.operator-layout {
  border: solid 1px #ced6d9;
  background-color: #ffffff;
  border-radius: 6px;
}
</style>
