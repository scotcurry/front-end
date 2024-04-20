FROM python:3.11.8-slim-bookworm

EXPOSE 8000

WORKDIR /app
COPY ../requirements.txt requirements.txt
# See Datadog Static Analysis -- https://docs.datadoghq.com/code_analysis/static_analysis_rules/docker-best-practices/pip-pin-versions/
RUN python3 -m pip install --upgrade pip==24.0 && python3 -m pip install --no-cache-dir -r requirements.txt
COPY . .

RUN useradd appuser && chown -R appuser /app
USER appuser

ENV DD_LOGS_INJECTION=true
CMD exec gunicorn -b :8000 --workers 1 --threads 8 --timeout 0 app:app
