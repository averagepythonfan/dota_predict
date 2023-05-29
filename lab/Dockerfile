FROM python:3.10-slim

WORKDIR /app

# installing poetry
RUN pip install "poetry==1.3.2"

# copy poetry metadata
COPY poetry.lock .
COPY pyproject.toml .

RUN poetry config virtualenvs.create false && \
    poetry install --only lab

COPY lab/entrypoint.sh entrypoint.sh

RUN chmod +x entrypoint.sh

ENTRYPOINT [ "./entrypoint.sh" ]
