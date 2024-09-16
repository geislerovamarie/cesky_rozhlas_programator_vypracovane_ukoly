# 2. Úkol: XML transformace
## Popis programu
Program extrahuje data z .xml souboru a exportuje je do .csv, .tsv nebo .json.

VSTUP: soubor .xml \
VÝSTUP: soubor .tsv, .csv, .json

Načtou se argumenty z CLI a zkontrolují se. Z daného .xml souboru jsou nejprve extrahovány atributy elementu <OM_OBJECT> ObjectID, DirectoryID, TemplateName a jejich hodnoty. Dále jsou přidány FieldID všech elementů <OM_FIELD> a text, který do nich spadá.

## Instalace a spuštění
Instalace
```
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```
Spuštění:
```
python3 src/main.py --source_file=<path_to_input_file> --output_file=<path_to_output_file> --otype=<type>
```
Příklady:
```
python3 src/main.py --source_file=../úkol2/obecnа_osoba.xml --output_file=../úkol2/obecna_osoba.csv --otype=csv
```
```
python3 src/main.py --source_file=../úkol2/obecnа_osoba.xml --otype=tsv
```
```
python3 src/main.py --source_file=../úkol2/obecnа_osoba.xml --output_file=../úkol2/obecna_osoba.json
```
## Testování
```
python3 -m unittest tests/test_handle_arguments.py
```