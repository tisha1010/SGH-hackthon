import numpy as np
import matplotlib.pyplot as plt

def generate_gauge_chart(bandwidth):
    fig, ax = plt.subplots(figsize=(4, 2), subplot_kw={'projection': 'polar'})

    # Define gauge parameters
    min_val, max_val = 0, 20  # Bandwidth range
    theta_range = np.linspace(np.pi, 0, 100)  # Arc from left to right
    bandwidth_angle = (1 - (bandwidth / max_val)) * np.pi  # Convert bandwidth to angle

    # Draw background arc (gray)
    ax.plot(theta_range, [1] * len(theta_range), color="lightgray", linewidth=10)

    # Draw active bandwidth arc (purple)
    active_range = np.linspace(np.pi, bandwidth_angle, 50)
    ax.plot(active_range, [1] * len(active_range), color="purple", linewidth=10)

    # Draw needle
    ax.plot([bandwidth_angle, bandwidth_angle], [0, 1], color="black", linewidth=3)

    # Remove grid, labels, and extra elements
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines['polar'].set_visible(False)

    # Add text for bandwidth value
    plt.text(0, -0.4, f"{bandwidth:.2f} Mbps", fontsize=12, ha="center")
    plt.title("Network Bandwidth", fontsize=10, pad=20)

    # Save the image
    plt.savefig("static/bandwidth.png", bbox_inches="tight", transparent=True)
    plt.close()
