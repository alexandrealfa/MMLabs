<template>
  <v-row justify="center" align="center">
    <v-col cols="12" sm="8" md="6">
      <v-card class="logo py-4 d-flex justify-center"> </v-card>
      <v-card>
        <v-card-title class="headline">
          Seja Bem-Vindo(a) a MMLabs!.
        </v-card-title>
        <v-card-text>
          <p>
            Crie Uma Conta e Venha fazer parte dessa rede!.
          </p>
          <p>
            Acesse o Link Abaixo Para fazer um cadastro:
            <a href="/signup" rel="noopener noreferrer"> Signup </a>.
          </p>
          <p>
            Para Ter acesso aos conteúdos do Menu é necessário estar logado!.
            <a href="/signin" rel="noopener noreferrer" title="chat"> Signin </a
            >.
          </p>
          <p>
            Para Navegar na aplicação, existe um menu lateral, que irá lhe
            ajudar com o acesso entre as paginas.
          </p>
          <div class="text-xs-right">
            <em><small>&mdash; Alexandre Alfa</small></em>
          </div>
          <hr class="my-3" />
          <a
            href="https://github.com/alexandrealfa/MMLabs"
            target="_blank"
            rel="noopener noreferrer"
          >
            Project GitHub
          </a>
        </v-card-text>
        <v-card-actions>
          <v-spacer />
          <v-btn color="primary" nuxt to="/Signup">
            Signup
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-col>
  </v-row>
</template>
