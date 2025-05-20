class LMS:
    def __init__(self, student_id, book_id):
        
        self.student_id = student_id 
        self.book_id = book_id
    
    def add_book(self,book_id,book_name,book_author,admin):
        self.book_id = book_id
        self.admin = admin
        self.book_name = book_name
        self.book_author = book_author
    def add_student(self,std_id,std_name,std_sem,std_batch,admin):
        self.std_id = std_id
        self.admin = admin
        self.std_name = std_name
        self.std_sem = std_sem
        self.std_batch = std_batch


class borrowed_book(LMS):
    def __init__(self,std_id,book_id,borrowed_date):
        super().__init__(book_id,std_id)
        self.borrowed_date = borrowed_date
class returned_book(LMS):
    def __init__(self,std_id,book_id,returned_date):
        super().__init__(book_id,std_id)
        self.returned_date = returned_date
        