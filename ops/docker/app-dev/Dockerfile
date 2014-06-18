# development sample app
#
# VERSION: see `TAG`
FROM joaodubas/base-sample-app:201406.6
MAINTAINER Joao Paulo Dubas "joao.dubas@gmail.com"

# configure container
VOLUME  ${APP_PROJ_HOME}
ENTRYPOINT ["${APP_VENV_HOME}/bin/python"]
CMD ["${APP_PROJ_HOME}/src/main.py"]
