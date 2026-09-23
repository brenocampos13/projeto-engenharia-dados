FROM python:3.13-slim

WORKDIR /app

RUN pip install dbt-postgres

COPY . .

ENV DBT_PROFILES_DIR=/app

CMD ["dbt", "build"]