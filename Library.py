import mysql.connector

class Book:
    def __init__(self, Bno, title):
        self.Bno = Bno
        self.title = title
        self.is_issued = False

class Member:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Issue:
    def __init__(self, book, member):
        self.book = book
        self.member = member
        self.due_date = None

class Library:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password = "Phenomenal2003_",
            database = "library"
        )
        self.cursor = self.conn.cursor()

    def add_book(self, book):
        self.cursor.execute("INSERT INTO books VALUES(%s, %s, %s)",
                            (book.Bno, book.title, book.is_issued))
        self.conn.commit()

    def add_member(self, member):
        self.cursor.execute("INSERT INTO members VALUES (%s, %s)", (member.id, member.name))
        self.conn.commit()

    def issue_book(self, Bno, member_id):
        self.cursor.execute("UPDATE books SET is_issued = True WHERE Bno = %s", (Bno,))
        self.conn.commit()
        self.cursor.execute("INSERT INTO issues(book_id, member_id) VALUES (%s, %s)", (Bno, member_id))
        self.conn.commit()
    def return_book(self, Bno):
        self.cursor.execute("UPDATE books SET is_issued = False WHERE Bno = %s", (Bno,))
        self.conn.commit()
        self.cursor.execute("DELETE FROM issues WHERE book_id = %s", (Bno,))
        self.conn.commit()
    class MenuLib:
        def __init__(self, library):
            self.library = library
        

