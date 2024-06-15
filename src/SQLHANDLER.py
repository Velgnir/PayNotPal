import sqlite3
import os
import re

class SQLHANDLER:
    def __init__(self, db_path='example.db'):
        try:
            self.connection = sqlite3.connect(db_path)
            self.cursor = self.connection.cursor()
            print("Connection to SQLite established!")
        except sqlite3.Error as e:
            print(f"Error connecting to SQLite: {e}")
            self.connection = None

    def __del__(self):
        if self.connection:
            self.connection.close()
            print("SQLite connection closed.")

    def list_tables(self):
        try:
            self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = self.cursor.fetchall()
            return [table[0] for table in tables]
        except sqlite3.Error as e:
            print(f"Error listing tables: {e}")
            return []
    def create_table(self,name,vals):
        try:
            self.cursor.execute(f'''
                CREATE TABLE IF NOT EXISTS {name} (
                    {','.join(vals)}
                )
            ''')
            self.connection.commit()
            print(f"{name} table created successfully!")
        except sqlite3.Error as e:
            print(f"Error creating {name} table: {e}")
            print(f'''
                CREATE TABLE IF NOT EXISTS {name} (
                    {','.join(vals)}
                )
            ''')

    def _validate_column_definition(self, col_def):
        column_regex = re.compile(
            r'^\s*[\w]+[\s]+[\w]+(\s+(PRIMARY KEY|NOT NULL|UNIQUE|AUTOINCREMENT|FOREIGN KEY.*))?\s*$', re.IGNORECASE)
        if not column_regex.match(col_def):
            raise ValueError(f"Invalid column definition: {col_def}")
        if "FOREIGN KEY" in col_def.upper():
            foreign_key_regex = re.compile(r'FOREIGN\s+KEY\s+\([\w]+\)\s+REFERENCES\s+[\w]+\s+\([\w]+\)', re.IGNORECASE)
            if not foreign_key_regex.search(col_def):
                raise ValueError(f"Invalid foreign key definition: {col_def}")
    def display_table(self, table_name):
        try:
            self.cursor.execute(f"SELECT * FROM {table_name}")
            rows = self.cursor.fetchall()
            if not rows:
                print(f"No data found in table '{table_name}'")
                return

            column_names = [description[0] for description in self.cursor.description]

            column_widths = [len(col) for col in column_names]
            for row in rows:
                column_widths = [max(len(str(row[i])), column_widths[i]) for i in range(len(row))]

            header = " | ".join([col.ljust(column_widths[i]) for i, col in enumerate(column_names)])
            print("-" * (len(header) + 3))
            print(f"| {header} |")
            print("-" * (len(header) + 3))

            for row in rows:
                row_str = " | ".join([str(row[i]).ljust(column_widths[i]) for i in range(len(row))])
                print(f"| {row_str} |")
            print("-" * (len(header) + 3))

        except sqlite3.Error as e:
            print(f"Error displaying table '{table_name}': {e}")

        def drop_table(self, table_name):
            try:
                self.cursor.execute(f'DROP TABLE IF EXISTS {table_name}')
                self.connection.commit()
                self._print_with_clear(f"Table {table_name} deleted successfully!")
            except sqlite3.Error as e:
                self._print_with_clear(f"Error deleting table {table_name}: {e}")

        def delete_row(self, table_name, condition):
            try:
                self.cursor.execute(f'DELETE FROM {table_name} WHERE {condition}')
                self.connection.commit()
                self._print_with_clear(f"Rows from {table_name} deleted where {condition}")
            except sqlite3.Error as e:
                self._print_with_clear(f"Error deleting rows from {table_name}: {e}")