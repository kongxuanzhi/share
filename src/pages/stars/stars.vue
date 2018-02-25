<template>
  <div id="stars">
    <h1>偶像的清晰的图片展示</h1>
    林俊杰，周杰伦，科比，欧文
    https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/drawImage
    http://bucephalus.org/text/CanvasHandbook/CanvasHandbook.html#transform-a-b-c-d-e-f
    https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API
    https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/clearRect
    https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement
    <poster v-for="poster in posters" :key="poster.name" :poster="poster"></poster>
  </div>
</template>

<script>
import Poster from '../../components/Poster'

export default {
    data () {
        return {
            posters: []
        }
    },
    mounted() {
        this.posters.push({
            offsetX: 300,
            offsetY: 300,
            width: 400,
            angle: 6,
            imgPath: './static/img/stars/irving.jpeg',
            name: 'irving'
        })
    },
    components: {
        Poster
    }
}
</script>

<style lang="less" scoped>
#stars {
  width: 1000px;
  height: 800px;
}
</style>