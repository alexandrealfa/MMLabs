<template>
  <v-card
    class="mx-auto"
    max-width="344"
  >
    <v-img
      :src= profileImg
      height="200px"
    ></v-img>

    <v-card-title>
      {{ username }}
    </v-card-title>

    <v-card-subtitle>
      Sobre Mim: {{ bio }}
    </v-card-subtitle>

    <v-card-actions>
      <v-btn
        color="orange lighten-2"
        text
      >
        Informações
      </v-btn>

      <v-spacer></v-spacer>

      <v-btn
        icon
        @click="show = !show"
      >
        <v-icon>{{ show ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
      </v-btn>
    </v-card-actions>

    <v-expand-transition>
      <div v-show="show">
        <v-divider></v-divider>

        <v-card-text>
          <div class="row mt-1">
            <p>Email: {{ email }}</p>
            <p>Telefone: {{ phone }}</p>
          </div>
        </v-card-text>
      </div>
    </v-expand-transition>
  </v-card>
</template>

<script>
export default {
  name: "CardProfile",
  props: {
    username: {
      type: String,
      default: 'Username',
    },
    email: {
      type: String,
      default: 'E-mail',
    },
    phone: {
      type: String,
      default: 'Telefone',
    },
    bio: {
      type: String,
      default: 'Biografia Vazia',
    },
    profileImg: {
      type: String,
      default: 'https://picsum.photos/id/1/500/500',
    },
  },
  data() {
    return {
      show: false,
    }
  }
}
</script>

<style scoped>

</style>
