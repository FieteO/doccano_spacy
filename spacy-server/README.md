# [SciSpacy](https://allenai.github.io/SciSpaCy/)

## Download the model
``` bash
wget -O en_core_sci_md 'https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.4.0/en_core_sci_md-0.4.0.tar.gz'
```

# Test authentication
``` bash
curl -X POST -F 'foo=bar' -u 'admin:password' http://localhost:8080/auto_annotate
```
## Using Header
Get the Base64 encoded credentials:
``` bash
(nlp_env) fiete@ubu:~/Documents/programming/doccano_spacy$ echo -n 'admin:password' | base64
YWRtaW46cGFzc3dvcmQ=
```

``` bash
curl -X POST -F 'foo=bar' -H 'Authorization: Basic YWRtaW46cGFzc3dvcmQ=' http://localhost:8080/auto_annotate
```

``` bash
curl -X POST -F 'foo=bar' -H 'Authorization: Basic ZG9jY19zcGFjeTpZQXQ5NVFhRllBdDk1UWFG' http://localhost:8080/auto_annotate
```