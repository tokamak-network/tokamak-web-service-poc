<template>
  <div class="stake-op">
    <div class="operator-info-container">
      <div class="operator-info-general-container">
        <div class="operator-info-general">
          <div class="operator-info-title">Operator address</div>
        </div>
        <div class="chain-info-general">
          <div class="chain-info-title">Rootchain</div>
          <div class="chain-info-title">Chain ID</div>
        </div>
      </div>
      <div class="operator-info-assets-container">
        <div class="operator-assets-general">Assets</div>
        <div class="operator-assets-header">
          <div class="operator-header">Asset</div>
          <div class="operator-header">Amount</div>
          <div class="operator-header">Charge</div>
        </div>
        <div class="operator-assets-content">
          <div class="operator-content">PETH</div>
          <div class="operator-content">0.10ETH</div>
          <button class="operator-content">GET ETH</button>
        </div>

        <div class="operator-assets-content">
          <div class="operator-content">PETH</div>
          <div class="operator-content">0.10ETH</div>
          <button class="operator-content">GET ETH</button>
        </div>
      </div>
    </div>
    <div class="operator-stake-container">
      <div class="operator-info-general-container">
        <div class="operator-details">
          <div class="operator-details-list"></div>
          <button class="button-submit">commit</button>
        </div>
      </div>
      <div class="staking-container">
        <div class="operator-info-assets-container" style="margin-bottom:8px">
          <div class="row-reverse">
            <base-tab
              :left-label="'Stake'"
              :right-label="'Unstake'"
              :tab="tab"
              @tab-changed="changeTab"
            />
          </div>
          <form v-if="tab === 'left'">
            <div class="ton-input">
              <div class="label-container">
                <div class="amount">Amount</div>
              </div>
              <div class="input-container">
                <input />
              </div>
              <div class="label-container"><span class="unit">MTON</span></div>
            </div>
            <div class="row">
              <div class="available-amount-label">Available Amount</div>
              <div class="available-amount">0.01MTON</div>
            </div>
            <button type="button" class="button-submit">Stake</button>
          </form>
          <form v-else>
            <div class="ton-input">
              <div class="label-container">
                <span class="amount">Amount</span>
              </div>
              <div class="input-container">
                <input />
              </div>
              <div class="label-container"><span class="unit">MTON</span></div>
            </div>
            <div class="row">
              <div class="available-amount-label">Available Amount</div>
              <div class="available-amount">0.01MTON</div>
            </div>
            <button type="button" class="button-submit">Stake</button>
            <div class="row">
              <div class="available-amount-label">Not Withdrawable</div>
              <div class="available-amount">0.01MTON</div>
            </div>
            <div class="row">
              <div class="available-amount-label">Withdrawable</div>
              <div class="available-amount">0.01MTON</div>
            </div>
            <div class="row" style="justify-content: center;">
              <button type="button" class="button-submit">Withdrawal</button>
              <button type="button" class="button-submit">Retake</button>
            </div>
          </form>
        </div>

        <div class="operator-info-assets-container">
          <div class="operator-assets-general">Commission Rate</div>
          <div class="ton-input">
            <div class="label-container">
              <div class="amount">Rate</div>
            </div>
            <div class="input-container">
              <input />
            </div>
            <div class="label-container"><span class="unit">%</span></div>
          </div>
          <form>
            <div class="row">
              <div class="available-amount-label">Current Commission</div>
              <div class="available-amount">0.01MTON</div>
            </div>
            <button type="button" class="button-submit">
              Fix Commission
            </button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import BaseTab from "@/components/BaseTab.vue";
export default {
  components: {
    "base-tab": BaseTab
  },
  data() {
    return {
      tab: "left"
    };
  },
  methods: {
    changeTab(tab) {
      this.tab = tab;
    }
  }
};
</script>

<style scoped>
.stake-op {
  display: flex;
  flex-direction: column;
  font-family: Roboto;
  font-size: 9px;
  justify-content: center;
  text-align: center;
  color: #7e8d93;
  min-width: 860px;
  max-width: 860px;
}

.operator-info-container {
  width: 100%;
  display: flex;
  padding-bottom: 16px;
  margin-bottom: 5px;
}
.operator-info-general-container {
  width: 70%;
  margin-right: 4px;
  flex: 1;
  height: auto;
}

.operator-info-general:first-child {
  margin-bottom: 8px;
}
.operator-info-general:last-child {
  margin-top: 8px;
}
.operator-info-assets-container {
  padding-bottom: 5px;
  margin-left: 4px;
  display: flex;
  flex-direction: column;
  flex: 1;
  border-radius: 6px;
  border: solid 1px #ced6d9;
  background-color: #ffffff;
}
.operator-info-general {
  border: solid 1px #ced6d9;
  height: 74px;
  display: flex;
  align-items: center;
  border-radius: 6px;
  justify-content: center;
  text-align: center;
  color: #7e8d93;
  background-color: #ffffff;
}
.chain-info-general {
  display: flex;
  flex-direction: row;
  border-radius: 6px;
  color: #7e8d93;
  background-color: #ffffff;
}
.chain-info-title {
  border: solid 1px #ced6d9;
  width: 100%;
  height: 74px;
  display: flex;
  align-items: center;
  border-radius: 6px;
  justify-content: center;
  text-align: center;
  font-size: 11px;
}
.chain-info-title:first-child {
  margin-right: 4px;
}
.chain-info-title:last-child {
  margin-left: 4px;
}
.operator-info-title {
  display: flex;
  flex-direction: row;
  font-family: Roboto;
  color: #586064;
  font-size: 16px;
}

.operator-assets-general {
  display: flex;
  padding: 5px;
  align-items: center;
  padding-left: 16.9px;
  font-size: 16px;
}
.operator-assets-header {
  padding-top: 10px;
  padding-bottom: 10px;
  display: flex;
  width: 100%;
  border-top: 1px solid #ddd;
  border-bottom: 1px solid #ddd;
}
.operator-assets-content {
  display: flex;
  width: 100%;
  height: 100%;
  align-items: center;
}
.operator-header {
  font-family: Roboto;
  margin-top: 4px;
  margin-bottom: 4px;
  width: 100%;
  text-align: center;
  color: #586064;
  font-size: 11px;
}
.operator-content {
  margin-top: 4px;
  margin-bottom: 2px;
  width: 50%;
  text-align: center;
  font-size: 12px;
  font-family: Roboto;
  letter-spacing: 0.27px;
  color: #586064;
}
.operator-stake-container {
  width: 100%;
  flex-direction: row;
  display: flex;
  padding-bottom: 16px;
}
.operator-details {
  height: auto%;
}
.staking-container {
  margin-left: 8px;
  width: 40%;
  display: flex;
  flex-direction: column;
}
.row-reverse {
  display: flex;
  flex-direction: row-reverse;
  margin-right: 8px;
}
.ton-input {
  display: flex;
  width: 100%;
  justify-content: space-around;
  align-items: center;
  border-top: 1px solid #ced6d9;
  border-bottom: 1px solid #ced6d9;
  padding-top: 0.6px;
  padding-bottom: 0.6px;
  height: 26px;
}
.label-container {
  display: flex;
  justify-content: center;
  align-items: center;
}
.input-container {
  flex: 1;
  display: table;
  height: 100%;
}
input {
  display: table-cell;
  width: 100%;
  height: 100%;
  font-size: 14px;
  text-align: right;
  border: none;
  border-left: solid 1px #ced6d9;
  border-right: solid 1px #ced6d9;
  padding-right: 6px;
}
.row {
  display: flex;
  flex-direction: row;
  margin-top: 8px;
  padding: 10px 10px 0px 10px;
}
.available-amount-label {
  display: flex;
  font-family: Roboto;
  font-size: 10px;
  font-stretch: normal;
  font-style: normal;
  letter-spacing: normal;
  color: #161819;
  flex: 1;

  font-weight: 400;
}
.operator-details-list {
  height: 250px;
  border: solid 1px #ced6d9;
  border-radius: 6px;
  margin-bottom: 5px;
}
.button-submit {
  padding: 5px 10px;
  background: #2868af;
  color: #ffffff; 
}
</style>
