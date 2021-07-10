# https://linuxize.com/post/bash-check-if-file-exists/#check-if-directory-exist
DIR=/model/abc
if [ ! -d "$DIR" ]; then
    echo "Custom spacy model not provided, downloading official one..."
    python -m spacy download en_core_web_md
    echo "Download complete"
else
    echo "Custom model was provided."
fi
uvicorn app.main:app --host 0.0.0.0 --port 8080