from flask import Flask, render_template
from utils import generate_gauge_chart

app = Flask(__name__)

@app.route("/")
def dashboard():
    bandwidth_value = 10.28  # Replace with real-time data
    generate_gauge_chart(bandwidth_value)  # Generates the gauge chart and saves it in "static/"
    return render_template("index1.html")

if __name__ == "__main__":
    app.run(debug=True)
