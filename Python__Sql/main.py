from fastapi import FastAPI, HTTPException
from pydantic import BaseModel #pesquisar objetivo
from database import Database #pesquisar objetivo
from dao import ComedouroRoboDAO, ReposicaoDAO, DisplayDAO
from models import ComedouroRobo, ReposicaoRacao, Display
from datetime import datetime
repos 
app = FastAPI()
class LeituraIn(BaseModel): # MODEL PARA ENTRADA DO ESP32
    mac: str
    distancia: float
    nivel_bateria: float

class ComandoIn(BaseModel): # MODEL PARA COMANDOS DO SITE → ESP32
    comando: str
    payload: str = ""

@app.post("/leitura")
def receber_leitura(dados: LeituraIn): # ROTA DO ESP32 MANDAR LEITURA
    Database.abrir()
    Database.execute("""
        INSERT INTO Leitura (nivel_bateria, distancia)
        VALUES (?, ?)
    """, (dados.nivel_bateria, dados.distancia))
    Database.fechar()
    return {"status": "ok", "msg": "Leitura registrada com sucesso"}

@app.post("/comando")
def enviar_comando(cmd: ComandoIn): # ROTA DO CELULAR/SITE MANDAR ROTINAS PARA O ESP32
    Database.abrir()
    Database.execute("""
        INSERT INTO comandos (comando, payload, enviado)
        VALUES (?, ?, 0)
    """, (cmd.comando, cmd.payload))
    Database.fechar()
    return {"status": "ok"}

@app.get("/comando")
def pegar_comando(): # ROTA DO ESP32 BUSCAR COMANDOS QUE O SITE ENVIOU
    Database.abrir()
    cursor = Database.conn.cursor()
    cursor.execute("SELECT id, comando, payload FROM comandos WHERE enviado=0 LIMIT 1")
    row = cursor.fetchone()

    if not row:
        Database.fechar()
        return {"comando": None}

    id_cmd, comando, payload = row

    cursor.execute("UPDATE comandos SET enviado=1 WHERE id=?", (id_cmd,))
    Database.conn.commit()
    Database.fechar()

    return {"comando": comando, "payload": payload}

@app.get("/reposicoes")
def listar_reposicoes(): # ROTA PARA STREAMLIT LER REPOSIÇÕES
    Database.abrir()
    cursor = Database.conn.cursor()
    cursor.execute("SELECT * FROM Reposicao_Racao")
    rows = cursor.fetchall()
    Database.fechar()

    return [
        {"id": row[0], "mac": row[1], "data": row[2]}
        for row in rows
    ]
