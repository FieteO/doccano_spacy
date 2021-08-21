# https://stackoverflow.com/questions/57902256/how-to-export-document-with-entities-from-spacy-for-use-in-doccano#58524417
import spacy


def text_to_jsonl(text):
    """
    :text (str): source text
    Returns (list (dict)): deccano format json
    """
    nlp = spacy.load('en_core_web_md')
    djson = list()
    doc = nlp(text)
    for sent in doc.sents:
        labels = list()
        for e in sent.ents:
            labels.append([e.start_char, e.end_char, e.label_])
        djson.append({'text': sent.text, "labels": labels})
    return djson

def text_to_textline(text):
    nlp = spacy.load('en_core_web_md')
    textline = list()
    doc = nlp(text)
    for sent in doc.sents:
        textline.append(sent.text)
    return textline

def jsonl_to_list(filepath):
    import ast
    with open(filepath) as f:
        content = f.readlines()

    data = []
    for line in content:
        line = ast.literal_eval(line)
        data.append((line['data'], {'entities': line['label']}))
    return data
