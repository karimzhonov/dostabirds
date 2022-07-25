<template>
  <navbar :user="user"/>
  <div class="content">
    Content
  </div>
</template>

<script>
import navbar from "@/components/main/nav";
import store from '@/store'

export default {
  name: 'HomeView',
  data() {
    return {
      user: null
    }
  },
  components: {navbar},
  async created() {
    let jwt_token = await store.dispatch('get_jwt')
    this.user = await store.dispatch('get_me', jwt_token)


  },
  methods: {

  }
  ,
}
</script>
