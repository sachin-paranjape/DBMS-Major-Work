# BLOB & CLOB Demo Application

## Overview
This project demonstrates how to handle **Binary Large Objects (BLOBs)** and **Character Large Objects (CLOBs)** in a relational database using Python and SQLite. It provides two interfaces for managing multimedia content (images, audio, and text):
1.  **Web Interface (Flask)**: A user-friendly web app to upload and view media.
2.  **Command Line Interface (CLI)**: A script (`media_vault.py`) for administrative tasks and batch processing.

## Features
-   **Database Storage**: Stores images (PNG) and audio (WAV) as BLOBs, and text content as CLOBs (TEXT) directly in the SQLite database.
-   **Dual Interface**:
    -   **Web App**: Upload new entries and view/play them in the browser.
    -   **CLI**: Add entries from local files, list all entries, and retrieve/export stored media back to the file system.
-   **Data Retrieval**: Demonstrates how to read binary data from the database and serve it to a web client or save it to disk.

## Project Structure
-   `app.py`: The main Flask application file.
-   `media_vault.py`: The CLI script for database management.
-   `library.db`: The SQLite database file (created automatically).
-   `templates/`: HTML templates for the web application.
-   `static/`: Static assets for the web application.
-   `assets/`: Folder to store sample assets for uploading.
-   `retrieved_media/`: Folder where the CLI exports retrieved media files.

## Prerequisites
-   Python 3.x
-   Flask (`pip install flask`)

## How to Run

### 1. Web Application
1.  Open a terminal in the `BLOB_CLOB_demo` directory.
2.  Run the Flask app:
    ```bash
    python app.py
    ```
3.  Open your web browser and navigate to `http://127.0.0.1:5000`.
4.  Use the "Upload New Media" button to add content.
5.  Click on a title to view the text, image, and play the audio.

### 2. Command Line Interface (CLI)
1.  Open a terminal in the `BLOB_CLOB_demo` directory.
2.  Run the script:
    ```bash
    python media_vault.py
    ```
3.  Follow the on-screen menu:
    -   **1. Add New Entry**: Prompts for title and file paths for text, image, and audio.
    -   **2. List All Entries**: Shows IDs and titles of stored media.
    -   **3. Retrieve Entry**: Exports the stored BLOBs/CLOBs back to files in the `retrieved_media` directory.

## Database Schema
The project uses a single table `media_library`:
```sql
CREATE TABLE media_library (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content_text TEXT,      -- CLOB
    cover_image BLOB,       -- BLOB (Image)
    audio_sample BLOB       -- BLOB (Audio)
);
```

## Key Concepts Demonstrated
-   **BLOB (Binary Large Object)**: Used here for storing `cover_image` and `audio_sample`. Ideal for multimedia files.
-   **CLOB (Character Large Object)**: Used here for `content_text`. Ideal for large text documents.
-   **Binary I/O**: Reading files in binary mode (`'rb'`) for insertion and writing binary data (`'wb'`) for retrieval.
