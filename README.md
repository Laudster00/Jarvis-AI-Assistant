# 🦾 Jarvis AI Assistant - Python, Gemini 2.0 & Automação Windows

> **Status:** 🟢 Online | 📦 Versão Standalone Disponível

Este é o meu primeiro grande projeto de programação, desenvolvido antes do início do meu 1º semestre de faculdade. O **Jarvis** é um assistente virtual inspirado no universo Marvel, que evoluiu de um script simples para um **software de sistema completo** capaz de gerenciar o computador e responder por voz usando Inteligência Artificial.

## ⚠️ Nota Importante sobre a IA (Disclaimer)
A integração atual utiliza a API gratuita do **Google Gemini 2.0 Flash**.
- **Limitações:** Por ser uma chave de teste gratuita, a IA possui **filtros de segurança rígidos** (que podem bloquear certas respostas) e limites de requisição (pode dar erro se usar muito rápido).
- **Contexto:** Esta API foi implementada apenas como uma solução temporária ("placeholder") para permitir o raciocínio gratuito.
- **Recomendação:** Para uma experiência real de assistente pessoal (sem bloqueios ou censura), sugiro futuramente adaptar o código para modelos locais (**Ollama/Llama 3**) ou APIs pagas (**OpenAI/Groq**).

## 🚀 Novas Funcionalidades (Update v2.0)
Agora o Jarvis não é apenas um script Python, mas um aplicativo integrado ao Windows:
- **Modo Standalone (.exe):** Compilado em executável, não exige instalação de Python para rodar.
- **Inicialização Automática:** O sistema se registra automaticamente no **Registro do Windows (Regedit)** para iniciar sozinho junto com o PC, rodando em segundo plano.
- **Comandos Locais (Offline):** Capaz de abrir ferramentas como **Calculadora** e **Bloco de Notas** diretamente pelo comando de voz ou texto, sem depender da nuvem.
- **Interface Silenciosa:** Roda oculto (sem janelas de terminal), acessível via interface Web.

## 🧠 Core Features
- **Interface Web:** Visual futurista do "Reator Arc" utilizando HTML/CSS, servido via Flask.
- **Cérebro (LLM):** Integração com **Google Gemini 2.0 Flash** (Versão Free).
- **Síntese de Voz:** Respostas faladas em tempo real via biblioteca `pyttsx3`.
- **Backend Flask:** Servidor local robusto rodando na porta 8000.

## 🛠️ Engenharia e Problem Solving
Durante o desenvolvimento, enfrentei desafios técnicos que simulam o ambiente real de engenharia:
1. **Compilação e Distribuição:** Utilizei `PyInstaller` para empacotar o ambiente Python e dependências em um único arquivo binário otimizado.
2. **Automação de Sistema:** Implementei manipulação da biblioteca `winreg` para criar chaves de inicialização no Windows via código.
3. **Gestão de API:** Tratamento de erros `429` (limite de cota) e `404` (modelos depreciados), garantindo que o assistente falhe graciosamente.

## 💻 Tecnologias
- **Linguagem:** Python 3.x
- **Framework:** Flask
- **AI:** Google Generative AI (Gemini) - *Temporário*
- **Sistema:** `winreg` (Registro), `os`, `sys`
- **Compilador:** PyInstaller

## 🔧 Como usar o projeto

### Opção 1: Baixando o Software (Recomendado)
1. Vá na aba **Releases** aqui no GitHub e baixe o `Jarvis.exe`.
2. Execute o arquivo. Na primeira vez, ele configurará a inicialização automática.
3. Acesse `http://localhost:8000` no seu navegador.

### Opção 2: Rodando o Código Fonte (Para Devs)
1. Clone o repositório.
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
