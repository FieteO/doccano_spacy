FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./app /app
WORKDIR /app
RUN pip install -r requirements

# replaced with volume mount (see docker-compose.yaml)
# COPY ./model-best /model

EXPOSE 8080
CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080" ]