<template>
  <table class="rootchain-table">
    <thead>
      <tr>
        <th>Name</th>
        <th>IP</th>
        <th>Status</th>
        <th>Instance ID</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="rootchain in rootchain" :key="rootchain.Name">
        <!-- <td class="text-center">{{ index }}</td> -->
        <td class="clickable text-center name" >{{ rootchain.Name }}</td>
        <td class="clickable text-center name" >{{ rootchain.IpAddress }}</td>
        <td class="clickable text-center name" >{{ rootchain.Status }}</td>
        <td class="clickable text-center name" >{{ rootchain.InstanceId }}</td>
      </tr>
    </tbody>
  </table>
</template>

<script>
import { getRootchains } from '@/api/index.js';

export default {
  data () {
    return {
      name: '',
      ip: '',
      status: '',
      instanceId: '',
      rootchain: [],
    };
  },
  computed: {
    orderedRootchain () {
      return [];
    },
  },
  created () {
    this.getRootchain();
  },
  methods: {
    async getRootchain () {
      const self = this;
      const root = await getRootchains();

      for (let i=0;i<Object.keys(root).length;i++) {
        await this.rootchain.push(root[i]);
      }

    },
  },
};
</script>

<style scoped>
.rootchain-table {
  width: 100%;
  table-layout: auto;
  border-collapse: collapse;
  border-spacing: 0;
  background: #ffffff;
}

.rootchain-table td, .rootchain-table th {
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

.dashboard-operator-table th {
  text-align: left;
}

.dashboard-operator-table td {
  text-align: left;
}

.dashboard-operator-table .text-center {
  text-align: center;
}

.dashboard-operator-table .text-right {
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
