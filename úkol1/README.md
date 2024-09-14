# 1. Úkol: Data cleanup
## Popis programu
Program zpracuje soubor formátu .csv nebo .tsv a vrátí indexy řádků určených k odstranění.

VSTUP: soubor .csv nebo .tsv
VÝSTUP: vytiskne se seznam indexů pro řádky určené k odstranění

Postup:
- Předpokládá se, že soubor může mít tisíce řádků, zpracovává se tedy postupně po kusech o 1000 řádcích.
- v každém kusu:
    - pro každou sekvenci se stejným ObjectID se spočítá se počet řádků s neprázdným Name
    - pro sekvence s 0 neprázdnými řádky se uloží ObjectID a index prvního řádků jako záloha
    - sekvence s alespoň 1 neprázdným řádkem se uloží jako kontrola do množiny, že není potřeba využít zálohu
    - všechny řádky s prázdným Name se označí k odstranění
- po zpracování všech kusů se projdou ObjectID v záloze a zkontroluje se za pomocí kontrolní množiny, zda je potřeba je využít
    - pokud se nenachází v kontrolní množině, jsou odstraněny z finálního seznamu řádků k odstranění


## Instalace a spuštění
```
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```
```
python3 src/main.py <filename>
```
příklad:
```
python3 src/main.py data_cleanup.tsv
```
## Testování