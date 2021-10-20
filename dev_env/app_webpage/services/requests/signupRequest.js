import axios from 'axios'
import getLocalUrl from '~/services/general/getLocal'

function signupPost(data) {
  axios
    .post(`${getLocalUrl()}users`, data)
    .then((response) => {
      window.$nuxt.$router.push({ path: 'Signin' })
    })
    .catch(() => {
      window.$nuxt.$router.push({ path: 'Signup' })
    })
}

const signupRequest = {
  post: signupPost,
}

export default signupRequest
