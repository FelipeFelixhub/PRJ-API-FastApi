from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

vendas = {
    1: {"item": "lata", "preco_unitario": 4, "quantidade": 5},
    2: {"item": "garrafa 2L", "preco_unitario": 15, "quantidade": 5},
    3: {"item": "garrafa 750ml", "preco_unitario": 10, "quantidade": 5},
    4: {"item": "ks", "preco_unitario": 4, "quantidade": 5}
}

class Venda(BaseModel):
    item: str
    preco_unitario: float
    quantidade: int


@app.get("/")
def home():
    return {"Vendas": len(vendas)}


@app.get("/vendas/{id_venda}")
def pegar_venda(id_venda: int):
    if id_venda in vendas:
        return vendas[id_venda]
    else:
        raise HTTPException(status_code=404, detail="ID Venda inexistente")


@app.post("/vendas/")
def criar_venda(venda: Venda):
    id_venda = max(vendas.keys()) + 1
    vendas[id_venda] = venda.model_dump()
    return vendas[id_venda]


@app.put("/vendas/{id_venda}")
def atualizar_venda(id_venda: int, venda: Venda):
    if id_venda in vendas:
        vendas[id_venda] = venda.model_dump()
        return vendas[id_venda]
    else:
        raise HTTPException(status_code=404, detail="ID Venda inexistente")


@app.delete("/vendas/{id_venda}")
def deletar_venda(id_venda: int):
    if id_venda in vendas:
        del vendas[id_venda]
        return {"message": "Venda deletada com sucesso"}
    else:
        raise HTTPException(status_code=404, detail="ID Não encontrado")
