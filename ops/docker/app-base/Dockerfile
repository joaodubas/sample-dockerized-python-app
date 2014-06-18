# base for sample app
#
# VERSION: see `TAG`
FROM debian:jessie
MAINTAINER Joao Paulo Dubas "joao.dubas@gmail.com"

# install system deps
RUN apt-get -y -qq --force-yes update \
    && apt-get -y -qq --force-yes install \
        build-essential \
        python-setuptools \
        python-dev \
        libpq-dev \
        sudo \
        openssl

# install pip & virtualenv
RUN easy_install pip \
    && pip install virtualenv virtualenvwrapper

# setup virtualenv
ENV WORKON_HOME /opt/.venv
RUN echo "export WORKON_HOME=${WORKON_HOME}" >> /etc/skel/.bashrc \
    && echo "source /usr/local/bin/virtualenvwrapper.sh" >> /etc/skel/.bashrc \
    && mkdir ${WORKON_HOME}

# create app virtualenv
ENV APP_VENV_HOME ${WORKON_HOME}/app
ENV APP_PROJ_HOME /opt/app
ADD requirements.txt /requirements.txt
RUN virtualenv ${APP_VENV_HOME} \
    && ${APP_VENV_HOME}/bin/pip install -r /requirements.txt \
    && echo ${APP_PROJ_HOME} > ${APP_VENV_HOME}/.project

# create sudo user
ENV PASSWD 123app4
RUN echo "User password: ${PASSWD}" \
    && useradd \
        -G sudo \
        -d /home/app \
        -m \
        -p $(openssl passwd $PASSWD) \
        -s /bin/bash \
        app

# change workon ownership to app user
RUN chown -R app:app ${WORKON_HOME}

# configure container
ENV APP_PORT 8000
USER app
EXPOSE 8000

# run extra commands on build
ONBUILD ADD requirements.txt /requirements.txt
ONBUILD RUN ${APP_VENV_HOME}/bin/pip install -r /requirements.txt
