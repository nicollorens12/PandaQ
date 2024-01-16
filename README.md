# Pràctica LP Q1 2023-2024 PandaQ
Autor: Nicolas Llorens Somalo

## Objectius
Aquesta pràctica consisteix en implementar un petit intèrpret anomenat PandaQ en Python3 amb les característiques principals següents:

- Entrada: subconjunt de consultes SQL (només consultes **SELECT**)

- Dades: arxius en format csv

- Tractament: llibreria pandas

- Interfície: Streamlit

## Plantejament
El meu objectiu personal en aquesta pràctica ha estat simplificar al màxim la gramàtica i alhora tindre un visitor també senzill que s'aprofites de tot el treball que ja fan el lexer i el parser, per tal de no haber de fer cap tractament de la entrada i només centrar el visitor en el que és realment la seva feina.

## Requisits

Per executar aquesta pràctica caldra ademes de Python tindre instalada la llibreria streamlit

```bash
pip install streamlit
```

Ademés, a partir de `pandaQ.g4` haurem de crear el lexer i parser corresponent, també necesitarem ajustar aquests perque treballin amb un visitador i siguin de Python. Tot això ho farem amb aquesta comanda:
```bash
antlr4 -Dlanguage=Python3 -no-listener -visitor exprs.g4
```

## Execució

Per executar el programa s'ha de escriure en terminal:
```bash
streamlit run pandaQ.py
```

El programa fa us de un arxiu `query.sql` que es crea automaticament per gestionar les consultes del usuari.
