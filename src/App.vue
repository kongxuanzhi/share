<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'app'
}
</script>

<style>
@font-face {
  font-family: "邯郸-郭灵霞灵芝体";
  src: url(../static/test.ttf);
}

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased; 
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
</style>
