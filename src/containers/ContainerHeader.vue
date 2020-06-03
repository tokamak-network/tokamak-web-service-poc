<template>
  <div class="container-header">
    <div class="title"><span>{{ title }}</span></div>
  </div>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      default: '',
    },
    path: {
      type: String,
      default: '',
    },
  },
};
</script>

<style scoped>
.container-header {
  display: flex;
  flex-direction: row;
  padding-top: 12px;
  padding-bottom: 12px;
}

.title {
  flex: 1;
  font-size: 14px;
  font-weight: normal;
  font-stretch: normal;
  font-style: normal;
  letter-spacing: normal;
  padding-left: 20px;
  color: #124b71;
}

button {
  margin-right: 8px;
  border: none;
  letter-spacing: 0.7px;
  font-size: 11px;
  font-weight: 300;
  font-stretch: normal;
  font-style: normal;
  line-height: 1.75;
  text-align: center;
  color: #bbb8b8;
}
</style>
