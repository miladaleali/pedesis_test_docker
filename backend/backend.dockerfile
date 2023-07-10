FROM miladaleali/pedesis_prod_env:latest as base

ARG GIT_TOKEN_PEDESIS

WORKDIR /app/

COPY ./app /app
COPY ./debug /app/debug

ENV PYTHONPATH=/app

RUN pip install git+https://${GIT_TOKEN_PEDESIS}@github.com/miladaleali/pedesis.git
RUN pip install tqdm
######################## START NEW BASE IMAGE: PRE PRODUCTION ############################
# FROM base as prod_base

# ENV GIT_TOKEN_PEDESIS=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

# RUN pip install git+https://${GIT_TOKEN_PEDESIS}@github.com/miladaleali/pedesis.git

######################## START NEW BASE IMAGE: PRE DEBUGGER ############################
# FROM base as debug_base

# COPY ./pedesis /usr/local/lib/python3.10/site-packages/pedesis

######################## START NEW IMAGE: DEBUGGER ############################
FROM base as debug
RUN pip install ptvsd

WORKDIR /app/

CMD python -m ptvsd --host 0.0.0.0 --port 5678 --wait --multiprocess -m manage run station

######################## START NEW IMAGE: PRODUCTION ##########################
FROM base as prod

COPY ./app/station-start.sh /station-start.sh

RUN chmod +x /station-start.sh

CMD bash /station-start.sh

######################## START NEW IMAGE: NOTEBOOK ##########################
FROM base as notebook
RUN pip install notebook

COPY ./app/lab-start.sh /lab-start.sh

RUN chmod +x /lab-start.sh

CMD bash /lab-start.sh && python -m notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root

######################## START NEW IMAGE: WORKER ##########################
FROM base as worker

COPY ./app/worker-start.sh /worker-start.sh

RUN chmod +x /worker-start.sh

CMD bash /worker-start.sh

######################## START NEW IMAGE: FLOWER ##########################
FROM base as flower
ARG FLOWER_PORT

RUN pip install flower

######################## START NEW IMAGE: BEAT ##########################
FROM base as beat

CMD celery -A pedesis.tasks_manager.manager beat -S redbeat.RedBeatScheduler -l INFO
