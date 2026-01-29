\# 🦾 Jarvis AI Assistant - Python \& Gemini 2.0



Este é o meu primeiro grande projeto de programação, desenvolvido antes do início do meu 1º semestre de faculdade. O \*\*Jarvis\*\* é um assistente virtual inspirado no universo Marvel, capaz de processar comandos de texto através de inteligência artificial generativa e responder por voz.



\## 🚀 Funcionalidades

\- \*\*Interface Web:\*\* Interface moderna com o visual do "Reator Arc" utilizando HTML e CSS.

\- \*\*Integração com Gemini API:\*\* Utiliza os modelos mais recentes (Gemini 2.0 Flash) para respostas rápidas e inteligentes.

\- \*\*Síntese de Voz:\*\* Respostas faladas em tempo real via biblioteca `pyttsx3`.

\- \*\*Backend Flask:\*\* Servidor robusto para gerenciar as rotas de comunicação entre o usuário e a IA.



\## 🛠️ Desafios Superados (Problem Solving)

Durante o desenvolvimento, enfrentei e resolvi desafios técnicos reais:

1\. \*\*Migração de Modelos (Erro 404):\*\* Identifiquei a depreciação de modelos antigos e atualizei o sistema para suportar a nova geração `gemini-2.0-flash`.

2\. \*\*Gestão de Quotas (Erro 429):\*\* Implementei tratamentos de exceção para lidar com limites de requisições da API gratuita, garantindo a estabilidade do servidor.



\## 🛠️ Tecnologias Utilizadas

\- \*\*Linguagem:\*\* Python

\- \*\*Framework Web:\*\* Flask

\- \*\*AI:\*\* Google Generative AI (Gemini API)

\- \*\*Voz:\*\* Pyttsx3



\## 🔧 Como rodar o projeto

1\. Clone o repositório.

2\. Instale as dependências: `pip install -r requirements.txt`.

3\. Insira sua chave da API do Google no arquivo `jarvis.py`.

4\. Execute: `python jarvis.py`.

5\. Acesse `*http://localhost:8000*` no seu navegador.

