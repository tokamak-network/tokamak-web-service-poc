<template>
  <div
    :class="{ 'disable': disable }"
    class="button"
    @click="click"
  >
    {{ label }}
  </div>
</template>

<script>

export default {
  props: {
    label: {
      type: String,
      default: '',
    },
    disable: {
      type: Boolean,
      default: false,
    },
    func: {
      type: Function,
      default: () => {},
    },
  },
  methods: {
    async click () {
      if (!this.disable) {
        await this.func();
      }
    },
  },
};
</script>

<style scoped>
.button {
  width: 100%;
  height: 100%;
}

.button:hover {
  cursor: pointer;
}

.disable:hover {
  cursor: not-allowed;
}
</style>
