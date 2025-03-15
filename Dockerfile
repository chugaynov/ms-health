FROM python:3.12-alpine

ENV APP_PATH=/project \
    PYTHONPATH=/project/src \
    COVERAGE_FILE=/tmp/coverage.db \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTEST_ADDOPTS="-p no:cacheprovider"

WORKDIR $APP_PATH

EXPOSE 8080

COPY ./pyproject.toml ./poetry.lock* ./

RUN apk update \
    && apk add --no-cache make \
    && adduser -u101 -D python-user \
    && pip install poetry==1.7.0 \
    && poetry config virtualenvs.create false \
    && poetry install --no-ansi

COPY . ./

USER python-user

CMD ["python", "src/app/main.py"]
