import sqlite3

def init_db():
    conn = sqlite3.connect("threats.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS threats (
                    id INTEGER PRIMARY KEY,
                    ip TEXT,
                    protocol TEXT,
                    port INTEGER,
                    status TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )""")
    conn.commit()
    conn.close()

def add_threat(ip, protocol, port, status):
    conn = sqlite3.connect("threats.db")
    c = conn.cursor()
    c.execute("INSERT INTO threats (ip, protocol, port, status) VALUES (?, ?, ?, ?)", 
              (ip, protocol, port, status))
    conn.commit()
    conn.close()

def get_threats():
    conn = sqlite3.connect("threats.db")
    df = conn.execute("SELECT * FROM threats").fetchall()
    conn.close()
    return df
