# Factorial Analysis - Indice de Cidades Empreendedoras (ICE)

<img width="1400" height="375" alt="image" src="https://github.com/user-attachments/assets/d93acc96-8447-43d8-a7b3-ffaf388c27ef" />

## What is the ICE

The Entrepreneurial Cities Index (in Portuguese, Índice de Cidades Empreendedoras, or ICE) is a ranking that assesses how favorable the business environment is across the country’s municipalities. This initiative is developed by ENAP (Escola Nacional de Administração Pública - _Public Management National School_), in partnership with Endeavor, and has been published annually since 2014.

Originally, it only covered a few state capitals, but since 2020 it has expanded to include the 100 most populous cities, plus any that recently dropped out of that list—bringing the total to 101 cities for recent editions.

## What is this research for

As said before, the ICE only convers the 100 most populous cities, but this research aims to add all the 11 [Amplanorte](https://amplanorte.org.br/) cities into it. This includes:
- Mafra
- Bela Vista do Toldo
- Canoinhas
- Itaiópolis
- Irineópolis
- Major Vieira
- Monte Castelo
- Papanduva
- Porto União
- Três Barras
- Timbó Grande

## Methodology

1. Data from the 2023 ICE edition was collected using ENAP's own research references
2. Each determinant (Regulatory Environment, Infrastructure, Market, Access to Capital, Innovation, Human Capital, Entrepreneurial Culture) was normalized using StandardScaler
3. Factor Analysis was applied to calculate the subdeterminants and overall scores
4. Scores for the 11 Amplanorte cities were calculated using the same indicators to ensure comparability
5. Final ranking includes 101 + 11 cities

## Reproducing the Analysis

1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run: 

```sh
python convert.py \
python main.py \
python pca.py
```

4. You can now open the `calculated_indexes.csv` and can use it

## Contributing
Feel free to submit issues or pull requests
