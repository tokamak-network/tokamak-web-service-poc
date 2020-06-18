<template>
  <div class="stake-container">
    <Stake-table v-if="show === false" @op-clicked="changeOpView" />
    <Stake-operator v-else />
  </div>
</template>

<script>
import StakeTable from "@/components/table/StakeTable.vue";
import StakeOperator from "@/components/StakeOperator.vue";
export default {
  components: {
    "Stake-table": StakeTable,
    "Stake-operator": StakeOperator
  },
  data() {
    return {
      show: false
    };
  },
  methods: {
    changeOpView(click) {
      this.show = click;
    }
  }
};
</script>

<style scoped>
.column {
  border: solid 1px #ced6d9;
  background-color: #ffffff;
  border-radius: 6px;
}
.stake-container {
  display: flex;
  margin-left: auto;
  margin-right: auto;
  min-width: 960px;
  max-width: 960px;
  /* justify-content: center; */
}
</style>
