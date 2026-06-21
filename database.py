import sqlite3

DB_NAME = "career.db"

def init_db():

    conn = sqlite3.connect(DB_NAME)

    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS chats(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        education TEXT,
        skills TEXT,
        interests TEXT,
        mbti TEXT,
        recommendation TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def save_chat(
    username,
    education,
    skills,
    interests,
    mbti,
    recommendation
):

    conn = sqlite3.connect(DB_NAME)

    cur = conn.cursor()

    cur.execute("""
    INSERT INTO chats(
        username,
        education,
        skills,
        interests,
        mbti,
        recommendation
    )
    VALUES(?,?,?,?,?,?)
    """,(
        username,
        education,
        skills,
        interests,
        mbti,
        recommendation
    ))

    conn.commit()
    conn.close()