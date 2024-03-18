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
        def run(self):
            while True:
                print("1. Add book")
                print("2. Add member")
                print("3. Issue Book")
                print("4. Return book")
                print("5. Exit")
                choice = input("Enter your choice: ")
                if choice == "1":
                    Bno = input("Enter book number: ")
                    title = input("Enter book title: ")
                    self.library.add_book(Bno, title)
                elif choice == "2":
                    id = input("Enter member id: ")
                    name = input("Enter member name: ")
                    self.library.add_member(Member(id, name))
                elif choice == "3":
                    Bno = input("Enter book number: ")
                    member_id = input("Enter member id: ")
                    self.library.issue_book(Bno, member_id)
                elif choice == "4":
                    Bno = input("Enter book number: ")
                    self.library.return_book(Bno)
                elif choice == "5":
                    break
Library = Library()
menu = MenuLib(Library)
menu.run()

