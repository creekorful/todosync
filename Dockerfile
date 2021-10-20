FROM python:3.9.7-alpine3.14

RUN addgroup -S todosync && adduser -S todosync -G todosync

WORKDIR /tmp/build

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN python3 setup.py install

RUN rm -rf /tmp/build

WORKDIR /app
USER todosync

ENTRYPOINT ["python3", "-m", "todosync"]
