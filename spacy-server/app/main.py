from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import spacy
import json

# https://github.com/doccano/doccano/issues/1417#issuecomment-866685966

nlp = spacy.load("/model")

class TextToAnnotate(BaseModel):
    text: str

app = FastAPI()

@app.post("/auto_annotate")
async def auto_annotate(document: TextToAnnotate):
    doc = nlp(document.text)
    ent_label_list = [
        {"label": ent.label_, "start_offset": ent.start_char, "end_offset": ent.end_char} for ent in doc.ents
    ]
    response = json.dumps(ent_label_list)
    return response

@app.get('/get')
def get():
    return 'hello'

if __name__ == "__main__":
    host = 'spacy-server'
    #uvicorn.run('auto_annotate:app', host=host, port=8080)