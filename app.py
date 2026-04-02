from flask import Flask, render_template, request, jsonify
from datetime import datetime, timedelta
import requests

app = Flask(__name__)

# Mock simples (LinkedIn não permite scraping direto oficialmente)
def buscar_vagas(query, horas):
    agora = datetime.now()
    vagas = []

    for i in range(1, 21):
        vagas.append({
            "titulo": f"{query} - Vaga {i}",
            "empresa": f"Empresa {i}",
            "link": "https://www.linkedin.com/jobs",
            "data": agora - timedelta(hours=i)
        })

    limite = agora - timedelta(hours=horas)

    return [
        v for v in vagas
        if v["data"] >= limite
    ]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/buscar", methods=["POST"])
def buscar():
    data = request.json
    query = data.get("query", "")
    horas = int(data.get("horas", 24))

    vagas = buscar_vagas(query, horas)

    return jsonify(vagas)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
