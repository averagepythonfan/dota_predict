FROM python:3.10-slim

WORKDIR /app

# installing poetry
RUN pip install "poetry==1.3.2"

# copy poetry metadata
COPY poetry.lock .
COPY pyproject.toml .

RUN poetry config virtualenvs.create false && \
    poetry install --no-root --only lab

CMD jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root
