import google.generativeai as genai
from flask import Flask, request, render_template_string
import pyttsx3
import os
import sys
import winreg as reg # Biblioteca para mexer no Registro do Windows

# --- CONFIGURAÇÃO DA INICIALIZAÇÃO AUTOMÁTICA ---
def add_to_startup():
    # Pega o caminho do arquivo atual (seja .py ou .exe)
    path = os.path.realpath(sys.executable if getattr(sys, 'frozen', False) else __file__)
    key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
    try:
        key = reg.OpenKey(reg.HKEY_CURRENT_USER, key_path, 0, reg.KEY_SET_VALUE)
        reg.SetValueEx(key, "JarvisSystem", 0, reg.REG_SZ, path)
        reg.CloseKey(key)
    except Exception as e:
        print(f"Erro ao configurar inicialização: {e}")

# --- CONFIGURAÇÃO IA ---
CHAVE_NOVA = "SUA CHAVE" 
genai.configure(api_key=CHAVE_NOVA)
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

# --- INTERFACE VISUAL (Mantida a mesma) ---
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
    pergunta = request.args.get('pergunta', '').lower()
    if not pergunta: return "Sem comando."
    
    if "calculadora" in pergunta:
        os.system("calc")
        msg = "Abrindo a calculadora, senhor."
        falar(msg)
        return f"<b>JARVIS LOCAL:</b> {msg}"
    
    if "bloco de notas" in pergunta or "notepad" in pergunta:
        os.system("notepad")
        msg = "Iniciando o Bloco de Notas."
        falar(msg)
        return f"<b>JARVIS LOCAL:</b> {msg}"

    try:
        response = model.generate_content(f"Responda como o Jarvis: {pergunta}", 
                                        generation_config={"max_output_tokens": 100})
        resposta = response.text
        falar(resposta)
        return f"<b>JARVIS:</b> {resposta}"
        
    except Exception as e:
        error_msg = str(e)
        if "429" in error_msg:
            aviso = "Limite de cota atingido. Estou operando apenas com comandos locais no momento."
            falar(aviso)
            return f"<b>AVISO:</b> {aviso}"
        return f"<b>ERRO:</b> {error_msg}"

if __name__ == '__main__':
    add_to_startup() # Chama a função para garantir que inicie com o PC
    app.run(host='0.0.0.0', port=8000)
