<template>
  <div class="header-container">
    <div class="header">
      <div class="header-title">
        <nav class="navbar navbar-dark sticky-top bg-dark flex-md-nowrap p-0">
        <a class="navbar-brand col-sm-3 col-md-2 mr-0" href="#">Tokamak Web Service(Beta)</a>
      </nav>
      </div>      
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex';

export default {
  // computed: {
  //   ...mapState([
  //     'signIn',
  //   ]),
  // },
  // methods: {
  //   toMainPage () {
  //     if (this.signIn && this.$route.path !== '/dashboard') {
  //       this.$router.push('/dashboard').catch(err => {});
  //     } else if(!this.signIn && this.$route.path !== '/') {
  //       this.$router.replace('/').catch(err => {});
  //     }
  //   },
  // },
};
</script>

<style scoped>
.header-container {
  width: 100%;
  height: 60px;
  background: #ffffff;
  display: flex;
  justify-content: center;
}

.header {
  width: 960px;
  height: 100%;
  align-items: center;
  display: flex;
}

.header-logo-container {
  flex: 1;
}

.header-logo {
  margin-top: 7px;
  padding-left: 16px;
}

.header-logo:hover {
  cursor: pointer;
}

.header-link-container {
  width: 160px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.header-link:hover {
  color: #141414b0;
}

.header-link {
  text-decoration: none;
  font-size: 14px;
  font-weight: normal;
  font-stretch: normal;
  font-style: normal;
  letter-spacing: normal;
  text-align: left;
  color: #7e8d93;
}
</style>
