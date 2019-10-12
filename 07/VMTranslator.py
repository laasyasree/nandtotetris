class Parser:
	def __init__(self,inputfile):
		self.inputfile=open(inputfile,'r')
		self.line=[""]
		self.commands={
			"add" : "C_ARITHMETIC",
            "sub" : "C_ARITHMETIC",
            "neg" : "C_ARITHMETIC",
            "eq" : "C_ARITHMETIC",
            "gt" : "C_ARITHMETIC",
            "lt" : "C_ARITHMETIC",
            "and" : "C_ARITHMETIC",
            "or" : "C_ARITHMETIC",
            "not" : "C_ARITHMETIC",
            "pop": "C_POP",
            "push": "C_PUSH"
            }
       self.end= False
            
	def hasMoreCommands(self):
		if(self.end):
			return False
		else:
			return True
		
		
	def advance(self):
		a=self.inputfile.readline()
		if(a==""):
			self.end = True
		else:
			line=a.strip()
			components=line.split()
			
			
			
	def commandType(self):
		return self.commands.get(components[0],"invalid")
		
	def arg1(self):
		return self.components[1]
		
	def arg2(self):
		return self.components[2]
		
class CodeWriter:
	def __init__(self,outputfile):
		self.outputfile.open(outputfile,"w")
		
	def Close(self):
		self.outputfile.close()
		
	def writeArithmetic(self,components):
		smtg=""
		if(components=="add"):
			smtg+="@SP\n"
			smtg+="A=M-1\n"
			smtg+="D=M\n"
			smtg+="@SP\n"
			smtg+="A=M-1\n"
			smtg+="M=D+M\n"
			smtg+="@SP\n"
			smtg+="M=M+1\n"
			
		elif(components=="sub"):
			smtg+="@SP\n"
			smtg+="A=M-1\n"
			smtg+="D=M\n"
			smtg+="@SP\n"
			smtg+="A=M-1\n"
			smtg+="M=D-M\n"
			smtg+="@SP\n"
			smtg+="M=M+1\n"
			
		elif(components=="neg"):
			smtg+="@SP\n"
			smtg+="A=M-1\n"
			smtg+="M=-M\n"
			
		elif(components=="eq"):
			smtg+="@SP\n"
			smtg+="A=M-1\n"
			smtg+="D=M\n"
			smtg+="@SP\n"
			smtg+="A=M-1\n"
			smtg+="D=D-M\n"
			smtg+="@equal\n"
			smtg+="D;JEQ\n"
			
		elif(components=="gt"):
			smtg+="@SP\n"
			smtg+="A=M-1\n"
			smtg+="D=M\n"
			smtg+="@SP\n"
			smtg+="A=M-1\n"
			smtg+="D=D-M\n"
			smtg+="@greaterthan\n"
			smtg+="D;JGT\n"
			
		elif(components=="lt"):
			smtg+="@SP\n"
			smtg+="A=M-1\n"
			smtg+="D=M\n"
			smtg+="@SP\n"
			smtg+="A=M-1\n"
			smtg+="D=D-M\n"
			smtg+="@dc\n"
			smtg+="D;JLTn"
			
			
		
		

	
		
			
			
			
			
			
		
			
			
		
	

