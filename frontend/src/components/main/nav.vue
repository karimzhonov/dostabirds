<template>
  <div class="navbar row justify-content-between p-3">
    <div class="col logo">
      Dostathing
    </div>
    <div class="col-5 auth">
      <div v-if="!user" class="row justify-content-around">
        <div @click="goToRegister" class="col-8 btn btn-orange my-btn">Register</div>
        <div @click="goToLogin" class="col-2 btn my-btn">Login</div>
      </div>
      <div v-if="user" class="row justify-content-around">
        <div class="col-8 btn my-btn btn-orange">{{user.username}}</div>
        <div @click="goToLogout" class="col-2 btn my-btn">Logout</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "NavbarComp",
  props: ['user'],
  methods: {
    goToRegister() {
      this.$router.push({name: 'register'})
    },
    goToLogin() {
      this.$router.push({name: 'login'})
    },
    goToLogout() {
      localStorage.setItem('access_token', null)
      localStorage.setItem('refresh_token', null)
      window.location.reload()
    }
  }
}
</script>

<style scoped lang="sass">
.logo
  font-weight: bold
  font-size: 30px
  color: #FFFFFF

.my-btn
  color: #FFFFFF
  font-weight: bold

</style>