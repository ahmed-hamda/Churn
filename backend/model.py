# model.py
# ==========================
# Fichier responsable de :
# - Charger le modèle ML et le scaler
# - Fournir des fonctions de prédiction
# - Fournir des statistiques pour le dashboard

import joblib
import numpy as np
import pandas as pd
from pathlib import Path

# Dossier courant du projet
BASE_DIR = Path(__file__).resolve().parent

# Paths vers les fichiers sauvegardés (à adapter si besoin)
MODEL_PATH = BASE_DIR / "models" / "random_forest_tuned.joblib"
SCALER_PATH = BASE_DIR / "models" / "scaler.joblib"

# Les features dans le même ordre que X.columns lors de l'entraînement
FEATURE_NAMES = [
    'CreditScore',
    'Gender',
    'Age',
    'Tenure',
    'Balance',
    'NumOfProducts',
    'HasCrCard',
    'IsActiveMember',
    'EstimatedSalary',
    'Geography_Germany',
    'Geography_Spain'
]

# Chargement global (une seule fois au démarrage)
try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    print(f"[ERREUR] Impossible de charger le modèle: {e}")
    model = None

try:
    scaler = joblib.load(SCALER_PATH)
except Exception as e:
    print(f"[ERREUR] Impossible de charger le scaler: {e}")
    scaler = None


# -----------------------------
# 1. Statistiques pour dashboard
# -----------------------------
def get_dashboard_stats():
    """
    Renvoie un dictionnaire avec quelques statistiques
    que le front Angular pourra afficher sous forme de cards / charts.
    
    ➜ À ADAPTER avec tes vraies valeurs (issues de ton notebook).
    """
    # Exemple de stats "mock" à remplacer par les tiennes
    stats_globales = {
        "nb_clients": 10000,
        "nb_features": len(FEATURE_NAMES),
        "taux_churn": 20.35,   # en %
    }

    # Résultats de comparaison des modèles (baseline)
    # Remplace ces chiffres par ceux de ton comparison_df
    models_baseline = [
        {
            "nom": "Logistic Regression",
            "accuracy": 0.84,
            "f1": 0.56,
            "roc_auc": 0.88
        },
        {
            "nom": "Random Forest",
            "accuracy": 0.86,
            "f1": 0.58,
            "roc_auc": 0.90
        },
        {
            "nom": "XGBoost",
            "accuracy": 0.87,
            "f1": 0.59,
            "roc_auc": 0.91
        },
    ]

    # Meilleur modèle après tuning (tuned_comparison_df)
    best_model = {
        "nom": "Random Forest (Tuned)",
        "accuracy": 0.89,
        "f1": 0.60,
        "roc_auc": 0.93
    }

    # Exemple de features importantes (à partir de all_feature_scores)
    top_features = [
        {"feature": "Age", "score": 25.3},
        {"feature": "NumOfProducts", "score": 18.7},
        {"feature": "IsActiveMember", "score": 16.2},
        {"feature": "Balance", "score": 14.9},
        {"feature": "CreditScore", "score": 12.4},
    ]

    return {
        "global": stats_globales,
        "models_baseline": models_baseline,
        "best_model": best_model,
        "top_features": top_features,
    }


# -----------------------------
# 2. Prédiction churn
# -----------------------------
def predict_churn(features_dict):
    """
    Reçoit un dict Python avec les features du client
    et renvoie la prédiction (0/1) + probabilité.
    
    features_dict doit contenir toutes les clés de FEATURE_NAMES.
    Exemple pour France :
      Geography_Germany = 0
      Geography_Spain = 0
    """
    if model is None or scaler is None:
        raise RuntimeError("Modèle ou scaler non chargé.")

    # Vérifier que toutes les features sont présentes
    missing = [f for f in FEATURE_NAMES if f not in features_dict]
    if missing:
        raise ValueError(f"Features manquantes: {missing}")

    # Construire un DataFrame dans le bon ordre
    sample_df = pd.DataFrame([features_dict])[FEATURE_NAMES]

    # Appliquer le scaler
    sample_scaled = scaler.transform(sample_df)

    # Prédiction
    pred = model.predict(sample_scaled)[0]
    proba = model.predict_proba(sample_scaled)[0][1]

    # On renvoie aussi le label texte (Yes/No)
    label = "Churn" if int(pred) == 1 else "No Churn"

    return {
        "prediction": int(pred),
        "label": label,
        "probability": float(proba)
    }
