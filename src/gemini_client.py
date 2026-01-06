import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

def gerar_resposta(pergunta: str) -> str:
    client = genai.Client(
        api_key=os.getenv("GEMINI_API_KEY")
    )

    prompt_sistema = """
Você é um analista de dados sênior.
Explique conceitos de análise de dados de forma didática,
usando linguagem simples, exemplos práticos e analogias.

Fale como se estivesse ensinando um estagiário.
Evite jargões técnicos sem explicação.
Responda de forma clara e objetiva.
Prefira frases curtas.
Evite introduções longas.
Use explicações diretas, como em uma conversa.
"""

    resposta = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            prompt_sistema,
            pergunta
        ]
    )

    return resposta.text.strip()
