# 📊 Análise Exploratória de Dados Salariais

Projeto de análise exploratória de um dataset internacional de salários na área de tecnologia e dados.

## 🎯 Objetivo

Extrair insights sobre distribuição salarial, diferenças regionais e a relação entre experiência e remuneração, utilizando Python e bibliotecas de análise de dados.

## 🛠 Ferramentas Utilizadas

- Python 3
- Pandas
- Matplotlib
- Seaborn
- NumPy

## 📁 Estrutura do Projeto

```
analise-salarial-dados/
│
├── analise_salario.py                  # Análise de distribuição salarial
├── media_salario_regiao.py             # Média salarial por região
├── correlacao_experiencia_salario.py   # Correlação experiência x salário
│
├── distribuicao_salario.png            # Histograma + Boxplot
├── media_salario_regiao.png            # Barras + Pizza por região
├── correlacao_experiencia_salario.png  # Scatter + Barras + Boxplot
│
└── README.md
```

## 📈 Análises Realizadas

### 1. Distribuição Salarial
- Cálculo de média, mediana, desvio padrão e assimetria
- Identificação de outliers via Boxplot
- **Conclusão:** Média ($137.570) > Mediana ($135.000) → assimetria à direita causada por salários extremos

### 2. Média Salarial por Região
- Agrupamento por região com cálculo de média e percentual
- **Conclusão:** Américas lideram com $150.915 de média — praticamente o dobro da Europa e Oceania

### 3. Correlação: Experiência x Salário
- Coeficiente de Pearson: **r = 0.41** (correlação positiva moderada)
- **Conclusão:** Maior experiência tende a estar associada a salários mais altos, porém a correlação não é perfeita nem implica causalidade

## 💡 Principais Insights

- Profissionais nas **Américas** ganham em média 3x mais que na Ásia e África
- A **experiência influencia o salário**, mas outros fatores como região e cargo têm peso significativo
- Existem **outliers relevantes** acima de $300k que distorcem a média geral

## 👤 Autor

**Jhonas Stankowitsch**  
Analista de Dados | Python • Power BI • Pandas  
Salvador, BA — Brasil
