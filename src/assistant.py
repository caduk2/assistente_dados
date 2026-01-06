from src.audio_recorder import gravar_audio
from src.speech_to_text import transcrever_audio
from src.gemini_client import gerar_resposta
from src.tts import texto_para_audio


class AssistenteDados:
    def __init__(self):
        self.caminho_audio = "audio/input.wav"

    def iniciar(self):
        print("🤖 Assistente de Dados iniciado\n")

        # 1. Captura de áudio
        gravar_audio(self.caminho_audio)

        # 2. Speech to Text
        pergunta = transcrever_audio(self.caminho_audio)

        if not pergunta.strip():
            print("⚠️ Não entendi o áudio.")
            return

        # 3. Geração da resposta
        resposta = gerar_resposta(pergunta)

        print("\n🤖 Resposta do Assistente:")
        print(resposta)

        # 4. Texto para voz
        texto_para_audio(resposta)
