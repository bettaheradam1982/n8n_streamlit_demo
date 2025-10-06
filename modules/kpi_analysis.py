import matplotlib.pyplot as plt
import os
import json
from datetime import datetime

def plot_daily_kpi():
    data_file = "data/appointments.json"
    if not os.path.exists(data_file):
        return None
    with open(data_file, "r", encoding="utf-8") as f:
        appointments = json.load(f)

    if not appointments:
        return None

    priorities = [a.get("priority", "Normal") for a in appointments]
    counts = {}
    for p in priorities:
        counts[p] = counts.get(p, 0) + 1

    fig, ax = plt.subplots(figsize=(5, 3))
    ax.bar(counts.keys(), counts.values())
    ax.set_title(f"KPI - Terminprioritäten ({datetime.now().date()})")
    ax.set_xlabel("Priorität")
    ax.set_ylabel("Anzahl")

    os.makedirs("data/reports", exist_ok=True)
    path = f"data/reports/kpi_{datetime.now().strftime('%Y%m%d')}.png"
    plt.tight_layout()
    plt.savefig(path)
    plt.close()
    return path
