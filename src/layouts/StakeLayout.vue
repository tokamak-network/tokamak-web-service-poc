<template>
  <div class="stake-layout">
    <container-header :title="'Stake/Unstake Controller'" />
    <Stake-container />
  </div>
</template>

<script>
import ContainerHeader from "@/containers/ContainerHeader.vue";
import StakeContainer from "@/containers/StakeContainer.vue";

export default {
  components: {
    "container-header": ContainerHeader,
    "Stake-container": StakeContainer
  }
};
</script>

<style scoped>
.stake-layout {
  border: solid 1px #ced6d9;
  background-color: #ffffff;
  border-radius: 6px;
}
</style>
