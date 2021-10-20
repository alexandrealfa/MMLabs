<template>
  <v-form>
    <v-container>
      <v-row class="justify-center">
        <v-col
          cols="12"
          md="4"
        >
          <v-text-field
            v-model="dataForm.username"
            label="Username"
            required
          ></v-text-field>
        </v-col>

        <v-col
          cols="12"
          md="4"
        >
          <v-text-field
            v-model="dataForm.name"
            label="Nome"
            required
          ></v-text-field>
        </v-col>

        <v-col
          cols="12"
          md="4"
        >
          <v-text-field
            v-model="dataForm.cpf"
            :rules="cpfRule"
            label="Cpf"
            required
          ></v-text-field>
        </v-col>

        <v-col
          cols="12"
          md="4"
        >
          <v-text-field
            v-model="dataForm.email"
            label="E-mail"
            :rules="emailRules"
            required
          ></v-text-field>
        </v-col>

        <v-col
          cols="12"
          md="4"
        >
          <v-text-field
            v-model="dataForm.phone"
            label="Telefone"
            :rules="phoneRule"
            required
          ></v-text-field>
        </v-col>

        <v-col
          cols="12"
          md="4"
        >
          <v-text-field
            v-model="dataForm.password"
            :counter="20"
            label="Senha"
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
import signupRequest from "~/services/requests/signupRequest";

export default {
  data(){
    return {
      valid: false,
      dataForm: {
        name: '',
        username: '',
        cpf: '',
        email: '',
        phone: '',
        birth_date: '2021-10-20',
        user_group: 'professional',
        password: '',
      },
      passwordRules: [
        v => !!v || 'O Campo Password é necessário!',
        v => v.length <= 20 || 'A senha inserida Ultrapassa 20 caracteres.',
      ],
      emailRules: [
        v => !!v || 'O Campo Cpf é necessário!',
        v => /.+@.+/.test(v) || '"Ex: (email@email.com)"',
      ],
      cpfRule: [
        v => !!v || "O Campo Cpf é necessário!",
        v => /([0-9]{2}[.]?[0-9]{3}[.]?[0-9]{3}[/]?[0-9]{4}[-]?[0-9]{2})|([0-9]{3}[.]?[0-9]{3}[.]?[0-9]{3}[-]?[0-9]{2})/.test(v) || "Ex: (01122232323)",
      ],
      phoneRule:[
        v => !!v || "O Campo Telefone é necessário!",
        v => /(\(?\d{2}\)?\s)?(\d{4,5}-\d{4})/.test(v) || "Ex: (99 99999-9999)"
      ]
    }
  },
  methods: {
    RequestForm(e) {
      // eslint-disable-next-line no-console
      signupRequest.post(this.dataForm)
      e.preventDefault()
    }
  }
}
</script>
