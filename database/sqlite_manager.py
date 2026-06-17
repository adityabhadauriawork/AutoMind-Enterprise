import sqlite3


def create_connection():

    conn = sqlite3.connect(
        "database/automind.db"
    )

    return conn
def create_tables():

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS forecast_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        forecast_date TEXT,
        predicted_sales REAL
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS model_registry (

        id INTEGER PRIMARY KEY AUTOINCREMENT,
            
        version TEXT,

        model_name TEXT,

        r2_score REAL,

        mae REAL,

        rmse REAL,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()
def save_forecast(
    forecast_date,
    predicted_sales
):

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO forecast_history
        (
            forecast_date,
            predicted_sales
        )
        VALUES (?, ?)
        """,
        (
            forecast_date,
            predicted_sales
        )
    )

    conn.commit()
    conn.close()
create_tables()

def save_model_metrics(

    model_name,

    version,

    r2,

    mae,

    rmse

):

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO model_registry
        (
            model_name,
            version,
            r2_score,
            mae,
            rmse
        )
        VALUES (?, ?,?, ?, ?)
        """,
        (
            model_name,
            version,
            r2,
            mae,
            rmse
        )
    )

    conn.commit()

    conn.close()