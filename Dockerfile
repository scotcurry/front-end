FROM python:3.11.8-slim-bookworm

EXPOSE 8000

WORKDIR /app
COPY ../requirements.txt requirements.txt
RUN python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . .

RUN useradd appuser && chown -R appuser /app
USER appuser
CMD exec ddtrace-run gunicorn -b :8000 --workers 1 --threads 8 --timeout 0 app:app
