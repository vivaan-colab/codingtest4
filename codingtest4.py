class Book:
    def __init__(self,title,author,is_borrowed):
        self.title=title
        self.author=author
        self.is_borrowed=is_borrowed
    def borrow(self,is_borrowed):
        self.is_borrowed=is_borrowed
        
        if self.borrowed=="true":
          print("confirmed")
        else:
            print("false")
    def return_book(self):
        if self.is_borrowed=="false":
            print("confirmed")
        else:
            print("not valid")
book=Book()
book.__init__("the bobbit","vivaan","true")
book.borrow()
book.return_book()



    


           


    
