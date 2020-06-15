<template>
  <div>
    <div class="label-container">
      <label v-if="label">{{ label }}</label>
    </div>
    <div class="input-container">
      <select :value="value" @input="updateValue($event.target.value)" >
        <option v-for="item in items" :key="item" :value="item.InstanceId">{{ item.Name }}</option>
      </select>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    value: {
      type: String,
      default: '',
    },
    label: {
      type: String,
      default: '',
    },
    items: {
      // type: String,
      default: '',
    },
  },
  methods: {
    updateValue (value) {
      this.$emit('input', value);
    },
  },
};
</script>

<style scoped>
.form-group {
  margin-top: 3px;
  margin-bottom: 3px;
}
.row {
  margin-top: 3px;
  margin-bottom: 3px;
}
.label-container {
  display: flex;
  justify-content: center;
  align-items: center;
  float: left;
  width: 30%;
  color: #3e3e3e;
  font: roboto;
}

span {
  display: block;
  overflow: hidden;
  text-align: center;
  font-size: 14px;
}
.config-container {
  display: flex;
  flex-direction: column;
  border-radius: 6px;
  border: solid 1px #ced6d9;
  background-color: #ffffff;
}

.input-container {
  flex: 1;
  display: table;
  height: 100%;
  float: right;
  width: 70%;
}

input {
  display: table-cell;
  width: 95%;
  height: 100%;
  font-size: 14px;
  text-align: right;
  border: none;
  border: solid 1px #ced6d9;
  padding-right: 6px;
}

span {
  font-size: 10px;
  font-weight: normal;
  font-stretch: normal;
  font-style: normal;
  letter-spacing: normal;
  color: #161819;
}
</style>
