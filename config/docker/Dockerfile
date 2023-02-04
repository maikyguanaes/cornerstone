FROM python:3.9 as base
LABEL version=1
ADD . /code
WORKDIR /code
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT [ "flask" ]
CMD [ "run", "--host=0.0.0.0" ]

FROM base as development
LABEL version=Dev
RUN pip install -r requirements_dev.txt