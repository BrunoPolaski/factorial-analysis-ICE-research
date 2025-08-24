## Idiomas/Languages

<table>
    <tr>
        <td>
            Português - Brasil
        </td>
    </tr>
    <tr>
        <td>
            English -
            <a href="https://github.com/BrunoPolaski/factorial-analysis-ICE-research/blob/main/README.en.md">
                [See here]
            </a>
        </td>
    </tr>
</table>
    

# Análise Fatorial - Índice de Cidades Empreendedoras (ICE)

<img width="1400" height="375" alt="image" src="https://github.com/user-attachments/assets/d93acc96-8447-43d8-a7b3-ffaf388c27ef" />

## O que é o ICE

O Índice de Cidades Empreendedoras (ICE) é um ranking que avalia quão favorável é o ambiente de negócios nos municípios brasileiros.  
A iniciativa é desenvolvida pela **ENAP (Escola Nacional de Administração Pública)**, em parceria com a **Endeavor**, e vem sendo publicada anualmente desde 2014.  

Originalmente, o índice abrangia apenas algumas capitais estaduais, mas desde 2020 passou a incluir as 100 cidades mais populosas do país, além de eventuais municípios que tenham deixado recentemente essa lista — totalizando **101 cidades** nas edições mais recentes.  

## Objetivo desta pesquisa

Como mencionado, o ICE considera apenas as 100 cidades mais populosas. Entretanto, esta pesquisa busca incluir também os **11 municípios da [Amplanorte](https://amplanorte.org.br/)**, sendo eles:  

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

## Metodologia

1. Os dados da edição 2023 do ICE foram coletados a partir das referências de pesquisa da própria ENAP  
2. Cada determinante (**Ambiente Regulatório, Infraestrutura, Mercado, Acesso a Capital, Inovação, Capital Humano, Cultura Empreendedora**) foi normalizado utilizando **StandardScaler**  
3. Aplicou-se a **Análise Fatorial** para calcular os subdeterminantes e os _scores_ gerais  
4. Os _scores_ das 11 cidades da Amplanorte foram calculados utilizando os mesmos indicadores, garantindo comparabilidade  
5. O ranking final inclui as **101 + 11 cidades**  

## Reproduzindo a Análise

1. Clone este repositório  
2. Instale as dependências:  

```sh
pip install -r requirements.txt
```
3. Execute:
```sh
python convert.py \
python main.py \
python pca.py
```
4. Agora você pode abrir o arquivo `fa_scores_by_city.csv` e utilizá-lo; ele contém todos os scores de fatores de cada cidade. Para calcular o score final, o cálculo é simples:

```
score_<city> = city_factor_1 + city_factor_2 + city_factor_3 + 6
```
