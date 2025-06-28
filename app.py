from flask import Flask, request, jsonify, render_template
import requests
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
                "Content-Type": "application/json"
            },
            json={
                "model": "openai/gpt-3.5-turbo",
                "messages": [{"role": "user", "content": user_message}]
            }
        )
        data = response.json()
        reply = data['choices'][0]['message']['content']
        return jsonify({"reply": reply})
    except Exception as e:
        print("Error:", e)
        return jsonify({"reply": "Terjadi kesalahan saat memproses permintaan."})

# 🔥 Bagian ini penting banget
if __name__ == "__main__":
    app.run(debug=True)
