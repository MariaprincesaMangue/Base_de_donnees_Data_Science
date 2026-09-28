import pandas as pd
import matplotlib.pyplot as plt

# 1. Lecture du fichier Excel (en-tête à la ligne 21, colonnes B à E)
df = pd.read_excel(
    "taux_chomage_maroc.xlsx",
    sheet_name="Trimestriel",
    header=20,
    usecols="B:E",
)

# 2. Nettoyage : on retire la ligne "Source", les espaces et on trie par date
df["Trimestre"] = df["Trimestre"].astype(str).str.strip()
df = df[df["Trimestre"].str.match(r"^\d{4}T[1-4]$")].copy()
df["Date"] = pd.PeriodIndex(df["Trimestre"].str.replace("T", "Q"), freq="Q").to_timestamp()
df = df.sort_values("Date")

# 3. Graphique
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(df["Date"], df["Urbain"], label="Urbain", color="#d62728", linewidth=2)
ax.plot(df["Date"], df["Rural"], label="Rural", color="#2ca02c", linewidth=2)
ax.plot(df["Date"], df["Ensemble"], label="Ensemble", color="#1f77b4", linewidth=2.5)

ax.set_title("Taux de chômage au Maroc par trimestre (2006 - 2025)", fontsize=14, fontweight="bold")
ax.set_xlabel("Trimestre")
ax.set_ylabel("Taux de chômage (%)")
ax.grid(True, linestyle="--", alpha=0.4)
ax.legend()
fig.text(0.01, 0.01, "Source : Enquête nationale sur l'emploi, Haut Commissariat au Plan",
         fontsize=8, color="gray")

plt.tight_layout(rect=(0, 0.03, 1, 1))
plt.savefig("graphique_chomage.png", dpi=150)
plt.show()

