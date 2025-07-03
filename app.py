from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

# === Configurações (use variáveis de ambiente no Azure) ===
AZURE_TRANSLATOR_KEY = os.environ.get("AZURE_TRANSLATOR_KEY")
AZURE_TRANSLATOR_ENDPOINT = os.environ.get("AZURE_TRANSLATOR_ENDPOINT", "https://api.cognitive.microsofttranslator.com/")
AZURE_TRANSLATOR_REGION = os.environ.get("AZURE_TRANSLATOR_REGION", "eastus")

OPENAI_API_KEY = os.environ.get("OPENAI_KEY")
OPENAI_ENDPOINT = "https://api.openai.com/v1/chat/completions"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.get_json()
    text = data.get("text", "")

    headers = {
        'Ocp-Apim-Subscription-Key': AZURE_TRANSLATOR_KEY,
        'Ocp-Apim-Subscription-Region': AZURE_TRANSLATOR_REGION,
        'Content-type': 'application/json'
    }

    body = [{
        'text': text
    }]

    params = {
        'api-version': '3.0',
        'from': 'en',
        'to': ['pt']
    }

    response = requests.post(AZURE_TRANSLATOR_ENDPOINT + '/translate', params=params, headers=headers, json=body)
    result = response.json()

    translation = result[0]['translations'][0]['text']
    return jsonify({"translation": translation})

@app.route('/insight', methods=['POST'])
def get_insight():
    data = request.get_json()
    text = data.get("text", "")

    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }

    body = {
        "model": "gpt-4",
        "messages": [
            {"role": "system", "content": "Você é um analista inteligente que resume e detecta sentimentos em conversas."},
            {"role": "user", "content": f"Analise o seguinte conteúdo: {text}"}
        ]
    }

    response = requests.post(OPENAI_ENDPOINT, headers=headers, json=body)
    result = response.json()
    answer = result["choices"][0]["message"]["content"]
    return jsonify({"insight": answer})

if __name__ == '__main__':
    app.run(debug=True)
