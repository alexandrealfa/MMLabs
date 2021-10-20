<template>
  <v-form v-model="valid">
    <v-container>
      <span v-if="errors.length" class="error-content">
          <p class="error-content__p">
            Por favor, corrija o(s) seguinte(s) erro(s):
          </p>
          <ul class="error-content__ul">
            <li
              v-for="error in errors"
              :key="error.id"
              class="error-content__ul-li"
            >
              {{ error }}
            </li>
          </ul>
        </span>

      <v-row class="justify-center">
        <v-col
          cols="12"
          md="4"
        >
          <v-text-field
            v-model="email"
            :rules="emailRules"
            label="E-mail"
            required
          ></v-text-field>
        </v-col>

        <v-col
          cols="12"
          md="4"
        >
          <v-text-field
            v-model="password"
            :rules="passwordRules"
            :counter="20"
            label="Password"
            required
          ></v-text-field>
        </v-col>
      </v-row>
      <v-row
        class="justify-center"
        cols="12"
        md="4"
      >
        <v-btn
          type="submit"
          @click="RequestForm"
        >
          submit
        </v-btn>
      </v-row>
    </v-container>
  </v-form>
</template>

<script>
import signingRequest from '~/services/requests/signinRequest'

export default {
  data(){
    return {
      errors: [],
      valid: false,
      password: '',
      passwordRules: [
        v => !!v || 'Name is required',
        v => v.length <= 20 || 'Name must be less than 10 characters',
      ],
      email: '',
      emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+/.test(v) || 'E-mail must be valid',
      ],
    }
  },
  methods: {
    RequestForm(e) {
      const formData = {
        username: this.email,
        password: this.password,
      }
      signingRequest.post(formData, this.errors)
      e.preventDefault()
    }
  }
}
</script>

<style lang="scss" scoped>
.error-content {
  padding: 10px;
  &__p{
    font-size: 0.8em;
    font-weight: bold;
  }
  &__ul{
    &-li{
      color: red;
      font-size: 0.7em;
    }
  }
}
</style>
