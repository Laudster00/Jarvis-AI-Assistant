import google.generativeai as genai
from flask import Flask, request, render_template_string
import pyttsx3

# --- 1. CONFIGURAÇÃO ---
CHAVE_NOVA = "COLOQUE SUA CHAVE AQUI" 

genai.configure(api_key=CHAVE_NOVA)

# IMPORTANTE: Se o 2.0 continuar negando por cota, 
# você pode trocar para 'gemini-1.5-flash' aqui embaixo
model = genai.GenerativeModel('gemini-2.0-flash') 

app = Flask(__name__)

def falar(texto):
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 180)
        engine.say(texto)
        engine.runAndWait()
    except:
        pass

# --- INTERFACE VISUAL ---
HTML_PAGINA = """
<!DOCTYPE html>
<html>
<head>
    <title>JARVIS SYSTEM</title>
    <style>
        body { background: #050505; color: #00d4ff; font-family: 'Segoe UI', sans-serif; text-align: center; padding: 50px; }
        .reactor { 
            width: 120px; height: 120px; border: 4px solid #00d4ff; border-radius: 50%; 
            margin: 0 auto 20px; box-shadow: 0 0 20px #00d4ff, inset 0 0 20px #00d4ff;
            animation: glow 2s infinite;
        }
        @keyframes glow { 0% { opacity: 0.5; } 50% { opacity: 1; } 100% { opacity: 0.5; } }
        input { padding: 12px; width: 350px; border-radius: 5px; border: 1px solid #00d4ff; background: #000; color: #fff; outline: none; }
        button { padding: 12px 25px; background: #00d4ff; color: #000; border: none; cursor: pointer; font-weight: bold; border-radius: 5px; }
        #res { margin-top: 25px; font-size: 1.2em; color: #fff; text-shadow: 0 0 5px #00d4ff; }
    </style>
</head>
<body>
    <div class="reactor"></div>
    <h1>SISTEMA JARVIS ONLINE</h1>
    <input type="text" id="pergunta" placeholder="O que deseja, Senhor?">
    <button onclick="enviar()">EXECUTAR</button>
    <div id="res">Aguardando ordens...</div>

    <script>
        function enviar() {
            let p = document.getElementById('pergunta').value;
            let d = document.getElementById('res');
            if(!p) return;
            d.innerHTML = "<i style='color:#777'>Consultando banco de dados...</i>";
            fetch('/jarvis?pergunta=' + encodeURIComponent(p))
                .then(r => r.text())
                .then(t => { d.innerHTML = t; });
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_PAGINA)

@app.route('/jarvis')
def jarvis_ia():
    pergunta = request.args.get('pergunta')
    if not pergunta: return "Sem comando."
    try:
        # Gerando a resposta
        response = model.generate_content(f"Responda como o Jarvis: {pergunta}", 
                                        generation_config={"max_output_tokens": 100})
        resposta = response.text
        
        # O retorno para o site
        falar(resposta)
        return f"<b>JARVIS:</b> {resposta}"
        
    except Exception as e:
        error_msg = str(e)
        if "429" in error_msg:
            return "<b>AVISO:</b> Limite de requisições atingido. Por favor, aguarde 60 segundos para o sistema resetar."
        return f"<b>ERRO:</b> {error_msg}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)