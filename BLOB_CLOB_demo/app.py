from flask import Flask, render_template, request, redirect, url_for, send_file
import sqlite3
import io
import os

app = Flask(__name__)
DB_FILE = 'library.db'

def get_db_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    media_items = conn.execute('SELECT id, title FROM media_library').fetchall()
    conn.close()
    return render_template('index.html', media_items=media_items)

@app.route('/upload', methods=('GET', 'POST'))
def upload():
    if request.method == 'POST':
        title = request.form['title']
        content_text = request.form['content_text']
        cover_image = request.files['cover_image']
        audio_sample = request.files['audio_sample']

        if title and cover_image and audio_sample:
            cover_data = cover_image.read()
            audio_data = audio_sample.read()
            
            conn = get_db_connection()
            conn.execute('INSERT INTO media_library (title, content_text, cover_image, audio_sample) VALUES (?, ?, ?, ?)',
                         (title, content_text, cover_data, audio_data))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('upload.html')

@app.route('/media/<int:media_id>')
def view_media(media_id):
    conn = get_db_connection()
    media = conn.execute('SELECT id, title, content_text FROM media_library WHERE id = ?', (media_id,)).fetchone()
    conn.close()
    if media is None:
        return "Media not found", 404
    return render_template('view.html', media=media)

@app.route('/image/<int:media_id>')
def get_image(media_id):
    conn = get_db_connection()
    media = conn.execute('SELECT cover_image FROM media_library WHERE id = ?', (media_id,)).fetchone()
    conn.close()
    if media and media['cover_image']:
        return send_file(io.BytesIO(media['cover_image']), mimetype='image/png')
    return "No Image", 404

@app.route('/audio/<int:media_id>')
def get_audio(media_id):
    conn = get_db_connection()
    media = conn.execute('SELECT audio_sample FROM media_library WHERE id = ?', (media_id,)).fetchone()
    conn.close()
    if media and media['audio_sample']:
        return send_file(io.BytesIO(media['audio_sample']), mimetype='audio/wav')
    return "No Audio", 404

if __name__ == '__main__':
    app.run(debug=True)
