<template>
  <div class="pem-input">
    <div>
      <input
        id="accessKey"
        type="text"
        name="AccessKey"
        placeholder="Insert Key Pair Name"
      >
      <button type="submit">Create</button>
      <button type="submit">Delete</button>
    </div>
    <div class="row">
      <pem-table/>
    </div>
  </div>
</template>

<script>
import PemTable from '@/components/table/PemTable.vue';

export default {
  components: {
    'pem-input': PemTable,
  },
};

</script>
