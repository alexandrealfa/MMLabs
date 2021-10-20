import getLocalUrl from '~/services/general/getLocal'

module.exports = {
  devServer: {
    proxy: getLocalUrl(),
  },
}
