<template>
  <table class="opeartor-table">
    <thead>
      <tr>
        <th>Name</th>
        <th>Rootchain</th>
        <th>Log</th>
        <th>Status</th>
        <th>Status</th>
        <th>IP</th>
        <th>IP</th>
        <th>(re)set scripts</th>
        <th>Is Set?</th>
        <th>Set Variable</th>
        <th>Is Set?</th>
        <th>Deploy Rootchain</th>
        <th>Deployed?</th>
        <th>Export Genesis</th>
        <th>Exported?</th>
        <th>Init Genesis</th>
        <th>Initialized?</th>
        <th>Import managers</th>
        <th>Is Imported?</th>
        <th>Set Managers</th>
        <th>Is Set?</th>
        <th>Register Managers</th>
        <th>Is Registered?</th>
        <th>Register Operator</th>
        <th>Is Registered?</th>
        <th>Run Operator</th>
        <th>Shutdown</th>
        <th>Drop</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="operator in operator" :key="operator.Name">
        <!-- <td class="text-center">{{ index }}</td> -->
        <td class="clickable text-center name" >{{ operator.Name }}</td>
        <td class="clickable text-center name" >{{ operator.RootChain.Name }}</td>
        <td class="clickable text-center name" >Log</td>
        <td class="clickable text-center name" >Check Status</td>
        <td class="clickable text-center name" >{{ operator.Status }}</td>
        <td class="clickable text-center name" >IpAddress</td>
        <td class="clickable text-center name" >{{ operator.IpAddress }}</td>
        <td class="clickable text-center name" >3.(re)set</td>
        <td class="clickable text-center name" >{{ operator.IsScriptSet }}</td>
        <td class="clickable text-center name" >4.Set Variable</td>
        <td class="clickable text-center name" >{{ operator.IsSet }}</td>
        <td class="clickable text-center name" >5.Deploy</td>
        <td class="clickable text-center name" >{{ operator.IsDeployed }}</td>
        <td class="clickable text-center name" >6.Export</td>
        <td class="clickable text-center name" >{{ operator.IsExported }}</td>
        <td class="clickable text-center name" >7.Init</td>
        <td class="clickable text-center name" >{{ operator.IsInitialized }}</td>
        <td class="clickable text-center name" >8.Import</td>
        <td class="clickable text-center name" >{{ operator.IsManagersImported }}</td>
        <td class="clickable text-center name" >9.Set</td>
        <td class="clickable text-center name" >{{ operator.IsManagersSet }}</td>
        <td class="clickable text-center name" >10.Register</td>
        <td class="clickable text-center name" >{{ operator.IsManagersRegistered }}</td>
        <td class="clickable text-center name" >11.Register</td>
        <td class="clickable text-center name" >{{ operator.IsOperatorRegistered }}</td>
        <td class="clickable text-center name" >12.Run Node</td>
        <td class="clickable text-center name" >Terminate</td>
        <td class="clickable text-center name" >Drop</td>
      </tr>
    </tbody>
  </table>
</template>

<script>
import { getOperators } from '@/api/index.js';

export default {
  data () {
    return {
      name: '',
      ip: '',
      status: '',
      instanceId: '',
      operator: [],
    };
  },
  computed: {
    orderedOperator () {
      return [];
    },
  },
  created () {
    this.getOperator();
  },
  methods: {
    async getOperator () {
      const self = this;
      const oper = await getOperators();

      for (let i=0;i<Object.keys(oper).length;i++) {
        await this.operator.push(oper[i]);
      }
    },
  },
};
</script>

<style scoped>
.operator-table {
  width: 100%;
  table-layout: auto;
  border-collapse: collapse;
  border-spacing: 0;
  background: #ffffff;
}

.operator-table td, .operator-table th {
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
