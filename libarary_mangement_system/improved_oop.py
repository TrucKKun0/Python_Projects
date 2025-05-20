def LMS():
    def __init__(self):
        self.books = []
        self.students = []
        self.borrowed_books = {}
        self.returned_books = []
    def add_book(self,book):
        self.books.append(book)
    def add_student(self,student):
        self.students.append(student)
    def borrow_book(self, book_id, student_id, borrowed_date):
        if student_id not in self.borrowed:
            self.borrowed[student_id]= []
        already_borrowed = any(entry["book_id"] == book_id for entry in self.borrowed[student_id])
        if already_borrowed:
            print(f"Book {book_id} is already borrowed by student {student_id}.")
        else:
            self.borrowed[student_id].append({"book_id": book_id, "date": borrowed_date})
            print(f"Book {book_id} borrowed by student {student_id} on {borrowed_date}.")

        



def book(self, book_id, book_name, book_author, admin):
    self.book_id = book_id
    self.admin = admin
    self.book_name = book_name
    self.book_author = book_author

def student(self, std_id, std_name, std_sem, std_batch, admin):
    self.std_id = std_id
    self.admin = admin
    self.std_name = std_name
    self.std_sem = std_sem
    self.std_batch = std_batch