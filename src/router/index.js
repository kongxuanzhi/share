import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import index from '@/pages/index/index'
import stars from '@/pages/stars/stars'
import Aims from '@/pages/Aims/Aims'
import Share from '@/components/Share'
import Flex from '@/components/Flex'
import fullpage from '@/components/fullpage'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: index
    },
    {
      path: '/share',
      name: 'Share',
      component: Share
    },
    {
      path: '/hello',
      name: 'Hello',
      component: HelloWorld
    },
    {
      path: '/flex',
      name: 'Flex',
      component: Flex
    },
    {
      path: '/aims',
      name: 'Aims',
      component: Aims
    },
    {
      path: '/stars',
      name: 'stars',
      component: stars
    },
    {
      path: '/fp',
      name: 'fullpage',
      component: fullpage
    }
  ]
})
