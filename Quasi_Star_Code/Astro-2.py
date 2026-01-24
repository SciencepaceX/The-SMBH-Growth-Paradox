import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import matplotlib
import matplotlib.ticker as ticker
from matplotlib.lines import Line2D

# 1. STYLE & FONT CONFIGURATION
plt.style.use('default')  # Reset to standard light theme
matplotlib.rcParams['font.family'] = 'serif'
matplotlib.rcParams['font.serif'] = ['Times New Roman'] + matplotlib.rcParams['font.serif']
matplotlib.rcParams['mathtext.fontset'] = 'stix'  # Matches math symbols to Times font
matplotlib.rcParams['axes.facecolor'] = 'white'
matplotlib.rcParams['figure.facecolor'] = 'white'

# 2. DATA (2026 Observations)
observed_bhs_data = [
    ["Gaia BH1", 9.6, 'cyan'], ["GS 2000+25 ", 5, 'cyan'], ["4U 1543-475", 9.4, 'cyan'], ["Cygnus X-3", 2.4, 'cyan'],
    ["Gaia BH3", 33, 'cyan'], ["Cygnus X-1", 21.2, 'cyan'], ["1E 1740.7-2942", 4.5, 'cyan'], ["A0620-00", 6, 'cyan'],
    ["GRO J0422+32", 2.1, 'cyan'], ["GRO J1655-40", 7.02, 'cyan'], ["GRS 1915+105", 12.4, 'cyan'],
    ["SS 433", 2.9, 'cyan'], ["V404 Cygni", 9, 'cyan'], ["XTE J1550-564", 10, 'cyan'], ["XTE J1650-500", 9.7, 'cyan'],
    ["GW190521", 142, 'orange'], ["GW231123", 137, 'orange'], ["HLX-1", 500, 'orange'], ["M82 X-1", 300, 'orange'],
    ["Sagittarius A*", 4.3e6, 'magenta'], ["NGC 7314", 8.7e5, 'magenta'], ["M87*", 6.5e9, 'magenta'],
    ["1ES 2344+514", 1e9, 'magenta'], ["NGC 7052", 3e9, 'magenta'], ["NGC 6251", 6e8, 'magenta'],
    ["OJ 287 BC", 1.5e8, 'magenta'], ["Fornax A", 1.4e8, 'magenta'], ["NGC 4486b", 5e8, 'magenta'],
    ["Pōniuāʻena", 1.5e9, 'magenta'], ["RX J1131-1231", 1.3e8, 'magenta'], ["Q0906+6930", 2e9, 'magenta'],
    ["Caldwell 52", 1.3e8, 'magenta'], ["NGC 4596", 7.8e7, 'magenta'], ["NGC 4564", 5.6e7, 'magenta'],
    ["NGC 4473", 1e8, 'magenta'], ["NGC 4261", 1.62e9, 'magenta'], ["M31*", 2.25e8, 'magenta'],
    ["M81*", 7e8, 'magenta'], ["M104*", 1e9, 'magenta'],
    ["TON 618", 6.6e10, 'red'], ["Phoenix A", 1.0e11, 'red'], ["Caldwell 35", 2.1e10, 'red'],
    ["S5 0014+81", 4e10, 'red'], ["OJ 287", 18.35e9, 'red'],
    ["APM 08279+5255", 1.65e10, 'red'], ["4C +37.11", 15e9, 'red']
]
names, masses, colors = zip(*observed_bhs_data)

# 3. CREATE PLOT
fig, ax = plt.subplots(figsize=(10, 7))

# Smoothed Density Trend (KDE)
sns.kdeplot(masses, log_scale=True, bw_adjust=0.28, color='black',
            fill=True, alpha=0.08, ax=ax, label='Population Trend')

# Scatter Points
y_pos = 0.05
ax.scatter(masses, [y_pos]*len(masses), color=colors, s=110, edgecolors='black', linewidth=0.8, zorder=5)

# 4. ANNOTATIONS
for i, name in enumerate(names):
    stagger = 28 if i % 2 == 0 else 48
    # Escape underscores for LaTeX-friendliness
    safe_name = name.replace("_", r"\_")
    ax.annotate(f"{safe_name}\n{masses[i]:.1e} $M_\odot$",
                 xy=(masses[i], y_pos), xytext=(0, stagger),
                 textcoords='offset points', ha='center', va='bottom',
                 fontsize=8, color=colors[i], fontweight='bold',
                 arrowprops=dict(arrowstyle='->', color=colors[i], lw=0.8, alpha=0.5),
                 bbox=dict(boxstyle="round,pad=0.3", fc=(1,1,1,0.8), ec='none', alpha=0.7))

# 5. AXIS FORMATTING
ax.set_xscale('log')
ax.set_xlim(1, 2e11)
ax.set_ylim(-0.02, 0.28)
ax.set_xlabel(r"Mass in Solar Masses ($M_\odot$)", fontsize=14, labelpad=12)
ax.set_ylabel("Relative Frequency (Log Scale)", fontsize=12)
ax.set_title("Mass Distribution of Observed Black Holes (2026)", fontsize=18, fontweight='bold')

# Ticks and Grid
ax.xaxis.set_major_locator(ticker.LogLocator(base=10.0, numticks=13))
ax.grid(True, which="major", ls="--", alpha=0.2, color='gray')
ax.tick_params(axis='both', which='major', labelsize=10)

# 6. LEGEND
legend_elements = [
    Line2D([0], [0], marker='o', color='w', label='Stellar',
           markerfacecolor='cyan', markersize=10, markeredgecolor='black'),
    Line2D([0], [0], marker='o', color='w', label='Intermediate/Mergers',
           markerfacecolor='orange', markersize=10, markeredgecolor='black'),
    Line2D([0], [0], marker='o', color='w', label='Supermassive',
           markerfacecolor='magenta', markersize=10, markeredgecolor='black'),
    Line2D([0], [0], marker='o', color='w', label='Ultramassive',
           markerfacecolor='red', markersize=10, markeredgecolor='black')
]
ax.legend(handles=legend_elements, loc='upper left', frameon=True,
          facecolor='white', edgecolor='gray', fontsize=10)

# 7. EXPORT
plt.tight_layout()
plt.savefig("bh_mass_distribution.pdf", bbox_inches='tight', dpi=600)
print("File 'bh_mass_distribution.pdf' has been generated with white background and Times New Roman.")
plt.show()
