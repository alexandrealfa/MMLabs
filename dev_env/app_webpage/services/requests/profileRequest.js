import axios from 'axios'
import Cookies from 'js-cookie'
import getLocalUrl from '~/services/general/getLocal'

async function profilePost(data, error = []) {
  await axios
    .post(`${getLocalUrl()}profile`, data, {
      headers: {
        Authorization: `Bearer ${Cookies.get('token')}`,
      },
    })
    .then((response) => {
      window.$nuxt.$router.push({ path: 'Signin' })
    })
    .catch(() => {
      error.push(
        'Não foi possível cadastrar os seus dados de perfil, verifique suas credenciais e tente novamente!.'
      )
    })
}

const profileRequest = {
  post: profilePost,
}

export default profileRequest
