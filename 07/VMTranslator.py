class Parser(self,inputfile):
	def __init__(self,inputfile):
		self.inputfile=open(inputfile,'r')
		self.command=[""]
		self.cursorAtEnd = False
		self.cType={
			"add" : "C_ARITHMETIC",
            "sub" : "C_ARITHMETIC",
            "neg" : "C_ARITHMETIC",
            "eq" : "C_ARITHMETIC",
            "gt" : "C_ARITHMETIC",
            "lt" : "C_ARITHMETIC",
            "and" : "C_ARITHMETIC",
            "or" : "C_ARITHMETIC",
            "not" : "C_ARITHMETIC",
            "push" : "push",
            "pop" : "pop",
            "EOF" : "C_EOF",
            }
	def hasMoreCommands(self):
		
		
	def advance(self):
		line=self.inputfile.readline()
		if(line==""):
			self.cursorAtEnd = True
		else:
			
			
			
			
			
		
			
			
		
	

