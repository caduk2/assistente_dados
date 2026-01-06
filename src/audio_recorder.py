import sounddevice as sd
from scipy.io.wavfile import write

def gravar_audio(
    caminho_arquivo="audio/input.wav",
    duracao=5,
    sample_rate=44100
):
    print("🎙️ Gravando... fale agora")
    
    audio = sd.rec(
        int(duracao * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="int16"
    )
    
    sd.wait()
    write(caminho_arquivo, sample_rate, audio)
    
    print("✅ Gravação finalizada!")
