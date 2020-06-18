<template>
  <table class="opeartor-table">
    <thead>
      <tr>
        <th>Operator Name</th>
        <th>Operator Staked</th>
        <th>Total Staked</th>
        <th>Network</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td class="clickable text-center name" @click="onClickOp(true)">hi</td>
        <td class="clickable text-center name">hi</td>
        <td class="clickable text-center name">hi</td>
        <td class="clickable text-center name">hi</td>
      </tr>
    </tbody>
  </table>
</template>
<script>
export default {
  methods: {
    onClickOp(click) {
      this.$emit("op-clicked", click);
    }
  }
};
</script>

<style scoped>
.stake-table {
  width: 100%;
  table-layout: auto;
  border-collapse: collapse;
  border-spacing: 0;
  background: #ffffff;
}

.stake-table td,
.stake-table th {
  border-top: solid 0.5px #dce2e5;
  /* border: 1px solid #555561; */
  /* padding: 8px; */
}

tbody tr:hover {
  background-color: #f8f8f8;
}

.pointer {
  cursor: pointer;
}

tbody .clickable {
  font-weight: bolder;
  text-decoration: underline;
}

.dashboard-stake-table th {
  text-align: left;
}

.dashboard-stake-table td {
  text-align: left;
}

.dashboard-stake-table .text-center {
  text-align: center;
}

.dashboard-stake-table .text-right {
  text-align: right;
}

th {
  padding: 6px;
  background-color: #f6f8f9;
  font-family: Roboto;
  font-size: 9px;
  font-weight: normal;
  font-stretch: normal;
  font-style: normal;
  letter-spacing: normal;
  text-align: center;
  color: #7e8d93;
}

td {
  padding: 12px;
  font-family: Roboto;
  font-size: 10px;
  font-weight: 300;
  font-stretch: normal;
  font-style: normal;
  letter-spacing: normal;
  text-align: center;
  color: #161819;
}

.name {
  width: 160px;
  word-break: break-all;
}
</style>
