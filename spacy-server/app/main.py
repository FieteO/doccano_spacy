from fastapi import FastAPI
from pydantic import BaseModel
import spacy
import json

# https://github.com/doccano/doccano/issues/1417#issuecomment-866685966

# nlp = spacy.load("/model")
nlp = spacy.load('en_core_web_md')

class TextToAnnotate(BaseModel):
    text: str

app = FastAPI()

# Try it out on http://localhost:8080/docs in your browser
@app.get('/get')
def get():
    return 'hello'

@app.post("/auto_annotate")
async def auto_annotate(document: TextToAnnotate):
    doc = nlp(document.text)
    ent_label_list = [
        {"label": ent.label_, "start_offset": ent.start_char, "end_offset": ent.end_char} for ent in doc.ents
    ]
    response = json.dumps(ent_label_list)
    return response