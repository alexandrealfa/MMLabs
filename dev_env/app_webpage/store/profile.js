import axios from 'axios'
import Cookies from 'js-cookie'
import getLocalUrl from '~/services/general/getLocal'

export const state = () => ({
  list: [],
})

export const actions = {
  async getPosts({ commit }) {
    const res = await axios.get(`${getLocalUrl()}profile/`, {
      headers: {
        Authorization: `Bearer ${Cookies.get('token')}`,
      },
    })
    commit('SET_POSTS', res.data)
  },
}

export const mutations = {
  SET_POSTS(state, profilesData) {
    state.list = profilesData
  },
  removeProfile(state, profile) {
    state.profiles = state.list.filter(
      (item) => item.id !== profile.id
    )
  },
}
