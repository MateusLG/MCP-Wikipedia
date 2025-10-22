from fastmcp import FastMCP
import wikipedia

servidor_mcp = FastMCP("buscar-wikipedia")

@servidor_mcp.tool()
def buscar_wikipedia(busca: str) -> str:
    return wikipedia.summary(busca)

if __name__ == '__main__':
    servidor_mcp.run(transport='stdio')