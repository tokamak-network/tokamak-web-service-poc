<template>
  <div class="menu-container">
    <div
      class="menu-title-container"
      :class="{ 'menu-selected': $route.path === '/home'}"
      @click="clickMenu('home')"
    >
    Home
    </div>
    <div
      class="menu-title-container"
      :class="{ 'menu-selected': $route.path === '/config'}"
      @click="clickMenu('config')"
    >
    Config
    </div>
    <div
      class="menu-title-container"
      :class="{ 'menu-selected': $route.path === '/rootchain'}"
      @click="clickMenu('rootchain')"
    >
    RootChain Setup
    </div>
    <div
      class="menu-title-container"
      :class="{ 'menu-selected': $route.path === '/operator'}"
      @click="clickMenu('operator')"
    >
    Operator Setup
    </div>
    <div
      class="menu-title-container"
      :class="{ 'menu-selected': $route.path === '/usernode'}"
      @click="clickMenu('usernode')"
    >
    Usernode Setup  
    </div>
    <div
      class="menu-title-container"
      :class="{ 'menu-selected': $route.path === '/stake'}"
      @click="clickMenu('stake')"
    >
    Stake/Unstake Tester
    </div>
  </div>
</template>

<script>
  export default {
    methods: {
      clickMenu (path) {
        if (`/${path}` === this.$route.path) {
          return ;
        }
        this.$router.push(`/${path}`).catch(err => {});
      },
    },
  };
</script>

<style scoped>
.menu-container {
  padding-top: 8px;
  padding-bottom: 24px;
  background: #ffffff;
  min-width: 210px;
  max-width: 210px;
  min-height: 340px;
  max-height: 340px;
  border-radius: 7px;
  border: solid 1px #ced6d9;
}

.menu-title-container {
  font-family: Roboto;
  margin-left: 1px;
  margin-right: 1px;
  margin-top: 16px;
  display: flex;
  align-items: center;
  padding: 10px;
  padding-left: 16px;
  text-decoration: none;
  padding-left: 8px;
  font-size: 16px;
  font-weight: 500;
  font-stretch: normal;
  font-style: normal;
  line-height: 1.67;
  letter-spacing: normal;
  text-align: left;
  color: #c4c4c4;
}

.menu-logout-container {
  font-family: Roboto;
  border-top: 0.7px solid rgb(238, 236, 236);
  margin-top: 16px;
  display: flex;
  align-items: center;
  font-size: 13px;
  color: #c4c4c4;
  padding: 14px;
  padding-left: 20px;
}

.menu-logout-container:hover {
  cursor: pointer;
  color: #3e3e3e;
}

.menu-image {
  -webkit-filter: grayscale(100%) brightness(110%) contrast(0.9);
  filter: grayscale(100%) brightness(110%) contrast(0.9);
  margin-left: 5px;
  margin-right: 10px;
}

.sub-menu-title-container {
  font-family: Roboto;
  margin-left: 1px;
  margin-right: 1px;
  padding: 10px;
  padding-left: 36px;
  text-decoration: none;
  font-size: 14px;
  font-stretch: normal;
  font-style: normal;
  letter-spacing: normal;
  text-align: left;
  color: #c4c4c4;
}

.menu-title-container:hover {
  cursor: pointer;
  color: #3e3e3e;
}

.sub-menu-title-container:hover {
  cursor: pointer;
}

.menu-title-container:hover .menu-image {
  -webkit-filter: invert(30%) grayscale(100%) brightness(70%) contrast(4);
  filter: invert(30%) grayscale(100%) brightness(70%) contrast(4);
}

.sub-menu-title:hover {
  color: #3e3e3e;
}

.menu-selected {
  background: #f7f8f9;
  color: #3e3e3e;
}

.menu-button-selected {
  -webkit-filter: invert(30%) grayscale(100%) brightness(70%) contrast(4);
  filter: invert(30%) grayscale(100%) brightness(70%) contrast(4);
}
</style>