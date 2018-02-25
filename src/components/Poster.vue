<template>
    <div class="poster" :style="{}">
        <canvas id="canvas" style="outline: 1px solid green"></canvas>
    </div>
</template>
<script>
export default {
    props: {
        poster: {
            required: true, 
            type: Object,
            default: { 
                offsetX: 0,
                offsetY: 0,
                width: 0,
                angle: 0,
                imgPath: null,
                name: ''
            }
        },
    },
    data () {
        return {
            canvas: null,
            ctx: null
        }
    }, 
    mounted() {
        this.canvas = document.getElementById('canvas')
        this.ctx = this.canvas.getContext('2d')
        this.canvas.width = document.body.clientWidth;
        this.canvas.height = document.body.clientHeight;

        const vm = this
        const poster = this.poster
        var image = new Image();
        image.src = poster.imgPath;
        image.onload = () => {
            let width = image.naturalWidth;
            let height = image.naturalHeight;
            let rate = height / width;
            let poserH = poster.width * rate;
            vm.ctx.translate(poster.offsetX, poster.offsetY); 
            vm.ctx.fillStyle="red";
            // setInterval(()=>{
            //     vm.ctx.clearRect(-poster.width/2, - poserH/2, poster.width, poserH);
            //     vm.ctx.rotate (poster.angle * Math.PI / 180);
            vm.ctx.drawImage(image, - poster.width/2, - poserH/2, poster.width, poserH);
            // }, 100)
        };
    },
    method: {
    }
}

/*
tbd:
1. 图片等比缩放
2. 图片旋转
3. 圆形裁切
4. 上传 -> 预览 -> 拖动 //基础
5. 给图片加特效
6. 平移侧切，给定中转轴，让图片有3D效果
*/
</script>

<style lang="less" scoped>
#poster {
  width: 100%;
  height: 800px;
  outline: 1px solid red;
}
 // vm.ctx.clearRect(0,0,  ,canvas.height);
</style>