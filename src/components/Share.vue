<template>
  <div id="share">
    <div class="right">
      <div class="header">导航</div>
      <div class="body">内容</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Share',
  data () {
    return {
      ajaxInstance: null,
      shareId: 'shareId',
      shareName: 'shareName',
      shareNum: 212,
      sharePrice: 12.22,
      canUseMoney: 1,
      sharesNowPrice: [9.560, 59.900, 5.700],
      shares: [
        {
          id: 'dsfddf1',
          name: '合金投资',
          number: 100,
          buyPrice: 9.620,
          shareVal: 0.0,
          shareLoseGet: 0,
          shareLoseGetRate: 0
        },
        {
          id: 'dsfddf2',
          name: 'B',
          number: 100,
          buyPrice: 60.060,
          shareVal: 0.0,
          shareLoseGet: 0,
          shareLoseGetRate: 0
        },
        {
          id: 'dsfddf3',
          name: 'C',
          number: 100,
          buyPrice: 5.795,
          shareVal: 0.0,
          shareLoseGet: 0,
          shareLoseGetRate: 0
        }
      ]
    }
  },
  computed: {
    totalMoney: function () {
      return this.shareTotalVal + this.canUseMoney
    },
    shareTotalVal: function () {
      let totalVal = 0.0
      for (let i = 0;  i< this.shares.length; i++) {
        totalVal += this.shares[i].shareVal
      }
      return totalVal
    }
  },
  watch: {
    sharesNowPrice: {
      handler(sharesOldPrice, sharesNowPrice) {
      // console.log( this.sharesNowPrice[0])
        for (let i = 0;  i< sharesNowPrice.length; i++) {
          this.shares[i].shareVal = this.shares[i].number * sharesNowPrice[i]
          this.shares[i].shareLoseGetRate = (sharesNowPrice[i] - this.shares[i].buyPrice) / this.shares[i].buyPrice * 100
          this.shares[i].shareLoseGet =  (sharesNowPrice[i] - this.shares[i].buyPrice) * this.shares[i].number
        }
　　　},
      deep: true
　　}
  },
  mounted: function () {
    // window.hx_hq_canvas.initShow()
    // this.ajaxInstance = this.$ajax.create({
    //   baseURL: 'http://pdfm.eastmoney.com',
    //   timeout: 2000,
    //   headers: {
    //     'dataType': 'jsonp'
    //   }
    // });
    // setInterval(() => {
    //   // console.log(document.getElementById('hexm_curPrice'))
    //   //  this.ajaxInstance.get('/EM_UBG_PDTI_Fast/api/js?rtntype=5&cb=jQuery183024268883230430283_1509546539162&id=6034581&type=k&authorityType=&_=1509546612612')
    //   //  .then(function(response) {
    //     // console.log(response)
    //     // this.sharesNowPrice = [response.data, response.data, response.data]
    //   // });
    //   // this.sharesNowPrice = [Math.random()*10, 3, 4]
    // }, 2000);
    // console.log(document.getElementById('ifrm').contentWindow.document.getElementById('hexm_curPrice'))
      // var d = window.frames["ifrm"].document;
      // console.log(d)
    // window.onload = function () {
    // }
  },
  methods: {
    buyShare: function () {
      this.shares.append({
        id: this.id,
        name: this.shareName,
        number: this.shareNum,
        buyPrice: this.sharePrice,
        shareVal: 0.0,
        shareLoseGet: 0,
        shareLoseGetRate: 0
      })
    },
    saleShare: function (i) {
      this.canUseMoney += this.shares[i].shareVal
      this.shares.splice(i, 1)
      this.sharesNowPrice.splice(i, 1)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lan>
h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #323423;
}
</style>
