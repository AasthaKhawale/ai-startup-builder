import sqlite3
import json
from datetime import datetime

def init_db():
    conn = sqlite3.connect("startup_memory.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS startups (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            idea TEXT,
            result TEXT,
            created_at TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_startup(idea: str, result: dict):
    conn = sqlite3.connect("startup_memory.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO startups (idea, result, created_at)
        VALUES (?, ?, ?)
    """, (idea, json.dumps(result), datetime.now().isoformat()))
    conn.commit()
    conn.close()