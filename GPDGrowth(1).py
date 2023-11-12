import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

DFP = pd.read_csv("C:\\Users\\Dung\\Desktop\\DataPy.csv", delimiter=';')

DFP['GDP_growth_diff'] = DFP.groupby('Country')['GDP_growth'].diff()

# Calculate the median GDP growth for each country
median_order = DFP.groupby('Country')['GDP_growth'].median().sort_values()

# Sort the DataFrame based on the median order
DFP_sorted = DFP.set_index('Country').loc[median_order.index].reset_index()

# Create the plot with the reordered boxplots
plt.figure(figsize=(10, 4))
sns.boxplot(data=DFP_sorted, x="Country", y="GDP_growth", showfliers=False, palette="tab10")

# Set the plot title and labels
plt.title("GDP Growth Rates in Southeast Asia\nData Source: World Bank", fontweight='bold', color='#FF5733', fontsize=22)
plt.xlabel("Country", fontsize=16, color='#00AA00', fontweight='bold')
plt.ylabel("GDP Growth (%)", fontsize=16, color='#00AA00', fontweight='bold')
plt.xticks(rotation=45, ha="right",fontsize=12)
plt.yticks(fontsize=12)
plt.minorticks_on()

# Display the plot
plt.show()
