# https://towardsdatascience.com/using-spacy-3-0-to-build-a-custom-ner-model-c9256bea098
from exporter import jsonl_to_list
import pandas as pd
from tqdm import tqdm
import spacy
from spacy.tokens import DocBin

# def generate_training_file(training_data, outdir, model = 'en_core_web_md'):
#     """ Generate a spacy training file that is used when invoking `spacy train` """
#     nlp = spacy.load(model)
#     db = DocBin() # create a DocBin object
#     for text, annot in tqdm(training_data): # data in previous format
#         doc = nlp.make_doc(text) # create doc object from text
#         ents = []
#         for start, end, label in annot["entities"]: # add character indexes
#             span = doc.char_span(start, end, label=label, alignment_mode="contract")
#             if span is None:
#                 print("Skipping entity")
#             else:
#                 ents.append(span)
#         doc.ents = ents # label the text with the ents
#         db.add(doc)
#     db.to_disk(outfile) # save the docbin object
#     print(f'Successfully wrote \'{outfile}\' to disk')

def df_to_spacy(df, outfile, model = 'en_core_web_md'):
    """ Convert a dataframe into a .spacy training file """
    nlp = spacy.load(model)
    # nlp = spacy.blank("en")
    db = DocBin() # create a DocBin object
    for index, row in df.iterrows():
        doc = nlp.make_doc(row['data']) # create doc object from text
        ents = []
        for start, end, label in row['label']: # add character indexes
            span = doc.char_span(start, end, label=label, alignment_mode="contract")
            if span is None:
                print("Skipping entity")
            else:
                ents.append(span)
        doc.ents = ents # label the text with the ents
        db.add(doc)
    db.to_disk(outfile) # save the docbin object
    print(f'Successfully wrote \'{outfile}\' to disk')

def generate_training_file(filepath, outdir, model = 'en_core_web_md'):
    """ Convert and split a jsonl file into spacy training files that are used when invoking `spacy train` """
    df = pd.read_json(path_or_buf=filepath, lines=True)
    df = df[df['label'].str.len() > 0]                  # filter out rows without labels
    train=df.sample(frac=0.8,random_state=2)
    test=df.drop(train.index)
    df_to_spacy(train, f'{outdir}/train.spacy', model)
    df_to_spacy(test, f'{outdir}/test.spacy', model)

if __name__ == '__main__':
    filepath = 'data/exported/admin.jsonl'
    outdir = "./custom-model"
    generate_training_file(filepath, outdir)