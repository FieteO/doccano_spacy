# https://towardsdatascience.com/using-spacy-3-0-to-build-a-custom-ner-model-c9256bea098
from exporter import jsonl_to_list
from tqdm import tqdm
import spacy
from spacy.tokens import DocBin

nlp = spacy.load('en_core_web_md') # load a new spacy model

def generate_training_file(training_data):
    """ Generate a spacy training file that is used when invoking `spacy train` """
    db = DocBin() # create a DocBin object
    for text, annot in tqdm(training_data): # data in previous format
        doc = nlp.make_doc(text) # create doc object from text
        ents = []
        for start, end, label in annot["entities"]: # add character indexes
            span = doc.char_span(start, end, label=label, alignment_mode="contract")
            if span is None:
                print("Skipping entity")
            else:
                ents.append(span)
        doc.ents = ents # label the text with the ents
        db.add(doc)

    db.to_disk("./custom-model/train.spacy") # save the docbin object

filepath = 'data/exported/admin.jsonl'
data = jsonl_to_list(filepath)
generate_training_file(data)