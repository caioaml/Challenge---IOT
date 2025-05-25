from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

ARQUIVO = "vagas.json"

def carregar_vagas():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    return {}

def salvar_vagas(vagas):
    with open(ARQUIVO, "w") as f:
        json.dump(vagas, f, indent=4)

@app.route("/")
def home():
    return "API do MotoMap AI rodando!"

@app.route("/vaga", methods=["POST"])
def atualizar_vaga():
    dados = request.json
    vaga_id = dados.get("vaga_id")
    status = dados.get("status")
    placa = dados.get("placa")

    if not vaga_id:
        return jsonify({"erro": "vaga_id é obrigatório"}), 400

    vagas = carregar_vagas()
    vagas[vaga_id] = {"status": status, "placa": placa}
    salvar_vagas(vagas)
    return jsonify({"mensagem": f"Vaga {vaga_id} atualizada com sucesso."})

@app.route("/vagas", methods=["GET"])
def listar_vagas():
    return jsonify(carregar_vagas())

if __name__ == "__main__":
    app.run(debug=True)
