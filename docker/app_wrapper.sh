#!/bin/sh

set -e

. ${PROJECT_PATH}/venv/bin/activate
cd ${PROJECT_PATH}/notejam
#python3 ${PROJECT_PATH}/notejam/docker/get_credentials.py
#. ${PROJECT_PATH}/secret_env.sh
#. ${PROJECT_PATH}/db_config.sh
. ${PROJECT_PATH}/dbConnection.sh
notejam syncdb --noinput
notejam migrate --noinput
notejam collectstatic --clear --noinput
notejam collectstatic --noinput
python ${PROJECT_PATH}/createadmin.py
tail -n0 -f /var/log/nginx/*log &
echo `sleep 5 ; service nginx start` &
gunicorn --help
gunicorn --config=${PROJECT_PATH}/gunicorn.ini --chdir=/usr/local/notejam/notejam/notejam notejam.wsgi

