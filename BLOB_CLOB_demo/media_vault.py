import sqlite3
import os
import sys

DB_FILE = 'library.db'
RETRIEVAL_DIR = 'retrieved_media'

def connect_db():
    return sqlite3.connect(DB_FILE)

def setup_database():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS media_library (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content_text TEXT,
            cover_image BLOB,
            audio_sample BLOB
        )
    ''')
    conn.commit()
    conn.close()
    print("Database initialized.")

def add_media(title, text_path, image_path, audio_path):
    try:
        with open(text_path, 'r', encoding='utf-8') as f:
            text_data = f.read()
        with open(image_path, 'rb') as f:
            image_data = f.read()
        with open(audio_path, 'rb') as f:
            audio_data = f.read()
            
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO media_library (title, content_text, cover_image, audio_sample)
            VALUES (?, ?, ?, ?)
        ''', (title, text_data, image_data, audio_data))
        conn.commit()
        print(f"Successfully added '{title}' to the library.")
        conn.close()
    except Exception as e:
        print(f"Error adding media: {e}")

def get_media(media_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT title, content_text, cover_image, audio_sample FROM media_library WHERE id = ?', (media_id,))
    row = cursor.fetchone()
    conn.close()
    
    if row:
        title, content, cover, audio = row
        print(f"\n--- Media Found: {title} ---")
        print(f"Content Preview (First 100 chars):\n{content[:100]}...")
        
        if not os.path.exists(RETRIEVAL_DIR):
            os.makedirs(RETRIEVAL_DIR)
            
        # Save retrieved files
        cover_path = os.path.join(RETRIEVAL_DIR, f"{title}_cover.png")
        audio_path = os.path.join(RETRIEVAL_DIR, f"{title}_audio.wav")
        text_path = os.path.join(RETRIEVAL_DIR, f"{title}_content.txt")
        
        with open(cover_path, 'wb') as f:
            f.write(cover)
        with open(audio_path, 'wb') as f:
            f.write(audio)
        with open(text_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"\nFiles exported to '{RETRIEVAL_DIR}':")
        print(f"- {cover_path}")
        print(f"- {audio_path}")
        print(f"- {text_path}")
    else:
        print("Media not found.")

def list_media():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT id, title FROM media_library')
    rows = cursor.fetchall()
    conn.close()
    
    print("\n--- Library Catalog ---")
    for row in rows:
        print(f"ID: {row[0]} | Title: {row[1]}")

def main():
    setup_database()
    
    while True:
        print("\n=== MediaVault System ===")
        print("1. Add New Entry")
        print("2. List All Entries")
        print("3. Retrieve Entry")
        print("4. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            title = input("Enter Title: ")
            txt = input("Enter Text File Path: ")
            img = input("Enter Image File Path: ")
            aud = input("Enter Audio File Path: ")
            if os.path.exists(txt) and os.path.exists(img) and os.path.exists(aud):
                add_media(title, txt, img, aud)
            else:
                print("Error: One or more files not found.")
        elif choice == '2':
            list_media()
        elif choice == '3':
            try:
                mid = int(input("Enter Media ID: "))
                get_media(mid)
            except ValueError:
                print("Invalid ID.")
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
