import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Setup Font
plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = ["Times New Roman"] + plt.rcParams["font.serif"]

# Mass range (Log10 Solar Masses)
x = np.linspace(1, 11, 400)

# 1. Stochastic Model (Pure Decay)
y_stochastic = 10 * np.exp(-0.8 * (x - 1))

# 2. Standard Hierarchical Model (Light Seeds)
y_standard = 8 * np.exp(-0.5 * (x - 1))  # Base decay
# Add the IMBH Valley and SMBH Peak
y_standard += 4 * np.exp(-0.8 * (x - 7.5)**2)  # SMBH Peak at 10^7.5
y_standard[ (x > 2.5) & (x < 5.5) ] *= 0.4 # Deepen the valley

# Normalize slightly for visual clarity
y_stochastic = np.maximum(y_stochastic, 0.01)
y_standard = np.maximum(y_standard, 0.01)

plt.figure(figsize=(12, 7))

# Plot the curves (Heavy Seed removed as requested)
plt.plot(x, y_stochastic, color='red', linewidth=2.5, linestyle=':', label='Stochastic Growth (No Centers)')
plt.plot(x, y_standard, color='black', linewidth=3, label='Standard Hierarchical (Light Seeds)')

# 3. The Eddington Limit "Wall"
plt.axvspan(9, 11, color='gray', alpha=0.2, label='Eddington Time Constraint (Age of Universe)')
plt.axvline(x=9, color='darkgray', linestyle='-', linewidth=1)
plt.text(9.1, 8, 'The "Eddington Wall"\n(Too big for Light Seeds)', fontsize=10, color='dimgray', rotation=90)

# Labels and Styling
plt.title('Black Hole Mass Distribution: Stochastic vs. Standard Hierarchical Models', fontsize=18, fontweight='bold')
plt.xlabel('Black Hole Mass ($M_{\odot}$)', fontsize=14)
plt.ylabel('Relative Frequency (~LogScale)', fontsize=14)

# X-axis
xticks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
xtick_labels = ['$10^1$', '$10^2$', '$10^3$', '$10^4$', '$10^5$', '$10^6$', '$10^7$', '$10^8$', '$10^9$', '$10^{10}$', '$10^{11}$']
plt.xticks(xticks, xtick_labels, fontsize=12)
plt.yticks([])

# Annotations for context
plt.text(1.2, 9.5, 'Stellar Remnants', fontsize=11, fontweight='bold')
plt.text(3.5, 0.5, 'IMBH "Valley"', color='black', fontsize=11, fontweight='bold')
plt.text(7.5, 4.5, 'SMBH Stabilization', color='black', fontsize=11, fontweight='bold')

plt.grid(True, linestyle='--', alpha=0.3)
plt.legend(loc='upper right', fontsize=12)
plt.tight_layout()

# Save as PDF
plt.savefig('bh_mass_distribution_final.pdf')
plt.savefig('bh_mass_distribution_final.png') # Saving png as well for display