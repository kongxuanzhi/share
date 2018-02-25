# pw

> 个人静态网页网站
  docker run -it --rm --name app-tom-ssh -p 8880:8080 -v F:\workspace\app-scrm\App\app-frontend\:/srv1/app -w /srv1/app app_app-frontend bash
docker exec -it app-tom-ssh bash
## Build Setup

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report

# run e2e tests
npm run e2e

# run all tests
npm test
```

For detailed explanation on how things work, checkout the [guide](http://vuejs-templates.github.io/webpack/) and [docs for vue-loader](http://vuejs.github.io/vue-loader).
-------

# 配置docker

1. 在您的 Node.js 应用项目中创建一个 Dockerfile
```
FROM daocloud.io/node:0.10-onbuild
# replace this with your application's default port
EXPOSE 8888
然后您可以构建并且运行该 Docker 镜像
```

2. 构建并且运行该 Docker 镜像
```
docker build -t my-nodejs-app .
docker run -it --rm --name my-running-app my-nodejs-app
```

> 注意
在该镜像中假定您的应用中有一个名为 package.json 的文件，其中列出了项目依赖以及定义了入口脚本

* 运行单个 Node.js 脚本
    对于许多简单的单一文件项目，你会发现写一个完整的 Dockerfile 是不合适的。 所以，您可以直接通过使用 Node.js 镜像来运行一个 Node.js 脚本。  
    ```
    docker run -it --rm --name my-running-script -v "$PWD":/usr/src/myapp -w /usr/src/myapp 
    daocloud.io/node:0.10 node your-daemon-or-script.js
    ```

<!--http://blog.csdn.net/huludan/article/details/52641090-->
# 宿主机和docker容器之间互相拷贝文件
1. 宿主机拷贝到容器
    * 把一个宿主机上的目录挂载到镜像里：
        ```
        docker run -it -v /home/dock/Downloads:/usr/Downloads ubuntu64 /bin/bash
        ```
        通过-v参数，冒号前为宿主机目录，必须为绝对路径，冒号后为镜像内挂载的路径。
        现在镜像内就可以共享宿主机里的文件了。
        默认挂载的路径权限为读写。如果指定为只读可以用：ro
        docker run -it -v /home/dock/Downloads:/usr/Downloads:ro ubuntu64 /bin/bash
    *  高级的用法: 数据卷 tbd

2. 从容器拷贝数据到主机上
    docker cp <containerId>:/file/path/within/container /host/path/target  
    
<!--http://blog.csdn.net/permike/article/details/51879578-->
# docker 常用命令

<!--https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/-->
# Install MongoDB Community Edition on Ubuntu

# 使用DOCKER FILE构建镜像
  原理是，在当前容器run一条命令，保存，生成新的容器，删除旧的容器， 最后保存到镜像中，省去了不断commit提交change的步骤
# Obstacles:

1. Error response from daemon: conflict: unable to delete d8638d086558 (cannot be forced) - image has d
    http://blog.csdn.net/xjj1314/article/details/73550388

2. Eslint: no-duplicates Resolve error: unable to load resolver “node”
    https://stackoverflow.com/questions/44865507/eslint-no-duplicates-resolve-error-unable-to-load-resolver-node

<!--npm install -g cnpm --registry=https://registry.npm.taobao.org-->

[## nvm](https://github.com/creationix/nvm/blob/master/README.md#install-script)
[## node repertory](https://nodejs.org/dist/)
[## npm set china source](https://cnodejs.org/topic/4f9904f9407edba21468f31e)
[## webpack-0](http://www.cnblogs.com/tugenhua0707/p/4793265.html)
[## webpack-1](http://webpack.github.io/docs/webpack-dev-server.html)
[## webpack-2](http://www.jianshu.com/p/42e11515c10f)
[## webpack-3](http://vuejs-templates.github.io/webpack/)
[## docker容器端口映射解析](http://www.cnblogs.com/isenhome/p/5133663.html)

chmod -R 777 node_modules/
nvm-node-cli-cnpm
docker run -it --privileged=true -p 8888:8080 -v F:\workspace\workspace:/home/workspace acaefcb06d8e /bin/bash   
OPTIONS: 
--rm=true 运行完会删除容器
-d deamon 后台运行
touch containid 连接上后台运行的容器

docker exec -it 986d8311d80f /bin/bash

---
Q: 容器内npm install 总是不能在共享文件夹中创建软链
A： 修改windows 共享文件夹的权限为faiyer

----
Q： [## npm 太慢，cnpm不靠谱](https://cnodejs.org/topic/4f9904f9407edba21468f31e)
A： 更改镜像源 ~/.npmrc文件
registry = https://registry.npm.taobao.org

----
[## 容器内修改能自动加载，容器外修改不能自动加载](https://github.com/vuejs-templates/webpack/pull/641)
npm run dev
修改容器内的中间件：
const devMiddleware = require('webpack-dev-middleware')(compiler, {
  publicPath: webpackConfig.output.publicPath,
  quiet: true,
+  watchOptions: {
+    aggregateTimeout: 300,
+    poll: true
+  }
})

-----
root@986d8311d80f:/home/workspace/share# npm run dev
path.js:1182
          cwd = process.cwd();
Error: ENOENT: no such file or directory, uv_cwd
```
$ cd $PWD;
```
https://stackoverflow.com/questions/19936850/nodejs-error-node-js810-var-cwd-process-cwd



2017-10-30 20:12:29：
[node] http://vuejs-templates.github.io/webpack/
http://vuejs-templates.github.io/webpack/pre-processors.html

npm install sass-loader node-sass --save-dev
<style lang="scss">
/* write SASS! */
</style>
依赖：
apt-get install python make g++
要编译源码，太久了

vue api: 
教程： https://cn.vuejs.org/v2/guide/computed.html
语法： https://cn.vuejs.org/v2/api/#mounted


总结常见的ES6新语法特性 http://www.cnblogs.com/jarson-7426/p/5481491.html

setTimeout与setTimeinterval的使用 http://www.cnblogs.com/yony/archive/2012/06/21/2557766.html

vue 实战问题－watch 数组或者对象 http://www.cnblogs.com/hity-tt/p/6677753.html

概述VUE2.0不可忽视的很多变化 https://www.52jbj.com/jbdq/525022.html

[如何引用静态资源文件 js， css]：
用vue-cli的话一般会有个静态资源文件夹目录吧，这里面的文件不会被打包可以在html中随意引用，把js或css放在这个文件夹下，就可以像src属性一样的引用了


[jquery cdn]
https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js

[Timestamp]
http://tool.chinaz.com/Tools/unixtime.aspx


requirejs中define和require的定位以及使用区别？
https://www.zhihu.com/question/21260764


[axio 精华]
https://github.com/axios/axios
http://blog.csdn.net/qq_26744901/article/details/69572204
http://www.cnblogs.com/sxz2008/p/6834560.html


//股票地址
http://q.10jqka.com.cn/
http://stockpage.10jqka.com.cn/603458/
http://quote.eastmoney.com/sh603458.html?StockCode=603458

拖动元素到指定位置定义颜色选择器皿

sass语法
http://www.w3cplus.com/sassguide/syntax.html

vue自定义指令
https://cn.vuejs.org/v2/guide/custom-directive.html 

全局自定义拖动组件
http://blog.csdn.net/h1069495874/article/details/55504789

JQuery鼠标移动事件
http://www.w3school.com.cn/jquery/event_mousemove.asp

color-picker
https://zhuanlan.zhihu.com/p/25748496
http://vue-color-picker.rxshc.com/

Vue-Awesome
Font Awesome component for Vue.js, using inline SVG.
https://justineo.github.io/vue-awesome/demo/

vue 下拉框
http://blog.csdn.net/u013910340/article/details/71601554?ABstrategy=codes_snippets_optimize_v3

字体库下载
https://www.youziku.com/onlinefont/index/0%23%E8%AF%AD%E7%B3%BB%23%E4%B8%AD%E6%96%87%23%E4%BD%BF%E7%94%A8%E6%9C%80%E5%A4%9A%231
css导入字体
http://blog.csdn.net/u011630575/article/details/49153597

bootsrap库
http://v3.bootcss.com/javascript/#dropdowns

引入less
http://www.cnblogs.com/lin-dong/p/6711224.html


TODO:
1. 删除drag div 拖动到边缘一个垃圾箱里达到删除的目的-> 改变分组之后的删除策略
2. ~~全局拖动指令  
3. drag的content和特定的变量关联，达到动态修改某个div中内容的效果
4. 上传图片， 控制宽和高
5. ect.
6. 定义元素组　width & height & backgroud-color & 选择图标　添加图标
7. 增加图标库 
8. 保存位置
９.　预定义几个变量绑定到ｄｉｖ的ｃｏｎｔｅｎｔ上

docker run -it --privileged=true -p 8080:8080 --name chrom-word-extention -v F:\workspace\chrom:/home/workspace -w /home/workspace nvm-node-cli-cnpm:2.0 bash
docker commit -a "backup for share node" 986d8311d80f node-for-share:1.0

