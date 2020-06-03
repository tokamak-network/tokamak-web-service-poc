<template>
  <div class="main-layout">
    <menu-container />
    <div class="main-container">
      <router-view />
      <home-container />
    </div>
  </div>
</template>

<script>
  // import { mapState } from 'vuex';
  import MenuContainer from '@/containers/MenuContainer.vue';
  import HomeContainer from '@/containers/HomeContainer.vue'

  export default {
    components: {
      'menu-container': MenuContainer,
      'home-container': HomeContainer,
    }
  };

</script>

<style scoped>
.main-layout {
  display: flex;
  min-width: 960px;
  max-width: 960px;
  padding-top: 16px;
  padding-bottom: 2rem;
}

.main-container {
  padding-left: 16px;
  width: 100%;
  position: relative;
}
</style>
