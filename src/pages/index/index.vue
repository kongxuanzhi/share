<template>
  <div id="index">
    <div class="data-area">
      <span class="glyphicon glyphicon-plus add-setting" v-on:click="addDrag()" aria-hidden="true"></span>
      <span>共{{dragDivs.length}}个</span>
      <div class="set-dragable-params" v-if="dragDivs.length > 0">
        <span>当前选中第{{currentIndex + 1}}个</span>
        <div class="form-group">
          <label for="content">内容： </label>
          <input type="text" class="form-control setting-item" id="content" v-model="dragDivs[currentIndex].content" placeholder="内容">
        </div>
        <div class="form-group">
          <label for="fontSize">字体大小: </label>
          <input type="number" class="form-control setting-item" id="fontSize" v-model="dragDivs[currentIndex].fontSize" placeholder="字体大小">
        </div>
        <div class="form-group">
          <label for="fontColor">字体颜色: </label>
          <input type="text" class="form-control setting-item" id="fontColor" v-model="dragDivs[currentIndex].color" placeholder="字体颜色">
          <color-picker class="color-picker" v-model="dragDivs[currentIndex].color"></color-picker>
        </div>
        <div class="form-group">
          <label for="fontFamily">字体: </label>
            <select class="form-control setting-item" id="fontFamily" v-model="dragDivs[currentIndex].fontFamily">
            <option v-for="font in fonts" v-bind:value="font">{{font}}</option>  
          </select>  
        </div>
        <div class="form-group">
          <label for="letterSpacing">字体间距: </label>
          <input type="number" class="form-control setting-item" id="letterSpacing" v-model="dragDivs[currentIndex].letterSpacing" placeholder="字体间距">
        </div>
        <div class="btn btn-primary"  v-on:click="saveToLocal()">提交</div>
      </div>
      <hr>
      <div v-for="(ddg, index) in dragDivGroups" v-on:click="selectGroup(index)" v-dragable 
        style="position: absolute; border: 1px solid red;"
        :style="{top: ddg.top+'px',left: ddg.left+'px',right: ddg.right+'px',bottom: ddg.bottom+'px',
        width: ddg.width + 'px',
        height: ddg.height + 'px'
        }">
        <div style="position: relative">
          <div v-for="(item, key) in dragDivs" v-on:click="selectDrag(key)">
            <dragable-div v-if="item.group==index" v-on:delete="deleteDrag" :index="key" :drag-params="item"></dragable-div>
          </div>
        </div>
      </div>
      <span class="glyphicon glyphicon-plus add-setting" v-on:click="addGroup()" aria-hidden="true"></span>
      <div class="form-group">
        <label for="width">WIDTH: </label>
        <input type="number" class="form-control setting-item" id="width" v-model="dragDivGroups[currentGroup].width" placeholder="width">
      </div>
      <div class="form-group">
        <label for="height">HEIGHT: </label>
        <input type="number" class="form-control setting-item" id="height" v-model="dragDivGroups[currentGroup].height" placeholder="height">
      </div>
    </div>
    <!--<div class="new-area"></div>-->
    <div class="preview">
      <img src="../../assets/template/template3.jpg">
    </div>
  </div>
</template>

<script>
//1. 动态增加 dragable-div实例
//2. 预览部分，使用canvas绘制内容，然后保存
import Share from '../../components/Share'
import DragableDiv from '../../components/DragableDiv'
import colorPicker from '../../components/colorPicker.vue'

export default {
  data () {
    return {
      dragDivs: [ ],
      dragDivGroups: [
        {
          top: 0,
          left: 0,
          width: 200,
          height: 300
        }
      ],
      currentIndex: 0,
      currentGroup: 0,
      fonts: ["邯郸-郭灵霞灵芝体", "cursive", "Helvetica Neue", "Helvetica", "Arial", "sans-serif", "monospace", "fantasy", "serif"],
    }
  },
  mounted: function () {
    this.dragDivs = JSON.parse(localStorage.drags)
    // let interval = setInterval(()=> {
    //   var day = new Date()
    //   this.dragDivs[0].content =  day.getHours() + ':' + day.getMinutes() + ":" + day.getSeconds();
    // }, 1000);
  },
  methods: {
    selectDrag: function(index) {
      this.currentIndex = index
    },
    selectGroup: function(index) {
      this.currentGroup = index
    },
    addDrag: function() {
      this.dragDivs.push({
        group: this.currentGroup,
        content: '在这里自定义内容',
        color: '#333',
        fontSize: 18,
        fontFamily: '',
        letterSpacing: 1,
        top: 20,
        left: 30
      })
      this.currentIndex = this.dragDivs.length - 1
    },
    addGroup: function() {
      this.dragDivGroups.push({
        top: 20,
        left: 30,
        width: 400,
        height: 110
      })
      this.currentGroup = this.dragDivGroups.length - 1
    },
    deleteDrag: function(index, top, left) {
      // if (top < 100) {
      //   console.log(this.dragDivs.length)
      //   if (this.dragDivs.length == 1) {
      //     alert('不能删除最后一个元素')
      //     return
      //   }
      //   this.dragDivs.splice(index, 1)
      //   // console.log(this.dragDivs)
      //   // this.currentIndex = 0
      //   // debugger
      // }
    },
    saveToLocal: function() {
      localStorage.drags = JSON.stringify(this.dragDivs)
    }
  },
  components: {
      Share, DragableDiv, colorPicker
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">

#index {
  .data-area {
    float: left;
    width: 30%;
    border: 1px solid red;
    margin-left: 12px;
    padding: 16px;
    
    .add-setting {
      font-size: 34px;
      cursor: pointer;
      color: #3e79b6;

      &:hover {
        color: #21cc57;
        font-size: 40px;
      }
    }

    .set-dragable-params {
      .setting-item {
      }
      
      .color-picker {
        border: 1px solid #ccc;
        float: right;
        margin-top: -23px;
        margin-right: 12px;
      }
    }
  }

  .new-area {
    border: 1px solid red;
    height: 400px;
    width: 400px;
    float: left;
    margin-left: 20px;
  }
  
  .preview {
    float: right;
    margin-right: 160px;
    background-image: url('../../assets/phone.png');
    background-size: contain;
    background-repeat: no-repeat;
    width: 421px;
    height: 813px;

    img {
      width: 77%;
      margin-top: 115px;
      margin-left: 44px;
    }
  }
}

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

<!--<div class="header">
  <div class="status-bar">
  信号，运行商，网络，时间， 屏幕旋转，地理位置， 时钟，电池
  </div>
  <div class="document-title">返回图标， 中间title， 右边刷新</div>
</div>
<div class="body">tab， 高亮</div>
!-->