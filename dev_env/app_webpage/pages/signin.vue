<template>
  <v-row>
    <v-col class="image-label text-center">
      <img
        src="/profile_default.png"
        alt="Vuetify.js"
        class="image-label__img mb-5"
      />
      <blockquote class="blockquote">
        &#8220;Bem Vindo A MMLabs!.&#8221;
      </blockquote>
      <footer>
        <FormSignIn />
      </footer>
    </v-col>
  </v-row>
</template>

<style lang="scss" scoped>
.image-label {
  &__img {
    height: 150px;
  }
}
</style>
