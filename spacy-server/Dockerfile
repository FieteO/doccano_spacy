FROM python:3.7

COPY . /app
WORKDIR /app
RUN pip install -r app/requirements \
    && chmod +x run.sh

EXPOSE 8080
# Conditionally downloads the official spacy model
CMD './run.sh'