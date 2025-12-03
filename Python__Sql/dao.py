import sqlite3
import requests
from fastapi import FastAPI, HTTPException
from datetime import datetime, timedelta

class ComedouroRoboDAO():
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        sql = """
            INSERT INTO Comedouro_Robo (mac_address, rotacoes)
            VALUES (?, ?)
        """
        cls.execute(sql, (obj.get_mac(), obj.get_rotacoes())
        cls.fechar()

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        sql = """
            UPDATE Comedouro_Robo SET rotacoes=?
            WHERE mac_address=?
        """
        cls.execute(sql, (obj.get_rotacoes(), obj.get_mac()))
        cls.fechar()

class ReposicaoDAO():
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        sql = """
            INSERT INTO Reposicao_Racao (mac_address, DT_reposicao)
            VALUES (?, ?)
        """
        cls.execute(sql, (obj.get_mac(), obj.get_data())
        cls.fechar()

    @classmethod
    def listar(cls):
        cls.abrir()
        sql = "SELECT * FROM Reposicao_Racao"
        cursor = cls.execute(sql)
        rows = cursor.fetchall()
        objs = [ReposicaoRacao(id, mac, data) for (id, mac_address, DT_reposicao) in rows]
        cls.fechar()
        return objs

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        sql = "DELETE FROM Reposicao_Racao WHERE id=?"
        cls.execute(sql, (obj.get_id(),))
        cls.fechar()

class DisplayDAO():
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        sql = """
            INSERT INTO Display (mac_address, cor, tema,)
            VALUES (?, ?, ?)
        """
        cls.execute(sql, (obj.get_mac(), obj.get_data())
        cls.fechar()

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        #    if cor == "DEFAULT":
        sql = """
            UPDATE Display SET cor=?
            UPDATE Display SET tema=?
            WHERE mac_address=?

        """
        cls.execute(sql, (obj.get_cor(), obj.get_tema(), obj.get_mac()))
        cls.fechar()
        