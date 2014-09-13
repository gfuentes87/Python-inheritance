from Book import Book
'''
Created on Sep 13, 2014

@author: Gus
'''

class HistoryBook(Book):
    
    def __init__(self, name, author, year):
        Book.__init__(self, name, author)
        self.year = year
        
    
    def displayCompleteInfo(self):
        print Book.getBasicInformation(self)+", Year: "+str(self.year)
