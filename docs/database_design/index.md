# Database Implementation Strategies

## Suggested Framework for Database Scripts and Workflow

1. **Folder Structure**
   Organize your database scripts into a dedicated folder for version-controlled migrations:

   ```plaintext
   project/
   ├── database/
   │   ├── migrations/
   │   │   ├── 001_initial.sql
   │   │   ├── 002_add_new_columns.sql
   │   │   ├── 003_other_changes.sql
   │   ├── schema_tracker.json  # Tracks applied migrations
   │   └── migration_runner.py  # Handles execution of migrations
   ├── main.py
   ├── requirements.txt
   └── README.md
   ```

2. **Migration Workflow**
   - Store individual `.sql` files in the `migrations/` folder, each containing specific database changes.
   - Use a script (`migration_runner.py`) to check which migrations have been applied and apply only new ones.

3. **`schema_tracker.json` Example**
   A simple JSON file to track applied migrations:

   ```json
   {
       "applied_migrations": [
           "001_initial.sql",
           "002_add_new_columns.sql"
       ]
   }
   ```

4. **Migration Runner Script**
   Create a Python script to apply new migrations:

   ```python
   import sqlite3
   import os
   import json

   # Database file name
   db_name = "video_metadata.db"
   migration_folder = "database/migrations"
   schema_tracker_file = "database/schema_tracker.json"

   def get_applied_migrations():
       """Read applied migrations from the schema tracker file."""
       if not os.path.exists(schema_tracker_file):
           return []
       with open(schema_tracker_file, "r") as f:
           return json.load(f).get("applied_migrations", [])

   def save_applied_migrations(migrations):
       """Save applied migrations to the schema tracker file."""
       with open(schema_tracker_file, "w") as f:
           json.dump({"applied_migrations": migrations}, f, indent=4)

   def apply_migrations():
       """Apply new migrations to the SQLite database."""
       connection = sqlite3.connect(db_name)
       cursor = connection.cursor()

       try:
           # Get all migration files and applied migrations
           migration_files = sorted(os.listdir(migration_folder))
           applied_migrations = get_applied_migrations()

           new_migrations = [
               f for f in migration_files if f not in applied_migrations
           ]

           if not new_migrations:
               print("No new migrations to apply.")
               return

           for migration in new_migrations:
               with open(os.path.join(migration_folder, migration), "r") as f:
                   sql = f.read()
                   cursor.executescript(sql)  # Execute the migration script
                   print(f"Applied migration: {migration}")

               applied_migrations.append(migration)

           # Save updated applied migrations
           save_applied_migrations(applied_migrations)
           connection.commit()
       except sqlite3.Error as e:
           print(f"Error applying migrations: {e}")
       finally:
           connection.close()

   if __name__ == "__main__":
       apply_migrations()
   ```

5. **Example Migration File**
   Save your SQL schema as `001_initial.sql` in `database/migrations/`:
  
    ```sql
   CREATE TABLE IF NOT EXISTS videos (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       file_name TEXT NOT NULL,
       file_path TEXT NOT NULL UNIQUE,
       file_size INTEGER,
       created_at TIMESTAMP,
       modified_at TIMESTAMP,
       duration REAL,
       resolution TEXT,
       frame_rate REAL,
       codec TEXT,
       bitrate INTEGER,
       thumbnail_path TEXT
   );
   ```

---

### **Workflow**

1. Add new `.sql` files to `database/migrations/` for each database change.

2. Run the migration runner script:

   ```bash
   python database/migration_runner.py
   ```

3. The script will:
   - Check the `schema_tracker.json` file for applied migrations.
   - Apply only the new migrations in order.
   - Update `schema_tracker.json` to track the latest state.

---

### **Advantages**

- **Version Control:** Each migration is a separate file, making changes traceable.
- **Idempotence:** Migrations are applied only once, ensuring a consistent database state.
- **Portability:** Works seamlessly with SQLite and can be adapted for other databases like PostgreSQL.

---

## Alembic - An Introduction

### **Key Features of Alembic**

1. **Versioning:** Tracks each migration with a unique identifier.
2. **Rollback Support:** Allows reversing changes if needed.
3. **Database Independence:** Works with multiple database backends supported by SQLAlchemy (e.g., SQLite, PostgreSQL, MySQL).
4. **Script Generation:** Automatically generates migration scripts based on changes in your SQLAlchemy models.
5. **Custom Scripts:** Allows you to write custom SQL migrations if needed.

---

### **How Alembic Works**

Alembic operates on a version-controlled system:

1. **Migration Script Creation:** Each migration is a Python script stored in a `versions/` folder.
2. **Database State Management:** Alembic uses a table (typically named `alembic_version`) to track which migrations have been applied.
3. **Commands:** Alembic provides commands to upgrade, downgrade, or inspect the database schema.

---

### **Setting Up Alembic**

#### 1. **Install Alembic**

Install Alembic via pip:

```bash
pip install alembic
```

---

#### 2. **Initialize Alembic**

Run the initialization command in your project directory:

```bash
alembic init alembic
```

This creates the following structure:

```plaintext
alembic/
├── versions/         # Folder for migration scripts
├── env.py            # Configures database connection and migration behavior
├── README            # Description of Alembic
└── script.py.mako    # Template for generating migration scripts
alembic.ini           # Main configuration file
```

---

#### 3. **Configure Alembic**

Edit the `alembic.ini` file to set your database connection string:

```ini
sqlalchemy.url = sqlite:///video_metadata.db
```

In `env.py`, Alembic generates migrations based on your SQLAlchemy models. Locate the `target_metadata` variable and point it to your `Base` metadata:

```python
from your_project.models import Base

# Replace None with your SQLAlchemy metadata object
target_metadata = Base.metadata
```

---

#### 4. **Create a Migration Script**

Generate a new migration script:

```bash
alembic revision --autogenerate -m "Initial migration"
```

- **Autogenerate:** Alembic inspects your SQLAlchemy models and generates a migration script to match them.
- **Migration Script:** The script is saved in the `versions/` folder and looks like this:

  ```python
  from alembic import op
  import sqlalchemy as sa

  # Revision identifiers, used by Alembic.
  revision = 'abcd1234'  # Unique ID for the migration
  down_revision = None   # ID of the previous migration (None for the first migration)

  def upgrade():
      op.create_table(
          'videos',
          sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
          sa.Column('file_name', sa.String(), nullable=False),
          sa.Column('file_path', sa.Text(), nullable=False, unique=True),
          sa.Column('file_size', sa.Integer()),
          sa.Column('created_at', sa.TIMESTAMP()),
          sa.Column('modified_at', sa.TIMESTAMP()),
          sa.Column('duration', sa.Float()),
          sa.Column('resolution', sa.String()),
          sa.Column('frame_rate', sa.Float()),
          sa.Column('codec', sa.String()),
          sa.Column('bitrate', sa.Integer()),
          sa.Column('thumbnail_path', sa.Text())
      )

  def downgrade():
      op.drop_table('videos')
  ```

---

#### 5. **Apply the Migration**

Run the migration to update your database schema:

```bash
alembic upgrade head
```

- **Upgrade:** Applies all unapplied migrations.
- **Head:** Refers to the latest migration in the `versions/` folder.

---

#### 6. **Rollback a Migration**

If you need to undo a migration, use:

```bash
alembic downgrade -1
```

This reverts the most recent migration. You can also specify a specific revision ID to rollback to.

---

### **Advantages of Alembic**

1. **Database Agnostic:** Works with SQLite, PostgreSQL, MySQL, etc.
2. **Integration with SQLAlchemy:** Tight coupling makes migrations easier.
3. **Autogenerate:** Reduces manual effort for creating migration scripts.
4. **Version Control:** Tracks database state changes effectively.
5. **Customizable:** Supports raw SQL for edge cases.

---

### **When to Use Alembic**

- **Complex Projects:** Ideal for projects requiring frequent schema updates.
- **SQLAlchemy Projects:** If you're using SQLAlchemy, Alembic is the go-to choice for managing migrations.
- **Production Systems:** Provides confidence in making and rolling back schema changes.
