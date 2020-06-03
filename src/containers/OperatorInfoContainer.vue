<template>
  <div class="operator-info-container">
    <div class="row name-container">
      <avatar class="avatar" fullname="O P R" :image="filteredImgURL(operator.avatar)" :size="50" :color="operator.color" />
      <div class="name">{{ operator.name }}</div>
      <div class="space" style="flex: 1;" />
      <div v-if="user === operator.address" class="button"><base-button :label="'edit'" :func="edit" /></div>
    </div>
    <text-viewer-link :title="'Website'"
                      :content="operator.website"
                      :with-divider="true"
                      :tooltip="'Website of the operator who runs the staking'"
                      :tooltipWidth="'240px'"
                      :tooltipMarginTop="'-6px'"
    />
    <text-viewer :title="'Description'"
                 :content="operator.description"
                 :with-divider="false"
                 :tooltip="'Introduction to the operator'"
                 :tooltipWidth="'180px'"
                 :tooltipMarginTop="'-9px'"
    />
    <text-viewer-downloader :title="'Genesis'"
                            :content="'Download'"
                            :href="exported(operator.genesis)"
                            :download="'genesis.json'"
                            :tooltip="'Information on Genesis Block of Operator’s Plasma Chain'"
                            :tooltipWidth="'280px'"
                            :tooltipMarginTop="'-6px'"
    />
    <text-viewer-link :type="'address'"
                      :title="'Operator Address'"
                      :content="operator.address"
                      :with-divider="false"
                      :tooltip="'Account address of the operator'"
                      :tooltipMarginTop="'-6px'"
    />
    <text-viewer-link :type="'address'"
                      :title="'Operator Contract'"
                      :content="operator.rootchain"
                      :with-divider="false"
                      :tooltip="'Smart Contract Address to manage the staking'"
                      :tooltipWidth="'260px'"
                      :tooltipMarginTop="'-6px'"
    />
    <text-viewer :title="'Chain ID'"
                 :content="operator.chainId"
                 :with-divider="false"
                 :tooltip="'Blockchain ID'"
                 :tooltipWidth="'160px'"
                 :tooltipMarginTop="'-9px'"
    />
    <text-viewer :title="'Commit Count'"
                 :content="operator.finalizeCount"
                 :with-divider="false"
                 :tooltip="'Number of a commit. Once the commit is made, the staking rewards and PowerTON Prize will be offered.'"
                 :tooltipWidth="'280px'"
                 :tooltipMarginTop="'-16px'"
    />
    <text-viewer :title="'Recent Commit'"
                 :content="fromNow(operator.lastFinalizedAt)"
                 :with-divider="false"
                 :tooltip="'This Operator\'s most recent commitment'"
                 :tooltipMarginTop="'-9px'"
    />
    <text-viewer :title="'Running Time'"
                 :content="fromNow(operator.deployedAt, true)"
                 :with-divider="false"
                 :tooltip="'Time in operation since the operator created the network'"
    />
    <text-viewer :title="'Commission Rate'"
                 :content="`${operator.isCommissionRateNegative ? '-' : ''}${rateOf(operator.commissionRate)}`"
                 :with-divider="false"
                 :tooltip="'The commission rate of this operator. It has a value between -100% and 100%.\n(1) + : The operator takes the profit from the delegator.\n(2) - : It distributes the operator\'s profits to the delegator.\n(3) 0 : It doesn’t divide the profit between the operator and the delegator.'"
                 :tooltipWidth="'300px'"
                 :tooltipMarginTop="'-41px'"
    />
    <text-viewer :title="'Reward'"
                 :content="currencyAmount(operator.userReward)"
                 :with-divider="false"
                 :tooltip="'Staking rewards from this Operator'"
                 :tooltipMarginTop="'-9px'"
    />
    <text-viewer :title="'Total Staked'"
                 :content="currencyAmount(operator.totalStaked)"
                 :with-divider="false"
                 :tooltip="'The amount of all MTONs currently staked on this operator. It contains the staking rewards that have been created so far.'"
                 :tooltipWidth="'300px'"
                 :tooltipMarginTop="'-17px'"
    />
    <text-viewer :title="'My Staked'"
                 :content="currencyAmount(operator.userStaked)"
                 :with-divider="false"
                 :tooltip="'The amount of all my MTONs currently staked on this operator. It includes the staking reward that I have received so far.'"
                 :tooltipWidth="'300px'"
                 :tooltipMarginTop="'-17px'"
    />
    <text-viewer :title="'Not Withdrawable'"
                 :content="currencyAmount(operator.userNotWithdrawable)"
                 :with-divider="false"
                 :tooltip="'Sum of your undelegate-stake reqeust amount. Each request does not withdrawable yet until 93046 blocks(14 days) passes from your request.'"
                 :tooltipWidth="'220px'"
                 :tooltipMarginTop="'-33px'"
    />
    <text-viewer :title="'Withdrawable'"
                 :content="currencyAmount(operator.userWithdrawable)"
                 :with-divider="false"
                 :tooltip="'Sum of all amount of undelegate-stake request which all passes 93046 blocks(14 days).'"
                 :tooltipWidth="'220px'"
    />
  </div>
</template>

<script>
import { getConfig } from '../../config.js';
import moment from 'moment';
import { createCurrency } from '@makerdao/currency';
const _TON = createCurrency('TON');

import { mapState } from 'vuex';
import Avatar from 'vue-avatar-component';
import TextViewer from '@/components/TextViewer.vue';
import TextViewerLink from '@/components/TextViewerLink.vue';
import TextViewerDownloader from '@/components/TextViewerDownloader.vue';
import BaseButton from '@/components/BaseButton.vue';

export default {
  components: {
    'avatar': Avatar,
    'text-viewer': TextViewer,
    'text-viewer-link': TextViewerLink,
    'text-viewer-downloader': TextViewerDownloader,
    'base-button': BaseButton,
  },
  props: {
    operator: {
      required: true,
      type: Object,
    },
  },
  computed: {
    ...mapState([
      'user',
    ]),
    filteredImgURL () {
      return name => name !== '' ? `${getConfig().baseURL}/avatars/${name}` : '';
    },
    currencyAmount () {
      return amount => this.$options.filters.currencyAmount(amount);
    },
    fromNow () {
      return (timestamp, suffix = false) => this.$options.filters.fromNow(timestamp, suffix);
    },
    rateOf () {
      return commissionRate => this.$options.filters.rateOf(commissionRate);
    },
    exported () {
      return genesis => 'data:text/json;charset=utf-8,' + encodeURIComponent(JSON.stringify(genesis, undefined, 2));
    },
  },
  methods: {
    edit () {
      const path = this.$route.path;
      this.$router.push({
        path: `${path}/edit`,
        query: { network: this.$route.query.network },
      }).catch(err => {});
    },
  },
};
</script>

<style scoped>
.operator-info-container {
  display: flex;
  flex-direction: column;
  border-radius: 6px;
  border: solid 1px #ced6d9;
  background-color: #ffffff;
}

.name-container {
  padding-top: 12px;
  padding-bottom: 12px;
  margin-left: 16px;
}

.row {
  display: flex;
  flex-direction: row;
  align-items: center;
}

.name {
  width: 200px;
  padding-left: 16px;
  padding-right: 8px;
  font-family: Roboto;
  font-size: 16px;
  font-weight: bold;
  font-stretch: normal;
  font-style: normal;
  letter-spacing: normal;
  color: #161819;
  word-break: break-all;
}

.button {
  color: #ffffff;
  background-color: #35496b;
  border: 1px solid #35496b;
  text-align: center;
  font-size: 14px;
  border-radius: 4px;
  height: 22px;
  width: 40px;
  margin-right: 16px;
}
</style>
