import axios from 'axios'
import Cookies from 'js-cookie'
import getLocalUrl from '~/services/general/getLocal'

async function signingPost(data, error) {
  const formData = new FormData()
  formData.append('username', data.username)
  formData.append('password', data.password)
  await axios
    .post(`${getLocalUrl()}token`, formData)
    .then((response) => {
      Cookies.set('token', response.data.access_token)
      window.$nuxt.$store.dispatch('profile/getPosts')
      window.$nuxt.$router.push({ path: 'profiles' })
    })
    .catch(() => {
      error.push(
        'Não foi possível fazer login, suas credenciais estão incorretas, por favor tente novamente'
      )
    })
}

const signingRequest = {
  post: signingPost,
}

export default signingRequest
