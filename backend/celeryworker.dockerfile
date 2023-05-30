FROM miladaleali/pedesis_prod_env:latest as base

WORKDIR /app/

ARG GIT_TOKEN_PEDESIS

RUN pip install git+https://${GIT_TOKEN_PEDESIS}@github.com/miladaleali/pedesis.git

COPY ./app /app
# COPY ./pedesis/pedesis /app/pedesis/
WORKDIR /app

ENV PYTHONPATH=/app

######################## START NEW IMAGE: DEBUGGER ############################‍
FROM base as debug
RUN pip install ptvsd

WORKDIR /app/

CMD python -m ptvsd --host 0.0.0.0 --port 5679 --wait --multiprocess -m manage run celery
######################## START NEW IMAGE: PRODUCTION ##########################
FROM base as prod

COPY ./app/worker-start.sh /worker-start.sh

RUN chmod +x /worker-start.sh

CMD bash /worker-start.sh
######################## START NEW IMAGE: PRODUCTION ##########################
FROM base as flower
ARG FLOWER_PORT

RUN pip install flower

# CMD celery -A pedesis.tasks_manager:manager flower --port=${FLOWER_PORT} --persisten=True
