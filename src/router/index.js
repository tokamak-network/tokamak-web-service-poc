import Vue from 'vue';
import Router from 'vue-router';
Vue.use(Router);

import HomeLayout from '@/layouts/HomeLayout';
import ConfigLayout from '@/layouts/ConfigLayout';
import RootchainLayout from '@/layouts/RootchainLayout';
import OperatorLayout from '@/layouts/OperatorLayout';
import UsernodeLayout from '@/layouts/UsernodeLayout';
import StakeLayout from '@/layouts/StakeLayout';
import VueRouter from 'vue-router';

const routes = [
  {
    path: '/home',
    component: HomeLayout,
  },
  {
    path: '/config',
    component: ConfigLayout,
  },
  {
    path: '/rootchain',
    component: RootchainLayout,
  },
  {
    path: '/operator',
    component: OperatorLayout,
  },
  {
    path: '/usernode',
    component: UsernodeLayout,
  },
  {
    path: '/stake',
    component: StakeLayout,
  },
];

const router = new VueRouter({
  mode: 'history',
  routes,
});

export default router;
