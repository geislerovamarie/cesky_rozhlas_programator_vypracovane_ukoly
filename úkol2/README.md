# 2. Úkol: XML transformace
## Popis programu
TODO kratke shrnuti

VSTUP: soubor .xml \
VÝSTUP: soubor .tsv, .csv, .json

Postup?


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