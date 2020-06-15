<template>
  <table class="opeartor-table">
    <thead>
      <tr>
        <th>Name</th>
        <th>IP</th>
        <th>Status</th>
        <th>Instance ID</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="usernode in usernode" :key="usernode.Name">
        <!-- <td class="text-center">{{ index }}</td> -->
        <td class="clickable text-center name" >{{ usernode.Name }}</td>
        <td class="clickable text-center name" >{{ usernode.IpAddress }}</td>
        <td class="clickable text-center name" >{{ usernode.Status }}</td>
        <td class="clickable text-center name" >{{ usernode.InstanceId }}</td>
      </tr>
    </tbody>
  </table>
</template>

<script>
import { getUsernodes, checkStatus, checkIP, getInstanceInfo, resetInstance, getLog, terminateInstance, dropData } from '@/api/index.js';

export default {
  data () {
    return {
      name: '',
      ip: '',
      status: '',
      instanceId: '',
      usernode: [],
    };
  },
  computed: {
    orderedUsernode () {
      return [];
    },
  },
  created () {
    this.getUsernode();
  },
  methods: {
    async getUsernode () {
      const self = this;
      const user = await getUsernodes();

      for (let i=0;i<Object.keys(user).length;i++) {
        await this.usernode.push(user[i]);
      }
    },
  },
};
</script>

<style scoped>
.usernode-table {
  width: 100%;
  table-layout: auto;
  border-collapse: collapse;
  border-spacing: 0;
  background: #ffffff;
}

.usernode-table td, .usernode-table th {
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

.dashboard-usernode-table th {
  text-align: left;
}

.dashboard-usernode-table td {
  text-align: left;
}

.dashboard-usernode-table .text-center {
  text-align: center;
}

.dashboard-usernode-table .text-right {
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
