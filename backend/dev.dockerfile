FROM python:3.10-slim

WORKDIR /app/

COPY requirements.txt .

RUN apt-get update &&\
    apt-get install -y --no-install-recommends\
    gcc\
    build-essential\
    wget\
    git

COPY ./ta-lib-0.4.0-src.tar.gz /app

# RUN wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz
RUN tar -xvzf ta-lib-0.4.0-src.tar.gz && \
  cd ta-lib/ && \
  ./configure --prefix=/usr && \
  make && \
  make install

RUN rm -R ta-lib ta-lib-0.4.0-src.tar.gz

# RUN cat requirements.txt | xargs -n 1 pip install
RUN pip install -r requirements.txt
