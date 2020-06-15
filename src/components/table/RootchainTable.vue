<template>
  <table class="rootchain-table">
    <thead>
      <tr>
        <th>Name</th>
        <th>Log</th>
        <th>Status</th>
        <th>*Status</th>
        <th>IP</th>
        <th>IP</th>
        <th>(re)set Scripts</th>
        <th>Is set?</th>
        <th>Start Node</th>
        <th>Deploy Seig Manager</th>
        <th>Deployed?</th>
        <th>Deploy PowerTON</th>
        <th>Deployed?</th>
        <th>Start PowerTON</th>
        <th>Started?</th>
        <th>Export Manager</th>
        <th>Exported?</th>
        <th>Shutdown</th>
        <th>Drop</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="rootchain in rootchain" :key="rootchain.Name">
        <!-- <td class="text-center">{{ index }}</td> -->
        <td class="clickable text-center name">{{ rootchain.Name }}</td>
        <td class="clickable text-center name">Log</td>
        <td class="clickable text-center name">
          <button @click="(checkNodeStatus(rootchain.InstanceId))">Status</button>
          <!-- <div class="button-container">
            <base-button :label="'Check Status'" :func="checkNodeStatus" :input="rootchain.instanceId" />
          </div> -->
        </td>
        <td class="clickable text-center name">{{ rootchain.Status }}</td>
        <td class="clickable text-center name">
          <button @click="(checkNodeIP(rootchain.InstanceId))">IP Address</button>
        </td>
        <td class="clickable text-center name">{{ rootchain.IpAddress }}</td>
        <td class="clickable text-center name">
          <button @click="(reset(rootchain.InstanceId))">3.(re)Set</button>
        </td>
        <td class="clickable text-center name">{{ rootchain.IsScriptSet }}</td>
        <td class="clickable text-center name">
          <button @click="(run(rootchain.InstanceId))">4.Run</button>
        </td>
        <td class="clickable text-center name">
          <button @click="(deploySeig(rootchain.InstanceId))">5.Deploy</button>
        </td>
        <td class="clickable text-center name">
          {{ rootchain.IsManagerDeployed }}
        </td>
        <td class="clickable text-center name">
          <button @click="(deployPowerTon(rootchain.InstanceId))">6.Deploy</button>
        </td>
        <td class="clickable text-center name">
          {{ rootchain.IsPowerTONDeployed }}
        </td>
        <td class="clickable text-center name">
          <button @click="(startPowerTon(rootchain.InstanceId))">7.Start</button>
        </td>
        <td class="clickable text-center name">
          {{ rootchain.IsPowerTONStarted }}
        </td>
        <td class="clickable text-center name">
          <button @click="(getManager(rootchain.InstanceId))">8.Export</button>
        </td>
        <td class="clickable text-center name">
          {{ rootchain.IsMangerExported }}
        </td>
        <td class="clickable text-center name">
          <div class="button-container">
            <base-button :label="'Shutdown'" :func="terminate" />
          </div>
          <button @click="(terminate(rootchain.InstanceId))">Shutdown</button>
        </td>
        <td class="clickable text-center name">
          <button @click="(drop(rootchain.InstanceId))">Drop</button>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script>
import {
  getRootchains,
  runRootchain,
  deploySeigManger,
  deployPowerTonContract,
  startPowerTonContract,
  getManagerContract,
  checkStatus,
  checkIP,
  getInstanceInfo,
  resetInstance,
  getLog,
  terminateInstance,
  dropData,
} from '@/api/index.js';
import BaseButton from '@/components/BaseButton.vue';

export default {
  components: {
    'base-button': BaseButton,
  },
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

      for (let i = 0; i < Object.keys(root).length; i++) {
        await this.rootchain.push(root[i]);
      }
    },
    async run (instanceId) {
      await runRootchain(instanceId);
    },
    async deploySeig (instanceId) {
      await deploySeigManger(instanceId);
    },
    async deployPowerTon (instanceId) {
      await deployPowerTonContract(instanceId);
    },
    async startPowerTon (instanceId) {
      await startPowerTonContract(instanceId);
    },
    async getManager (instanceId) {
      await getManagerContract(instanceId);
    },
    async checkNodeStatus (instanceId) {
      console.log(instanceId);
      await checkStatus(instanceId);
    },
    async checkNodeIP (instanceId) {
      await checkIP(instanceId);
      await getRootchains();
    },
    async getInfo (instanceId) {
      await getInstanceInfo(instanceId);
    },
    async reset (instanceId) {
      await resetInstance(instanceId);
    },
    async log (instanceId) {
      await getLog(instanceId);
    },
    async terminate (instanceId) {
      await terminateInstance(instanceId);
    },
    async IP (instanceId) {
      await checkIP(instanceId);
    },
    async drop (instanceId) {
      await dropData(instanceId);
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

.rootchain-table td,
.rootchain-table th {
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

.button-container {
  background-color: #c4c4c4;
  border: 1px solid #c4c4c4;
  text-align: center;
  font-size: 10px;
  border-radius: 6px;
}

.button-container:hover {
  -webkit-filter: opacity(0.8);
  filter: opacity(0.8);
}
</style>
