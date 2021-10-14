echo '\e[1;32m'"= = = = = = = = = = = = = = = = = = = = = ="'\e[0m'
echo '\e[1;32m'"=      Creating API environment           ="'\e[0m'
echo '\e[1;32m'"= = = = = = = = = = = = = = = = = = = = = ="'\e[0m'

if [ ! -d medqi_api ]; then
    echo '\e[1;33m'"= = = = = = = ="'\e[0m'
    echo '\e[1;33m'"=  Cloning the API"'\e[0m'
    echo '\e[1;33m'"= = = = = = = ="'\e[0m'
    git clone git@gitlab.com:target-clock/medqi/medqi_api.git
fi

cd medqi_api

if [ ! -e secrets.toml ] || [ ! -e .env ]; then
    echo '\e[1;31m'"= = = = = = = ="'\e[0m'
    echo '\e[1;31m'" You need to create your config files to the API"'\e[0m'
    echo '\e[1;31m'"  -> secrets.toml"'\e[0m'
    echo '\e[1;31m'"  -> .env"'\e[0m'
    echo '\e[1;31m'"= = = = = = = ="'\e[0m'
    exit 1
fi
echo '\e[1;33m'"= = = = = = = ="'\e[0m'
echo '\e[1;33m'"Building docker image for API"'\e[0m'
echo '\e[1;33m'"= = = = = = = ="'\e[0m'
pwd
docker build -t medqi/api .
cd ..

echo '\e[1;32m'"= = = = = = = = = = = = = = = = = = = = = ="'\e[0m'
echo '\e[1;32m'"=      Creating Front-End environment     ="'\e[0m'
echo '\e[1;32m'"= = = = = = = = = = = = = = = = = = = = = ="'\e[0m'

if [ ! -d medqi_web ]; then
    echo '\e[1;33m'"= = = = = = = ="'\e[0m'
    echo '\e[1;33m'"Cloning the web"'\e[0m'
    echo '\e[1;33m'"= = = = = = = ="'\e[0m'
    git clone git@gitlab.com:target-clock/medqi/medqi_api.git
fi

cd medqi_web
echo '\e[1;33m'"= = = = = = = ="'\e[0m'
echo '\e[1;33m'"Building docker image for front-end"'\e[0m'
echo '\e[1;33m'". . . . . . . ."'\e[0m'
echo '\e[1;33m'Path: "$(pwd)"'\e[0m'
echo '\e[1;33m'"= = = = = = = ="'\e[0m'
docker build -t medqi/web .
cd ..
