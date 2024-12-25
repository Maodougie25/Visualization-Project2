import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
try:
    data = pd.read_csv("Final-50-stocks.csv")  # Replace with your dataset name
    print("Dataset loaded successfully!")
except FileNotFoundError:
    print("Error: The file was not found.")
    exit()

# Display basic dataset information
print("\nDataset Info:")
print(data.info())
print("\nFirst Few Rows:")
print(data.head())

# --- HISTOGRAM ---
plt.figure(figsize=(10, 6))
sns.histplot(data['WIPRO'], kde=True, bins=30, color='blue')  # Replace 'WIPRO' with a numeric column name
plt.title("Histogram of WIPRO Stock Prices")
plt.xlabel("Stock Price")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("histogram_stock_price.png")
plt.show()

# --- BOXPLOT ---
plt.figure(figsize=(10, 6))
sns.boxplot(data=data[['TATASTEEL', 'RELIANCE', 'WIPRO']])  # Replace column names with your dataset's numeric columns
plt.title("Boxplot of Selected Stocks")
plt.ylabel("Stock Prices")
plt.tight_layout()
plt.savefig("boxplot_stock_prices.png")
plt.show()

# --- SCATTERPLOT WITH REGRESSION LINE ---
plt.figure(figsize=(10, 6))
sns.regplot(x=data['TATASTEEL'], y=data['RELIANCE'], scatter_kws={'alpha':0.6})
plt.title("Scatterplot with Regression Line (TATASTEEL vs RELIANCE)")
plt.xlabel("TATASTEEL Stock Price")
plt.ylabel("RELIANCE Stock Price")
plt.tight_layout()
plt.savefig("scatterplot_regression.png")
plt.show()