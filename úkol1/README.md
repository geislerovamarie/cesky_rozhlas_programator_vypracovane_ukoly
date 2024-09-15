# 1. Úkol: Data cleanup
## Popis programu
Program zpracuje soubor formátu .csv nebo .tsv a vrátí indexy řádků určených k odstranění.

VSTUP: soubor .csv nebo .tsv \
VÝSTUP: vytisknou se 2 seznamy indexů pro řádky určené k odstranění
- 1. seznam odpovídá indexům, které by odpovídaly situaci, kdy jsou hodnoty načtené samostatně bez názvů sloupců a také kdy indexování začíná od 0.
- 2. seznam odpovídá indexům pro tabulky indexované od 1 a kdy je první řádek obsazen názvy sloupců.

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