#!/usr/bin/env python3
"""
Database initialization script.
Run this to create the SQLite database and tables.
"""

from database import create_tables, engine
from sqlalchemy import text

def init_database():
    """Initialize the database with tables"""
    print("Creating database tables...")
    create_tables()
    
    # Test connection
    with engine.connect() as conn:
        result = conn.execute(text("SELECT name FROM sqlite_master WHERE type='table';"))
        tables = [row[0] for row in result]
        print(f"Created tables: {', '.join(tables)}")
    
    print("Database initialized successfully!")

if __name__ == "__main__":
    init_database()
