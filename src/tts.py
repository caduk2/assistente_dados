from gtts import gTTS
import os
import re

def limpar_texto_para_voz(texto: str) -> str:
    """
    Remove símbolos de Markdown e ajusta o texto
    para leitura natural em voz.
    """

    # Remove títulos Markdown (###, ##, #)
    texto = re.sub(r"#+\s*", "", texto)

    # Remove negrito e itálico (* e **)
    texto = texto.replace("**", "")
    texto = texto.replace("*", "")

    # Remove linhas separadoras ---
    texto = re.sub(r"-{2,}", "", texto)

    # Remove múltiplas quebras de linha
    texto = re.sub(r"\n{2,}", "\n", texto)

    return texto.strip()

def texto_para_audio(
    texto: str,
    caminho_saida="audio/output.mp3",
    idioma="pt",
    velocidade=1.0
):
    print("🔊 Gerando áudio da resposta...")

    texto_limpo = limpar_texto_para_voz(texto)

    tts = gTTS(
        text=texto_limpo,
        lang=idioma,
        slow=False
    )

    tts.save(caminho_saida)

    print("✅ Áudio gerado com sucesso!")

    # Reproduz automaticamente (Windows)
    os.system(f'start {caminho_saida}')

