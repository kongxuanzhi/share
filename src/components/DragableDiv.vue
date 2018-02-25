<template>
  <span class="drag" v-drag :style="{
   color: dragParams.color,
   fontSize: dragParams.fontSize + 'px',
   fontFamily: dragParams.fontFamily,
   letterSpacing: dragParams.letterSpacing +　'px', 
   left: dragParams.left + 'px',
   top: dragParams.top + 'px'}">
  {{ dragParams.content }}
  </span>
</template>

<script>
// 1. 改变大小
// 2. 可以拖动
// 3. 内容居中
// 4. 背景可以设置
// 5. 字体颜色和大小可以设置

export default {
  props: {
    dragParams: {
      type: Object,
      default: {
        content: '0',
        color: '#333',
        fontSize: 18,
        fontFamily: 'cursive',
        letterSpacing: 1,
        top: 200,
        left: 200
      }
    },
    index: {
      type: Number,
      required: true
    }
    //,
    // content: [Number, String] //自定义变量绑定到组件的内容上
  },
  data () {
    return {
    }
  },
  methods: {
    
  },
  mounted: function() {
  },
  // watch: {
  //   content: function (val, oldVal) { //将变量的内容再绑定到this.dragParams.content上
  //     if (val != oldVal) {
  //       this.dragParams.content = val
  //     }
  //   }
  // },
  directives: {
    drag: {
      inserted: function (el, binding, vnode) {  // https://cn.vuejs.org/v2/guide/custom-directive.html
        el.onmousedown = function(ev) {
          let disX = ev.clientX -el.offsetLeft;
          let disY = ev.clientY - el.offsetTop;
          ev.stopPropagation();

          document.onmousemove = function(ev){
            let l = ev.clientX - disX;
            let t = ev.clientY - disY;
            el.style.left =  l + 'px';
            el.style.top = t + 'px';
            vnode.context.dragParams.top = t
            vnode.context.dragParams.left = l
          };
          document.onmouseup = function(){
            vnode.context.$emit('delete', vnode.context.index, vnode.context.dragParams.top, vnode.context.dragParams.left)
            document.onmousemove=null;
            document.onmouseup=null;
          };
        };
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.drag {
  display: inline-block;
  font-weight: bold;
  color: red;
  padding: .5rem;
  margin: 4px;
  cursor: move;
  position: absolute;
  top: 200px;
  left: 300px;
  z-index: 9999;
  word-wrap:break-word;
  white-space:normal;

  &:hover {
    background: #ccc;
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