import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from sqlalchemy import text
from backend.db import engine, DATABASE_URL
from backend.config import settings

def test_connection():
    """Test database connection and display connection info"""
    print("=" * 50)
    print("Testing Database Connection")
    print("=" * 50)
    
    # Display connection info (without password)
    print(f"Host: {settings.DB_HOST}")
    print(f"Port: {settings.DB_PORT}")
    print(f"Database: {settings.DB_NAME}")
    print(f"User: {settings.DB_USER}")
    print(f"Password: {'*' * len(settings.DB_PASSWORD) if settings.DB_PASSWORD else 'NOT SET'}")
    print("-" * 50)
    
    try:
        # Test connection
        with engine.connect() as conn:
            result = conn.execute(text("SELECT version();"))
            version = result.fetchone()[0]
            print("✅ Connection successful!")
            print(f"PostgreSQL version: {version}")
            
            # Test if we can query
            result = conn.execute(text("SELECT current_database();"))
            db_name = result.fetchone()[0]
            print(f"Connected to database: {db_name}")
            
            return True
    except Exception as e:
        print(f"❌ Connection failed!")
        print(f"Error: {str(e)}")
        print("\nTroubleshooting:")
        print("1. Check if PostgreSQL is running:")
        print("   docker-compose -f docker/docker-compose.yaml up -d")
        print("2. Verify your .env file has correct database credentials")
        print("3. Check if the database exists")
        return False

if __name__ == "__main__":
    success = test_connection()
    sys.exit(0 if success else 1)