# simulate_alert.py
# 🔁 Simulation d'alerte IA automatique toutes les 3 minutes
# ⛔ Stop après 5 alertes critiques

import random
import os

COUNTER_FILE = "alert_counter.txt"
ALERT_FILE = "alert.txt"
THRESHOLD = 0.8
MAX_ALERTS = 5

# Lire compteur actuel
if os.path.exists(COUNTER_FILE):
    with open(COUNTER_FILE, "r") as f:
        alert_count = int(f.read().strip())
else:
    alert_count = 0

# Simuler un nouveau score
risk_score = round(random.uniform(0, 1), 2)

# Si déjà trop d’alertes, on bloque
if alert_count >= MAX_ALERTS:
    with open(ALERT_FILE, "w") as f:
        f.write(f"🚨 STOP - Trop d’alertes critiques détectées ({alert_count})\n")
    print("🔁 Simulation arrêtée.")
else:
    with open(ALERT_FILE, "w") as f:
        if risk_score > THRESHOLD:
            alert_count += 1
            f.write(f"🔴 ALERTE CRITIQUE - Risk Score: {risk_score}\n")
        else:
            f.write(f"🟢 SITUATION NORMALE - Risk Score: {risk_score}\n")

    with open(COUNTER_FILE, "w") as f:
        f.write(str(alert_count))
