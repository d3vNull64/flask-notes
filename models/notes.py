from instance.db import get_db_connection


class Notes:
    @classmethod
    def get_all_notes(cls):
        # This function return all notes saved in database
        conn = get_db_connection()
        query = "SELECT * FROM notes"
        curs = conn.cursor()
        curs.execute(query)
        notes = curs.fetchall()
        conn.close()
        return notes

    @classmethod
    def reset_notes(cls):
        query1 = "DELETE FROM notes"
        query2 = "DELETE FROM sqlite_sequence WHERE name = 'notes'"
        with get_db_connection() as conn:
            conn.execute(query1)
            conn.execute(query2)

    @classmethod
    def selected_false_all(cls):
        # This function set to false all selected field in notes table
        query = "UPDATE notes SET selected=0 WHERE selected=1"
        with get_db_connection() as conn:
            conn.execute(query)

    @classmethod
    def get_selected_note(cls):
        # This function returns selected note
        query = "SELECT * FROM notes WHERE selected=1"
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            selected = cursor.fetchall()
            return selected

    @classmethod
    def mark_as_selected(cls, id):
        cls.selected_false_all()
        query = f"UPDATE notes SET selected=1 WHERE id={id}"
        with get_db_connection() as conn:
            conn.execute(query)

    @classmethod
    def add_note(cls, title):
        # This function insert the new note to dabatabe
        cls.selected_false_all()
        query = f"""INSERT INTO notes (title, content, selected) VALUES ('{title}', '', 1)"""
        with get_db_connection() as conn:
            conn.execute(query)

    @classmethod
    def update_note(cls, id, title, content):
        query = f"UPDATE notes SET title='{title}', content='{content}' WHERE id={id}"
        with get_db_connection() as conn:
            conn.execute(query)

    @classmethod
    def delete_note(cls, id):
        query = f"DELETE FROM notes WHERE id={id}"
        with get_db_connection() as conn:
            conn.execute(query)
