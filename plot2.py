import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r'C:\Users\Dung\Desktop\DataPY.csv', delimiter=';')

plt.figure(figsize=(10, 6))
colors = ['#EE2C2C', '#00F5FF', '#CD853F', '#00CD00']

for rating, color in zip(df['Rating_economy'].unique(), colors):
    subset = df[df['Rating_economy'] == rating]
    sns.kdeplot(subset['GDP_growth'], fill=True, color=color, alpha=0.4, linewidth=1.4,
                label=f'Rating economy: {rating}')

plt.title('Distribution of GDP growth rate according to rating economy\nData Source: World Bank',
          fontweight='bold', color='#FF5733', fontsize=22)
plt.xlabel('GDP Growth (%)', fontsize=16, color='#00AA00', fontweight='bold')
plt.ylabel('Density', fontsize=16, color='#00AA00', fontweight='bold')
plt.legend(title='Rating economy')
plt.minorticks_on()
plt.grid(True, which='both', linestyle='--', alpha=0.8)
plt.tight_layout()
plt.show()