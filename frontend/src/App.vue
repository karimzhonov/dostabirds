<template>
  <HomeView></HomeView>
</template>

<script>
import HomeView from "@/views/HomeView";
import axios from 'axios'
import store from "@/store";

export default {
  name: 'App',
  components: {HomeView},
  async created () {
    let response = await axios.get(`http://${store.state.host}/api/v1/test`)
      console.log(response.data)
      response = await axios.post(`http://${store.state.host}/api/v1/test`, {
        'user_id': 1
      })
      console.log(response.data)
  },
  data: () => {
    return {
      test_text: '',
    }
  }
}
</script>

<style lang="sass">

</style>
