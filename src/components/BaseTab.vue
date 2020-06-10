<template>
  <div class="base-tab">
    <button :class="{ 'left-tab-clicked': tab === 'left' }" @click="onTabChanged('left')">
      {{ leftLabel }}
    </button>
    <button :class="{ 'right-tab-clicked': tab === 'right' }" @click="onTabChanged('right')">
      {{ rightLabel }}
    </button>
  </div>
</template>

<script>
export default {
  props: {
    leftLabel: {
      type: String,
    },
    rightLabel: {
      type: String,
    },
    tab: {
      type: String,
    },
  },
  methods: {
    onTabChanged (tab) {
      this.$emit('tab-changed', tab);
    },
  },
};
</script>

<style scoped>
.base-tab {
  display: flex;
  flex-direction: row;
  margin-top: 8px;
  margin-bottom: 8px;
}

button {
  width: 72px;
  height: 30px;
  padding-top: 2px;
  font-family: Roboto;
  font-weight: normal;
  font-stretch: normal;
  font-style: normal;
  letter-spacing: normal;
  font-size: 11px;
  color: #161819;
}

button:hover {
  cursor: pointer;
  background-color: #ecf1f3;
}

.left-tab {
  border-top-left-radius: 4px;
  border-bottom-left-radius: 4px;
  z-index: 2;
}

.left-tab-clicked {
  background-color: #2868af;
  color: #ffffff;
  z-index: 2;
}

.left-tab-clicked:hover {
  background-color: #1e4e85;
  color: #ffffff;
}

.right-tab {
  border-top-right-radius: 4px;
  border-bottom-right-radius: 4px;
}

.right-tab-clicked {
  background-color: #f38777;
  color: #ffffff;
  z-index: 2;
}

.right-tab-clicked:hover  {
  background-color: #f06752;
  color: #ffffff;
}
</style>
