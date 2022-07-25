<template>
  <div class="p-3 row justify-content-center register">
    <div class="col-4 p-3 row align-items-center">
      <form class="col p-3">
        <div class="form-group mb-3">
          <input v-model="username" type="text" class="form-control" id="username" aria-describedby="usernameHelp"
                 placeholder="Username">
          <small id="emailHelp" class="form-text text-muted"></small>
        </div>
        <div class="form-group mb-3">
          <input v-model="password" type="password" class="form-control" id="password" placeholder="Password">
        </div>
        <div class="alert alert-danger" v-if="error">{{ error }}</div>
        <div class="row justify-content-center">
          <div @click="login" class="col-8 btn btn-orange">Submit</div>
        </div>
      </form>
    </div>
  </div>

</template>

<script>
import store from '@/store'


export default {
  name: "login-view",
  data: () => {
    return {
      error: null,
      username: '',
      password: '',
    }
  },
  methods: {
    async login() {
      this.error = await store.dispatch('set_jwt', {
        username: this.username,
        password: this.password,
      })
      if (!this.error) {
        this.$router.push({name: 'home'})
      }
    }
  }
}
</script>

<style scoped lang="sass">
.register
  width: 100%
  height: 100vh
  align-items: center

.register > div
  border: 1px solid rgb(53 76 97)
  border-radius: 8px


.register > div
  height: 70vh

</style>