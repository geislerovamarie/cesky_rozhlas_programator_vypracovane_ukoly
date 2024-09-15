# 2. Úkol: XML transformace
## Popis programu
Program extrahuje data z .xml souboru a exportuje je do .csv, .tsv nebo .json.

VSTUP: soubor .xml \
VÝSTUP: soubor .tsv, .csv, .json

Z .xml souboru jsou nejprve extrahovány atributy elementu <OM_OBJECT> ObjectID, DirectoryID, TemplateName a jejich hodnoty.
Dále jsou přidány FieldID všech elementů OM_FIELD a text, který do nich spadá.


## Instalace a spuštění
Instalace
```
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```
Spuštění:
```
python3 src/main.py <filename>
```
Příklad:
```
python3 src/main.py data_cleanup.tsv
```
## Testování
```
python3 -m unittest tests/test_clean_data.py
```