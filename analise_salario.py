# ================================================
# ANÁLISE 1 — DISTRIBUIÇÃO SALARIAL
# Projeto: Análise Exploratória de Dados Salariais
# Autor: Jhonas Stankowitsch Martins
# Ferramentas: Python | Pandas | Matplotlib
# ================================================

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# ── 1. Carregar dados ──
df = pd.read_csv('dataset.csv')

# ── 2. Estatísticas descritivas ──
salario    = df['salary_in_usd']
media      = salario.mean()
mediana    = salario.median()
desvio     = salario.std()
assimetria = salario.skew()

print("=" * 50)
print("   DISTRIBUIÇÃO: salary_in_usd")
print("=" * 50)
print(f"  Média:         $ {media:,.2f}")
print(f"  Mediana:       $ {mediana:,.2f}")
print(f"  Desvio Padrão: $ {desvio:,.2f}")
print(f"  Mínimo:        $ {salario.min():,.2f}")
print(f"  Máximo:        $ {salario.max():,.2f}")
print(f"  Assimetria:      {assimetria:.4f}")
print("=" * 50)

if media > mediana:
    print("\n✅ Média > Mediana → Assimetria à DIREITA")
    print("   Salários altos (outliers) puxam a média para cima.")

# ── 3. Visualização ──
fig, axes = plt.subplots(1, 2, figsize=(16, 6))
fig.suptitle('Distribuição de Salários (salary_in_usd)', fontsize=15, fontweight='bold')

ax1 = axes[0]
ax1.hist(salario, bins=50, color='steelblue', edgecolor='white', alpha=0.85)
ax1.axvline(media,   color='red',    linestyle='--', linewidth=2, label=f'Média: ${media:,.0f}')
ax1.axvline(mediana, color='orange', linestyle='--', linewidth=2, label=f'Mediana: ${mediana:,.0f}')
ax1.set_title('Histograma com Média e Mediana')
ax1.set_xlabel('Salário (USD)')
ax1.set_ylabel('Frequência')
ax1.legend()
ax1.yaxis.grid(True, linestyle='--', alpha=0.5)
ax1.set_axisbelow(True)

ax2 = axes[1]
ax2.boxplot(salario, vert=False, patch_artist=True,
            boxprops=dict(facecolor='steelblue', color='navy'),
            medianprops=dict(color='orange', linewidth=2.5),
            flierprops=dict(marker='o', color='red', alpha=0.4, markersize=4))
ax2.axvline(media, color='red', linestyle='--', linewidth=2)
ax2.set_title('Boxplot - Identificação de Outliers')
ax2.set_xlabel('Salário (USD)')
patch_med = mpatches.Patch(color='orange', label=f'Mediana: ${mediana:,.0f}')
patch_avg = mpatches.Patch(color='red',    label=f'Média: ${media:,.0f}')
ax2.legend(handles=[patch_med, patch_avg])

plt.tight_layout()
plt.savefig('distribuicao_salario.png', dpi=150, bbox_inches='tight')
plt.show()
