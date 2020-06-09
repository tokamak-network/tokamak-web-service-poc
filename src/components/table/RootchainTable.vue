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
      <tr v-for="(rootchain, index) in orderedRootchain" :key="rootchain">
        <td class="text-center">{{ index }}</td>
        <td class="clickable text-center name" >{{ rootchain.Name }}</td>
        <td class="clickable text-center name" >{{ rootchain.Status }}</td>
        <td class="clickable text-center name" >{{ rootchain.InstanceId }}</td>
      </tr>
    </tbody>
  </table>
</template>

<script>
import axios from 'axios';

export default {
  data () {
    return {
      name: '',
      ip: '',
      status: '',
      instance_id: '',
      rootchain: {}
    }
  },
  created() {
    this.getRootchain()
  },
  computed: {
    orderedRootchain () {
      return [];
    }
  },
  methods: {
    getRootchain: function () {
      const self = this;
      axios.get('http://localhost:8000/rootchain').then(function (response) {
        // console.log(response.data)
        self.rootchain = response.data
        // console.log(self.rootchain[0])
      })
    }
  }
}
</script>