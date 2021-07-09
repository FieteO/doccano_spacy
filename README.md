# Doccano annotation server with spacy backend

``` bash
fiete@ubu:~/Documents/programming/spacy/doccano_spacy$ tree -L 2
.
├── custom-model                # contains the spacy model (training) files
│   ├── model-best              # trained model (best)
│   ├── model-last              # trained model (last)
│   ├── base_config.cfg
│   ├── config.cfg
│   └── train.spacy
├── data                        # contains the source data
│   ├── exported
│   ├── captum.csv
│   ├── captum.txt
│   └── doccano_export.zip
├── spacy-server                # spacy backend server
│   ├── app
│   ├── model-best
│   └── Dockerfile
├── convert.py                     # convert reports csv to doccano format
├── docker-compose.yaml
├── exporter.py                 # contains helper functions
├── generate_train_file.py      # generate data file used for training spacy
└── README.md

9 directories, 13 files
```

## Getting started

### Training a custom model

### Spinning up the server