# https://github.com/doccano/doccano/issues/1417#issuecomment-866685966
import secrets
from fastapi import FastAPI, Depends, status
from fastapi.exceptions import HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
# from auth import has_access
import spacy
import json
import os
from os import listdir, getenv


    
model = '/model'
if not listdir(model):
    model = 'en_core_web_md'

# nlp = spacy.load("/model")
nlp = spacy.load(model)

class TextToAnnotate(BaseModel):
    text: str

app = FastAPI()

security = HTTPBasic()

def has_access(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, os.getenv('SPACY_USER'))
    correct_password = secrets.compare_digest(credentials.password, os.getenv('SPACY_PASSWORD'))
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

# Try it out on http://localhost:8080/docs in your browser
@app.get('/get')
def get():
    return 'hello'

@app.post("/auto_annotate", dependencies=[Depends(has_access)])
async def auto_annotate(document: TextToAnnotate):
    doc = nlp(document.text)
    ent_label_list = [
        {"label": ent.label_, "start_offset": ent.start_char, "end_offset": ent.end_char} for ent in doc.ents
    ]
    response = json.dumps(ent_label_list)
    return response