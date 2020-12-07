"""library for working with files"""

class files:
    """to work with extraction, writing of data etc.
    to & fro from a file"""
    
    def __init__(self, fn=None):
        if fn == None:
            print("please provide a valid filename")
        else:
            self.filename = fn
    
    def read_column(self, col=0):
        """method for extracting a column
        provide a valid column number, 0 will be assumed by default"""
        with open(self.filename, "r") as fc:
            strc = fc.read()  
            
        listc = strc.splitlines()
        column = []

        for line in listc:
            temp = line.split()
            column.append(temp[col])
        return column
    
    def __add__(self, other):
        a = self.filename
        a = a.replace(".txt", "_")
        b = other.filename
        
        fa = open(self.filename, "r")
        fb = open(other.filename, "r")
        fc = open(a+b, "w")
        
        stra = fa.read()
        strb = fb.read()
        
        fc.write(stra)
        fc.write("\n")
        fc.write(strb)
        
        fa.close()
        fb.close()
        fc.close()
    