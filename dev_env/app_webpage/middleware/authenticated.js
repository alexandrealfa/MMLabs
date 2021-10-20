// eslint-disable-next-line camelcase
import jwt_decode from 'jwt-decode'

export default function (context) {
  if (!context.app.context.app.$cookies.get('token')) {
    return context.redirect('/signin')
  }

  if (context.app.context.app.$cookies.get('token')) {
    const token = context.app.context.$cookies.get('token')
    const { exp } = jwt_decode(token)
    if (Date.now() >= exp * 1000) {
      return context.redirect('/signin')
    }
  }
}
