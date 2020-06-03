<template>
  <div id="app">
    <header-container />
    <div class="body-container">
      <!-- <div v-if="!signIn">
        <loading-spinner v-if="loading" />
        <access-wallet-layout v-else />
      </div> -->
      <div>
        <!-- <tx-processor /> -->
        <main-layout />
      </div>
    </div>
    <footer-container />
  </div>
</template>

<script>
import { mapState, mapGetters } from 'vuex';

import LoadingSpinner from '@/components/LoadingSpinner.vue';
import TxProcessor from '@/components/TxProcessor.vue';
import HeaderContainer from '@/containers/HeaderContainer.vue';
import FooterContainer from '@/containers/FooterContainer.vue';
import AccessWalletLayout from '@/layouts/AccessWalletLayout.vue';
import MainLayout from '@/layouts/MainLayout.vue';
import AccessWalletLayoutVue from '@/layouts/AccessWalletLayout.vue';
// import NetworkGuideLayout from '@/layouts/NetworkGuideLayout.vue';

export default {
  components: {
    'loading-spinner': LoadingSpinner,
    'header-container': HeaderContainer,
    'footer-container': FooterContainer,
    'access-wallet-layout': AccessWalletLayout,
    'main-layout': MainLayout,
    'tx-processor': TxProcessor,
  },
  data () {
    return {
      message: '',
    };
  },
  computed: {
    ...mapState([
      'loading',
      'signIn',
    ]),
    ...mapGetters([
      'initialState',
    ]),
  },
  created () {
    if (this.initialState && this.$route.path !== '/') {
      this.$router.replace({
        path: '/',
        query: { network: this.$route.query.network },
      }).catch(err => {});
    }
    this.$store.watch(
      (_, getters) => getters.initialState,
      (logout) => {
        if (logout && this.$route.path !== '/') {
          this.$router.replace({
            path: '/',
            query: { network: this.$route.query.network },
          }).catch(err => {});
        }
      },
    );
  },
};
</script>
