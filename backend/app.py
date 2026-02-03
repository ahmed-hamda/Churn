# app.py
from flask import Flask, jsonify, request
from flask_cors import CORS
from flasgger import Swagger
from model import get_dashboard_stats, predict_churn, FEATURE_NAMES

app = Flask(__name__)
CORS(app)

# Configuration Swagger de base
swagger_template = {
    "info": {
        "title": "Churn Prediction API",
        "description": "API Flask pour la prédiction du churn et l'affichage de statistiques.",
        "version": "1.0.0"
    },
    "basePath": "/"
}

swagger = Swagger(app, template=swagger_template)


@app.route("/api/health", methods=["GET"])
def health():
    """
    Health check
    ---
    tags:
      - System
    responses:
      200:
        description: API opérationnelle
        schema:
          type: object
          properties:
            status:
              type: string
              example: ok
    """
    return jsonify({"status": "ok"}), 200


@app.route("/api/dashboard", methods=["GET"])
def dashboard():
    """
    Statistiques pour le dashboard
    ---
    tags:
      - Dashboard
    responses:
      200:
        description: Statistiques globales et des modèles
        schema:
          type: object
          properties:
            global:
              type: object
            models_baseline:
              type: array
              items:
                type: object
            best_model:
              type: object
            top_features:
              type: array
              items:
                type: object
    """
    stats = get_dashboard_stats()
    return jsonify(stats), 200


@app.route("/api/predict", methods=["POST"])
def api_predict():
    """
    Prédire si un client va churn ou non
    ---
    tags:
      - Prediction
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        description: Features du client pour la prédiction
        schema:
          type: object
          properties:
            CreditScore:
              type: number
              example: 650
            Gender:
              type: integer
              example: 0
            Age:
              type: integer
              example: 40
            Tenure:
              type: integer
              example: 5
            Balance:
              type: number
              example: 60000
            NumOfProducts:
              type: integer
              example: 2
            HasCrCard:
              type: integer
              example: 1
            IsActiveMember:
              type: integer
              example: 1
            EstimatedSalary:
              type: number
              example: 80000
            Geography_Germany:
              type: integer
              example: 0
            Geography_Spain:
              type: integer
              example: 1
    responses:
      200:
        description: Résultat de la prédiction
        schema:
          type: object
          properties:
            success:
              type: boolean
            features_used:
              type: array
              items:
                type: string
            result:
              type: object
              properties:
                prediction:
                  type: integer
                  example: 1
                label:
                  type: string
                  example: Churn
                probability:
                  type: number
                  format: float
                  example: 0.72
      400:
        description: Erreur de données envoyées
      500:
        description: Erreur interne du serveur
    """
    data = request.get_json()

    if not data:
        return jsonify({"success": False, "error": "JSON body manquant"}), 400

    try:
        result = predict_churn(data)
        return jsonify({
            "success": True,
            "features_used": FEATURE_NAMES,
            "result": result
        }), 200

    except ValueError as ve:
        return jsonify({"success": False, "error": str(ve)}), 400

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
