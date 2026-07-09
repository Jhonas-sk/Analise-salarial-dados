# ================================================
# ANÁLISE 2 — MÉDIA SALARIAL POR REGIÃO
# Projeto: Análise Exploratória de Dados Salariais
# Autor: Jhonas Stankowitsch Martins
# Ferramentas: Python | Pandas | Matplotlib
# ================================================

import pandas as pd
import matplotlib.pyplot as plt

# ── 1. Carregar dados ──
df = pd.read_csv('dataset.csv')

# ── 2. Agrupar por região e calcular média ──
media_regiao = (
    df.groupby('region')['salary_in_usd']
    .mean().round(2).reset_index()
    .rename(columns={'salary_in_usd': 'media_salario'})
    .sort_values('media_salario', ascending=False)
)
media_regiao['percentual'] = (
    media_regiao['media_salario'] / media_regiao['media_salario'].sum() * 100
).round(2)

print("=" * 50)
print("   MÉDIA SALARIAL POR REGIÃO")
print("=" * 50)
print(media_regiao.to_string(index=False))
print("=" * 50)
maior = media_regiao.iloc[0]
print(f"\n✅ Maior salário médio: {maior['region']} — ${maior['media_salario']:,.2f}")

# ── 3. Visualização ──
cores = ['#2ecc71' if r == maior['region'] else '#5b8dee' for r in media_regiao['region']]

fig, axes = plt.subplots(1, 2, figsize=(16, 6))
fig.suptitle('Média Salarial por Região', fontsize=15, fontweight='bold')

ax1 = axes[0]
bars = ax1.barh(media_regiao['region'], media_regiao['media_salario'], color=cores, edgecolor='white')
ax1.set_xlabel('Média Salarial (USD)')
ax1.set_title('Ranking por Região')
ax1.xaxis.grid(True, linestyle='--', alpha=0.5)
ax1.set_axisbelow(True)
for bar, val in zip(bars, media_regiao['media_salario']):
    ax1.text(bar.get_width() + 1000, bar.get_y() + bar.get_height()/2,
             f'${val:,.0f}', va='center', fontsize=10, fontweight='bold')
ax1.invert_yaxis()

ax2 = axes[1]
explode = [0.05 if r == maior['region'] else 0 for r in media_regiao['region']]
ax2.pie(media_regiao['media_salario'], labels=media_regiao['region'],
        autopct='%1.1f%%', explode=explode,
        colors=['#2ecc71','#5b8dee','#e67e22','#e74c3c','#9b59b6'], startangle=140)
ax2.set_title('Participação Percentual por Região')

plt.tight_layout()
plt.savefig('media_salario_regiao.png', dpi=150, bbox_inches='tight')
plt.show()
