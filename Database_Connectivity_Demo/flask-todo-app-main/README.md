# Database Connectivity Demo using ORM (Python/Flask)

This project demonstrates how to establish connectivity with a relational database (SQLite) using an **Object-Relational Mapper (ORM)** in a High-Level Language (Python). It uses a simple Todo application as a practical example to showcase database operations without writing raw SQL queries.

## Key Concepts Demonstrated

### 1. Object-Relational Mapping (ORM)
Instead of writing SQL tables manually, we define **Models** as Python classes. The ORM (SQLAlchemy) translates these classes into database tables.

**Example Model (`app.py`):**
```python
class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    # ...
```
*   `class Todo` -> Table `todo`
*   `db.Column` -> Table Column

### 2. Database Session Management
The application uses `db.session` to manage transactions. This ensures that a series of operations either all succeed or all fail (Atomicity).

### 3. CRUD Operations via ORM
The application performs Create, Read, Update, and Delete operations using Python methods:

*   **Create (Insert)**:
    ```python
    todo = Todo(title=title, description=desc, user_id=current_user.id)
    db.session.add(todo)
    db.session.commit()
    ```
*   **Read (Select)**:
    ```python
    allTodo = Todo.query.filter_by(user_id=current_user.id).all()
    ```
*   **Update**:
    ```python
    todo = Todo.query.filter_by(sno=sno).first()
    todo.title = new_title
    db.session.commit()
    ```
*   **Delete**:
    ```python
    db.session.delete(todo)
    db.session.commit()
    ```

## Technologies Used
-   **Language**: Python 3
-   **Web Framework**: Flask
-   **ORM**: Flask-SQLAlchemy
-   **Database**: SQLite (Embedded relational database)
-   **Authentication**: Flask-Login & Flask-Bcrypt

## Project Structure
```
flask-todo-app/
├── app.py              # Contains Database Models (User, Todo) and Logic
├── requirements.txt    # Dependencies
├── instance/
│   └── todo.db         # SQLite Database File (Created automatically)
└── templates/          # HTML Views
```

## Running the Connectivity Demo

### Prerequisites
-   Python 3.7+
-   Git

### Steps
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/sachin-paranjape/flask-todo-app.git
    cd flask-todo-app
    ```

2.  **Create and Activate Virtual Environment:**
    ```bash
    # Windows
    virtualenv todo-env
    todo-env\Scripts\activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Application:**
    ```bash
    python app.py
    ```
    *This command will automatically create the `todo.db` database file if it doesn't exist, initializing the tables defined in `app.py`.*

5.  **Verify Connectivity:**
    -   Open `http://localhost:8000/`.
    -   Register a user (Inserts into `User` table).
    -   Add a Task (Inserts into `Todo` table).
    -   View Tasks (Selects from `Todo` table).
