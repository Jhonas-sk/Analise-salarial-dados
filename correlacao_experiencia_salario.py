# ================================================
# ANÁLISE 3 — CORRELAÇÃO EXPERIÊNCIA x SALÁRIO
# Projeto: Análise Exploratória de Dados Salariais
# Autor: Jhonas Stankowitsch Martins
# Ferramentas: Python | Pandas | Matplotlib | NumPy
# ================================================

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ── 1. Carregar dados ──
df = pd.read_csv('dataset.csv')

# ── 2. Calcular correlação ──
corr         = df[['salary_in_usd', 'years_of_experience']].corr().iloc[0, 1]
media_por_exp = df.groupby('years_of_experience')['salary_in_usd'].mean()
std_por_exp   = df.groupby('years_of_experience')['salary_in_usd'].std()

print("=" * 60)
print("   CORRELAÇÃO: ANOS DE EXPERIÊNCIA x SALÁRIO")
print("=" * 60)
print(f"  Coeficiente de Pearson: {corr:.4f}")
print("\n  INTERPRETAÇÃO:")
print("  ✅ Correlação POSITIVA MODERADA")
print("  ➡  Maior experiência tende a estar associada a salários mais altos.")
print("  ⚠  Correlação NÃO é causalidade.")
print("=" * 60)

# ── 3. Visualização ──
fig, axes = plt.subplots(1, 3, figsize=(18, 6))
fig.suptitle('Correlação: Anos de Experiência x Salário', fontsize=15, fontweight='bold')

ax1 = axes[0]
ax1.scatter(df['years_of_experience'], df['salary_in_usd'], alpha=0.25, color='steelblue', s=15)
z  = np.polyfit(df['years_of_experience'], df['salary_in_usd'], 1)
xs = np.linspace(1, 10, 100)
ax1.plot(xs, np.poly1d(z)(xs), color='red', linewidth=2, label=f'Tendência (r={corr:.2f})')
ax1.set_xlabel('Anos de Experiência')
ax1.set_ylabel('Salário (USD)')
ax1.set_title(f'Scatter — r = {corr:.4f}')
ax1.legend()
ax1.yaxis.grid(True, linestyle='--', alpha=0.4)

ax2 = axes[1]
anos   = media_por_exp.index
medias = media_por_exp.values
stds   = std_por_exp.values
bars = ax2.bar(anos, medias, color='steelblue', alpha=0.8, edgecolor='white', zorder=3)
ax2.errorbar(anos, medias, yerr=stds, fmt='none', color='black', capsize=4, linewidth=1, alpha=0.5)
ax2.set_xlabel('Anos de Experiência')
ax2.set_ylabel('Média Salarial (USD)')
ax2.set_title('Média ± Desvio Padrão')
ax2.yaxis.grid(True, linestyle='--', alpha=0.4)
for bar, val in zip(bars, medias):
    ax2.text(bar.get_x() + bar.get_width()/2, val + 3000,
             f'${val/1000:.0f}k', ha='center', fontsize=8, fontweight='bold')

ax3 = axes[2]
grupos = [df[df['years_of_experience'] == a]['salary_in_usd'].values
          for a in sorted(df['years_of_experience'].unique())]
ax3.boxplot(grupos, patch_artist=True,
            positions=sorted(df['years_of_experience'].unique()),
            boxprops=dict(facecolor='steelblue', alpha=0.6),
            medianprops=dict(color='orange', linewidth=2),
            flierprops=dict(marker='o', color='red', alpha=0.3, markersize=3))
ax3.set_xlabel('Anos de Experiência')
ax3.set_ylabel('Salário (USD)')
ax3.set_title('Boxplot por Anos de Experiência')
ax3.yaxis.grid(True, linestyle='--', alpha=0.4)

plt.tight_layout()
plt.savefig('correlacao_experiencia_salario.png', dpi=150, bbox_inches='tight')
plt.show()
