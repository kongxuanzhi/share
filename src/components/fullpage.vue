<template>
  <div class="fullpage">
    <div id="dowebok" v-on:click="a=!a">
      <div class="section">
        <!--<div class="slide" v-if="type=='word'" v-for="(item, key) in currentArea">
          <span>{{item.idea}}</span>
          <label :style="{color: getRandColor()}">
            {{key}}  {{item.en}}  {{item.zh}}
          </label>
        </div> -->
        <div class="slide" style="font-size: 25px;  " v-if="type=='word'">
          <div style="text-align: left;" v-for="(item, key) in currentArea">
              {{key}}. {{item.en}}  {{item.zh}}
          </div>
        </div>
        <div class="slide" v-if="type=='pic'" v-for="(item, key) in currentArea">
          <img :src="item">
        </div>
      </div>
    </div>
    <div class="pagination">
      <span class="previous" v-on:click="previous">previous</span>
      <span class="next" v-on:click="next">next</span>
    </div>
  </div>
</template>

<script>

export default {
  data () {
    return {
        query: this.$route.query,
        type: 'word',
        a: false,
        offset: 0,
        length: 56,
        contents: [],
        currentArea: [],
        ideas: [
            '尼克杨', '木棍', '鸭子', '耳朵', '红旗', '我', '视频666', '镰刀', '盘山公路', '酒', '国庆节', '光棍节', '腊月',
            '哈登', '情人节', '食物', '石榴', '石器', '少女', '19大', '耳屎', '二姨', '两只小鸭子', '乔丹', '科比',
            '西蒙斯', '初中排名', '2把镰刀', '二爸', '二舅', '月末吃土', '三姨', '格里芬', '失恋33天', '字母哥，奥尼尔', '杜兰特', '360度完美', '三妻四妾', '妇女',
            'zolu大招', '中年人', '司仪', '王宝强', '廉颇', '东北人大鹏', '抗日战争胜利', '重庆和谈', '死妻', '死爸', '建国', '中世纪', '武艺李小龙', '吾儿',
            '下雨无伞', '54运动', '端午节'
        ]
    }
  },
  mounted: function() {
    let vm = this
    vm.offset = +(localStorage.getItem('wordIndex') || 1);
    if (vm.query.type === 'pic') {
        vm.type = 'pic';
        vm.$ajax.get('static/pic.json').then(function(response) {
            vm.contents = response.data;
            vm.currentArea = vm.getArea(vm.offset, vm.length);
            vm.initFullpage(vm)
        })
    } else {
        vm.type = 'word';
        vm.$ajax.get('static/words.json').then(function(response) {
            vm.contents = response.data;
            vm.currentArea = vm.getArea(vm.offset, vm.length);
            vm.initFullpage(vm)
        })
    }
  },
  methods: {
    initFullpage(vm) {
        $(function(){
            $('#dowebok').fullpage({
                verticalCentered: true,
                continuousHorizontal: true,
                keyboardScrolling: true,
                touchSensitivity: 3,
                css3: true,
                slidesNavigation: false,
                scrollingSpeed: 1000,
                resize: true,
                slidesNavPosition: 'top',
                loopHorizontal: true,
                autoScrolling: false,
                scrollOverflow: false,
                fitToSection: false,
                afterRender: function () {
                    let i = 0
                    setInterval(function() {
                        if (!vm.a) {
                            $.fn.fullpage.moveTo(1, (i++) % vm.length);
                        }
                    }, 5000);
                }
            });
        });
    },
    getRandColor() {
        return '#def5cd';
        // return '#' + (~~(Math.random() * Math.pow(2, 21)) + Math.pow(2, 10)).toString(16)
    },
    previous() {
        this.offset -= this.length;
        this.offset = this.offset < 0 ? 0 : this.offset;
        localStorage.setItem('wordIndex', this.offset);
        this.currentArea = this.getArea(this.offset, this.length);
    },
    next() {
        this.offset += this.length;
        this.offset = this.offset > this.words - this.length ? this.words - this.length : this.offset;
        localStorage.setItem('wordIndex', this.offset);
        this.currentArea = this.getArea(this.offset, this.length);
    },
    getArea (offset, length) {
        return this.contents.slice(offset, offset + length).map((word, index) => {
            if (this.type === 'word' && index < this.ideas.length) {
                word['idea'] = this.ideas[index]
            }
            return word;
        })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="less">

#dowebok {
  outline: 1px solid red;
  height: auto !important;
  
  .section {
    text-align: center;
  
    .slide {
      font-size: 3rem;
      background-color: #6c7d5a;
      color: #ffcebb;

      label {
        display: block;
        transform: rotateZ(00deg);
      }

      img {
        width: 100%;
      }
    }
  }
}

.pagination {
  position: fixed;
  bottom: 20px;
  right: 20px;
  z-index: 1000;
  height: 50px;
  width: 400px;

  span {
    display: inline-block;
    width: 100px;
    height: 100%;
    color: white;
    line-height: 50px;
    text-align: center;
    cursor: pointer;
  }

  .previous {
    background: green;
    float: left;
  }
  
  .next {
    background: #c5203d;
    float: right;
  }
}
</style>
