# simulate_alert.py
# ─────────────────────────────────────────────────────────────────────────────
# 🔎 Simulation d'une alerte IA basée sur un score de risque
# ─────────────────────────────────────────────────────────────────────────────

import random

# Simuler un score de risque IA
risk_score = round(random.uniform(0, 1), 2)

# Définir le seuil critique
threshold = 0.8

# Simuler une alerte si le seuil est dépassé
with open("alert.txt", "w") as f:
    if risk_score > threshold:
        f.write(f"🔴 ALERTE CRITIQUE - Risk Score: {risk_score}\n")
    else:
        f.write(f"🟢 SITUATION NORMALE - Risk Score: {risk_score}\n")
