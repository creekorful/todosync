FROM python:3.9.6-alpine3.14

WORKDIR /app

# Create the user to run the app
RUN addgroup -S todosync && adduser -S todosync -G todosync
USER todosync

# Install the dependencies in a separate layer to enable caching
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY todosync ./todosync

ENTRYPOINT ["python3", "-m", "todosync"]
