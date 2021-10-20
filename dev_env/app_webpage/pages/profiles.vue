<template>
  <v-row>
    <v-row  class="mt-6 text-center">
        <div v-for="profile in profilesData" :key="profile.id" class="col-sm-12 col-lg-4 col-md-6">
          <CardProfile
            v-if="profile.user.person"
            :username="profile.user.username"
            :bio="profile.bio"
            :email="profile.user.email"
            :phone="profile.user.person.phone"
            :profile-img="profile.profile_url"
            class="m-4"/>
        </div>
    </v-row>
  </v-row>
</template>

<script>
export default {
  middleware: 'authenticated',
  computed: {
    profilesData() {
      return this.$store.state.profile.list
    },
  },
  mounted() {
    this.$store.dispatch('profile/getPosts')
  },
}
</script>
