import os
from flask import Flask, render_template, send_file
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

app = Flask(__name__)

csv_path = "filtered_dataset.csv"
heatmap_path = "static/heatmap.png"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/heatmap")
def heatmap():
    # Ensure 'static' directory exists
    os.makedirs("static", exist_ok=True)  # ✅ Creates 'static/' if it doesn't exist

    # Load dataset
    df = pd.read_csv(csv_path)

    # Convert categorical columns into numeric form
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = pd.factorize(df[col])[0]  

    # Compute correlation matrix
    corr_matrix = df.corr()

    # Generate heatmap
    plt.figure(figsize=(10, 6))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)

    # Save heatmap
    plt.savefig(heatmap_path)
    plt.close()

    return send_file(heatmap_path, mimetype="image/png")

if __name__ == "__main__":
    app.run(debug=True)
