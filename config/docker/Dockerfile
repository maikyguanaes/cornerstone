FROM python:3.9 as base

ENV APP_PATH /code

LABEL version=1

ADD . $APP_PATH
WORKDIR $APP_PATH

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT [ "flask" ]
CMD [ "run", "--host=0.0.0.0" ]

FROM base as development
LABEL version=Dev
RUN pip install -r requirements_dev.txt

FROM base as production

ENV FLASK_ENV production
ENV FLASK_APP cornerstone
ENV FLASK_DEBUG False
ENV FLASK_TESTING False
ENV FLASK_RUN_PORT 8080
ENV CURRENT_API_VERSION=v1

ENV PATH $APP_PATH/bin:$PATH

ENTRYPOINT [ "flask" ]
CMD [ "run", "--host=0.0.0.0" ]
