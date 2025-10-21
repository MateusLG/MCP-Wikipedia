import asyncio
import os
from dotenv import load_dotenv
from pathlib import Path
from fastmcp import Client
from openai import OpenAI

load_dotenv() 

caminho_servidor = 'http://localhost:8000/sse'
cliente = Client(caminho_servidor)

async def testar_servidor(cliente, busca):
    
    api_key = os.environ.get('CHAVE_API_OPENAI')
    if not api_key:
        print("Erro: CHAVE_API_OPENAI não encontrada. Verifique seu .env")
        return

    resultado_wikipedia = None

    async with cliente:
        try:
            print(f"Buscando por '{busca}' no servidor MCP...")
            argumentos = {"busca": busca}
            resultado_wikipedia = await cliente.call_tool("buscar_wikipedia", arguments=argumentos)
            print("Busca na Wikipedia concluída.")
        
        except Exception as e:
            print(f"Erro ao chamar a ferramenta 'buscar_wikipedia': {e}")
            print("Verifique se o nome da ferramenta está correto e se o servidor MCP está rodando.")
            return
        
        mensagem_sistema = f"""
        Você é um assistente prestativo. O usuário buscou por '{busca}' na Wikipedia.
        O conteúdo encontrado foi:
        ---
        {resultado_wikipedia}
        ---
        Com base *apenas* no conteúdo acima, formule uma resposta amigável para o usuário.
        """

        try:
            client_openai = OpenAI(api_key=api_key)
            print("Formatando resposta com OpenAI...")
            
            response = client_openai.chat.completions.create(
                model='gpt-4o-mini',
                messages=[
                    {"role": "system", "content": mensagem_sistema},
                    {"role": "user", "content": f"Me fale sobre {busca}."} # O prompt do usuário
                ]
            )
            
            resposta_final = response.choices[0].message.content
            
            print("\n--- Resposta Final ---")
            print(resposta_final)
            print("----------------------")

        except Exception as e:
            print(f"Erro ao chamar a API da OpenAI: {e}")

if __name__ == '__main__':
    asyncio.run(testar_servidor(cliente=cliente, busca='Linus Torvalds'))