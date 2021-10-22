import axios from 'axios'
import getLocalUrl from '~/services/general/getLocal'
import profileRequest from '~/services/requests/profileRequest'

function signupPost(data) {
  axios
    .post(`${getLocalUrl()}users`, data)
    .then((response) => {
      const profileDefault = {
        profile_url: "https://picsum.photos/400/400",
        banner_profile_url: "string",
        bio: "Nada A Informar",
        user_id: response.data.id
      }
      profileRequest.post(profileDefault)
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
