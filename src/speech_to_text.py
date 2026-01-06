import whisper

def transcrever_audio(caminho_audio="audio/input.wav"):
    print("🧠 Transcrevendo áudio com Whisper...")

    model = whisper.load_model("base", device="cpu")
    resultado = model.transcribe(
        caminho_audio,
        language="pt",
        fp16=False
    )

    texto = resultado["text"].strip()

    print("📝 Texto reconhecido:")
    print(texto)

    return texto
