FROM ubuntu:18.04

MAINTAINER Andrey Kononov <akononov.job@gmail.com>

# Install system deps
RUN apt-get update && apt-get install -y \
    libmysqlclient-dev \
    nginx \
    python3-pip \
    python3-virtualenv \
    virtualenv \
    iputils-ping \
    telnet \
 && rm -rf /var/lib/apt/lists/*

 #Configure Environment

ENV PROJECT_PATH=/usr/local/notejam
ENV PROJECT_EXEC=$PROJECT_PATH/venv/bin/notejam

# configure external DB instead of sqllite

ENV DJANGO_SETTINGS_MODULE="settings.docker"

WORKDIR $PROJECT_PATH

ADD prereq $PROJECT_PATH/requirements
#ADD Makefile $PROJECT_PATH/Makefile

ADD docker/conf/gunicorn.ini $PROJECT_PATH/gunicorn.ini
ADD docker/app_wrapper.sh $PROJECT_PATH/
ADD docker/conf/notejam.conf /etc/nginx/sites-available/notejam.conf
ADD docker/conf/dbConnection.sh $PROJECT_PATH/
RUN $PROJECT_PATH/dbConnection.sh
RUN rm -f /etc/nginx/sites-enabled/default
RUN ln -s /etc/nginx/sites-available/notejam.conf /etc/nginx/sites-enabled
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

RUN mkdir -p $PROJECT_PATH/static

ADD . $PROJECT_PATH/notejam

RUN virtualenv --python=/usr/bin/python3.6 --no-wheel $PROJECT_PATH/venv
RUN cd $PROJECT_PATH/notejam; . ../venv/bin/activate; pip install -r prereq/docker.txt

RUN cd $PROJECT_PATH/notejam; . ../venv/bin/activate; pip install -e .

# Configure entrypoint
ADD docker/conf/createadmin.py /usr/local/notejam/createadmin.py
ADD docker/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]
CMD $PROJECT_PATH/app_wrapper.sh