# Report

## Příprava

Soubor `fpga-data.txt` má podobu hexadecimálních řetězců o velikosti dvou slabik (bajtů). Každý řetězec má tedy 16 bitů informace. S rozdělením na jednotlivé bitstreamy nám pomůže program `extract.c`. Pro zkompilování programu a pro následné rozsekání dat do jednotlivých souborů po bitstreamech lze spustit `make`.

Pro testování bude požit [NIST Statistical Test Suite](https://github.com/arcetri/sts). Program `sts` ve složce `sts/` lze také připravit pomocí `make`.

## Testování

Testované sekvence bitů mají délku 5 400 000. Výchozí délka jednoho testovaného bitstreamu je 1024 \* 1024 a neměla by být kratší než 1 000 000. Ponechal jsem výchozí délku bitstreamu a nastavil jsem počet iterací na 5. Tedy 5 \* 1024 \* 1024 <= 5 400 000.

Testování tedy porbíhalo spuštením následujícího příkazu. Přepínač `-F a` nastavuje formát vstupních dat na ASCII '0'/'1'. Přepínač `-i 5` nastavuje 5 iterací.

```sh
./sts -i 5 -F a ../data-0.txt
```

Výsledky testování jsou uloženy ve složce `results/` pro každý bitstream zvlášť.

## Závěr

Očekávaný výsledek testování byl, že méně signifikantní bity budou splňovat testy náhodnosti, ale ne všechny testy náhodnosti proběhly pro tyto bity úspěšně.

Nastavení parametrů nehrálo významnou roli, protože první neúspěšný test, _Frequency Test_, má jen jeden vstupní parametr a to délku bitstreamu, která by měla být větší než 100 bitů.

Nejúspěšnější bitstream je druhý nejméně signifikantní bit, který měl úspěšnost 177 testů z celkových 188. Dalším úspěšným byl třetí nejméně signifikantní bit s úspěšností 160/188. Až potom byl ten nejméně signifikantní bit s úšpěšností 143/188.

Od 4. a výš signifikantního bitu je úspěšnost testů nízká a nelze považovat bitstreamy za náhodné. Od 6. a výš signifikantního bitu neuspěl už žádný test náhodnosti.
