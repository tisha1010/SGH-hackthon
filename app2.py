import matplotlib
matplotlib.use("Agg")  # Fix GUI issue for Matplotlib in Flask

from flask import Flask, render_template
import matplotlib.pyplot as plt
import numpy as np
import os

app = Flask(__name__)

# Function to generate the gauge chart
def generate_availability_chart(availability_rate):
    fig, ax = plt.subplots(figsize=(4, 2.5), subplot_kw={'projection': 'polar'})

    min_val, max_val = 0, 100  # Percentage range
    theta_range = np.linspace(np.pi, 0, 100)  # Half-circle arc
    availability_angle = (1 - (availability_rate / max_val)) * np.pi  # Convert to angle

    # Draw background arc
    ax.plot(theta_range, [1] * len(theta_range), color="lightcoral", linewidth=10)

    # Draw active availability arc
    active_range = np.linspace(np.pi, availability_angle, 50)
    ax.plot(active_range, [1] * len(active_range), color="black", linewidth=10)

    # Draw needle
    ax.plot([availability_angle, availability_angle], [0, 1], color="darkblue", linewidth=4)

    # Remove extra elements
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines['polar'].set_visible(False)

    # Add text for percentage
    plt.text(0, -0.3, f"{availability_rate:.2f}%", fontsize=12, ha="center", fontweight="bold")
    plt.title("Network Availability Rate", fontsize=10, pad=20)

    # Ensure the "static" directory exists
    if not os.path.exists("static"):
        os.makedirs("static")

    # Save image
    plt.savefig("static/availability_rate.png", bbox_inches="tight", transparent=True)
    plt.close()

@app.route("/")
def dashboard():
    availability_rate = 95.04  # Example value
    generate_availability_chart(availability_rate)
    return render_template("index2.html", availability_rate=availability_rate)  # Changed to index2.html

if __name__ == "__main__":
    app.run(debug=True)
