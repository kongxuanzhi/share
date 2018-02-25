// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'

Vue.config.productionTip = false
Vue.prototype.$ajax = axios


// must defined before new Vue()
Vue.directive('dragable', {
  inserted: function (el) {
    let oDiv = el;
    oDiv.onmousedown = function(ev){
      let disX = ev.clientX -oDiv.offsetLeft;
      let disY = ev.clientY - oDiv.offsetTop;
      
      document.onmousemove = function(ev){
        let l = ev.clientX-disX;
        let t = ev.clientY-disY;
        oDiv.style.left =  l+'px';
        oDiv.style.top = t+'px';
      };
      document.onmouseup = function(){
        document.onmousemove=null;
        document.onmouseup=null;
      };
    };
  }
});

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})