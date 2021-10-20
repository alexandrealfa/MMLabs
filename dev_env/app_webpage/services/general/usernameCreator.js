const usernameBuild = (name) => {
  return name.split(' ')[0] + ' ' + name.split(' ')[name.split(' ').length - 1]
}

export default usernameBuild
