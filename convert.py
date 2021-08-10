import re
import pandas as pd
import numpy as np
from exporter import text_to_textline

"""
Generate a doccano import compatible file
that contains the reports split into one sentence per line
"""
input = "data/captum.csv"
output = "data/captum.text"

# def convert(reports):
#     textline = []
#     for index, row in reports.iterrows():
#         textline.extend(text_to_textline(row['text']))

#     with open(output, 'w') as outfile:
#         for e in textline:
#             outfile.write(e+'\n')

try:
    reports = pd.read_csv(input)
    print(f"Converting '{input}' into '{output}'...")
    np.savetxt(output, reports['lemma'].sample(n=9500,random_state=2).values, fmt='%s')
    print(f'Conversion completed.')
except FileNotFoundError:
    print(f"File '{input}' could not be found.")

