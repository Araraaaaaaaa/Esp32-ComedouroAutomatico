import sqlite3
import requests
from fastapi import FastAPI, HTTPException
from datetime import datetime, timedelta

class Database:
    conn = None
    nome_bd="agenda.db"
    
    @classmethod
    def abrir(cls):
        cls.conn = sqlite3.connect(cls.nome_bd)
        cls.conn.execute("PRAGMA foreign_keys = ON")
 
    @classmethod
    def fechar(cls):
        cls.conn.close()

    @classmethod
    def execute(cls, sql, params = None):
        cursor = cls.conn.cursor()
        cursor.execute(sql, params or [])
        cls.conn.commit()

    @classmethod
    def criar_tabelas(cls):
        cls.execute("""
            CREATE TABLE IF NOT EXISTS Comedouro_Robo (
                mac_address TEXT PRIMARY KEY NOT NULL,
                rotacoes INTEGER DEFAULT 3,
            );
        """)
        cls.execute("""
            CREATE TABLE IF NOT EXISTS Reposicao_Racao (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                mac_address TEXT UNIQUE NOT NULL,
                DT_reposicao TEXT NOT NULL,
                FOREIGN KEY (mac_address) REFERENCES Comedouro_Robo(mac_address)
            );
        """)
        cls.execute("""
            CREATE TABLE IF NOT EXISTS Display (
                mac_address TEXT PRIMARY KEY NOT NULL,
                cor TEXT DEFAULT '#7ed957',
                tema INTEGER DEFAULT 0,
                FOREIGN KEY (mac_address) REFERENCES Comedouro_Robo(mac_address)
            );
        """)
        cls.execute("""
            CREATE TABLE IF NOT EXISTS Leitura (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                nivel_bateria REAL,
                distancia REAL,
            );
        """)
        cls.execute("""
            CREATE TABLE IF NOT EXISTS comandos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                comando TEXT,
                payload TEXT,
                enviado INTEGER DEFAULT 0,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            );
        """)

if __name__ == "__main__":
    Database.abrir()
    Database.criar_tabelas()
    Database.fechar()
