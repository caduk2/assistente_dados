# 🎙️ Assistente de Voz para Estagiários em Análise de Dados

Este projeto consiste em um **assistente inteligente por voz**, desenvolvido em Python, com foco em **Análise de Dados**.  
O assistente atua como um **analista sênior didático**, explicando conceitos técnicos de forma simples e acessível para estagiários.

O usuário faz perguntas por voz, o sistema processa a pergunta com IA e retorna a resposta também em áudio.

---

## 🎯 Objetivo

Criar um assistente educacional que:
- Auxilie estagiários de Análise de Dados
- Explique conceitos técnicos de forma didática
- Simule a comunicação de um analista sênior
- Utilize IA generativa e processamento de áudio

---

## 🧠 Funcionalidades

- 🎙️ Gravação de áudio do usuário
- 🧠 Reconhecimento de fala com Whisper
- 🤖 Geração de resposta com Gemini API
- 🗣️ Síntese de voz com gTTS
- 🧹 Limpeza de texto para leitura natural em TTS
- 🧩 Arquitetura modular e escalável

---

## 🔁 Fluxo do Sistema

1. Usuário fala com o assistente
2. Áudio é transcrito para texto (Speech-to-Text)
3. Texto é enviado à IA (Gemini)
4. IA gera resposta didática
5. Texto é convertido em áudio
6. Assistente responde por voz

---

## 🛠️ Tecnologias Utilizadas

- Python 3.10+
- Whisper (Speech-to-Text)
- Google Gemini API (IA Generativa)
- gTTS (Text-to-Speech)
- sounddevice / scipy
- Visual Studio Code

---

## 🏗️ Estrutura do Projeto

assistente_dados/
├── audio/
│ ├── input.wav
│ └── output.mp3
├── src/
│ ├── assistant.py
│ ├── audio_recorder.py
│ ├── speech_to_text.py
│ ├── gemini_client.py
│ └── tts.py
├── main.py
├── requirements.txt
└── README.md

---

## ▶️ Como Executar

1. **Clone o repositório**

   Clone o projeto para sua máquina local:

   git clone https://github.com/seu-usuario/assistente_dados.git

2. **Crie e ative o ambiente virtual**

   Crie o ambiente virtual:

   python -m venv venv

   Ative o ambiente virtual (Windows):

   venv\Scripts\activate

3. **Instale as dependências**

   Instale todas as bibliotecas necessárias:

   pip install -r requirements.txt

4. **Configure a variável de ambiente**

   Crie um arquivo chamado `.env` na raiz do projeto e adicione sua chave da API do Gemini:

   GEMINI_API_KEY=SUA_CHAVE_AQUI

5. **Execute o projeto**

   Inicie o assistente executando:

   python main.py

---

### 📌 Observações

**PS:**  
Lembre de criar as pastas e arquivos que não subiram devido a boas práticas de versionamento (como `.gitignore`).  
Que suas previsões estejam sempre a seu favor e seus modelos tragam só bons insights.  
Boa codagem! ☕💻

---

### 🚀 Próximos Passos

- Histórico de conversa  
- Modo de resposta curta / longa  
- Interface gráfica com Streamlit  
- Integração com datasets reais  

---
