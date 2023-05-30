FROM miladaleali/dev_python:latest

RUN python -m pip install --upgrade pip

RUN pip install \
    structlog==22.3.0\
    gevent==22.10.2\ 
    python-telegram-bot==20.3\
    factory-boy==3.2.1\
    Faker==17.0.0\
    greenlet==2.0.1\
    httpcore==0.17.1\
    httpx==0.24.1\
    Jinja2==3.0.3\
    Mako==1.2.4\
    pandocfilters==1.5.0\
    prometheus-client==0.13.1\
    pytest-celery==0.0.0\
    pytest-mock==3.10.0\
    python-engineio==4.3.4\
    python-socketio==5.7.2\
    rich==13.0.1\
    websocket-client==1.5.0\
    zope.event==4.6\
    zope.interface==5.5.2
