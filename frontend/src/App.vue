<template>
  <div class="container-fluid main">
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App',
}
</script>

<style lang="sass">
@import "bootstrap"


*
  padding: 0
  margin: 0
  box-sizing: border-box
  color: #DDDDDD


#app
  background-color: #0F161C
  min-height: 100vh
  width: 100%


.btn-orange
  background-color: #FF9147
  color: #000000

.main
  min-height: 100vh
</style>
