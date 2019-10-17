import os
class Parser:
	def __init__(self,inputfile):
		self.inputfile=open(inputfile,'r')
		self.components=[""]
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
		cursorPosition = self.inputfile.tell()
		self.advance()
		self.inputfile.seek(cursorPosition)
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
			if(line==""):
				self.advance()
			else:
				self.components=line.split() 
			
	def commandType(self):
		return self.components[0]
		
	def arg1(self):
		return self.components[1]
		
	def arg2(self):
		return self.components[2]
		
class CodeWriter:
	def __init__(self,outputfile):
		self.outputfile=open(outputfile,'w')
		self.count=0
		self.fn=outputfile[:-3]
		
	def close(self):
		self.outputfile.close()
		
	def writeArithmetic(self,component):
		smtg=""
		self.outputfile.write("//"+component+"\n")
		if(component =="add"):
			smtg+="@SP\n"
			smtg+="AM=M-1\n"
			smtg+="D=M\n"
			smtg+="@SP\n"
			smtg+="AM=M-1\n"
			smtg+="M=D+M\n"
			smtg+="@SP\n"
			smtg+="M=M+1\n"
			
		elif(component=="sub"):
			smtg+="@SP\n"
			smtg+="AM=M-1\n"
			smtg+="D=M\n"
			smtg+="@SP\n"
			smtg+="AM=M-1\n"
			smtg+="M=M-D\n"
			smtg+="@SP\n"
			smtg+="M=M+1\n"
			
		elif(component=="neg"):
			smtg+="@SP\n"
			smtg+="A=M-1\n"
			smtg+="M=-M\n"
			
		elif(component=="eq"):
			c=str(self.count)
			self.count+=1
			smtg+="@SP\n"
			smtg+="AM=M-1\n"
			smtg+="D=M\n"
			smtg+="@SP\n"
			smtg+="A=M-1\n"
			smtg+="D=M-D\n"
			smtg+="M=-1\n"
			smtg+="@equal"+c+"\n"
			smtg+="D;JEQ\n"
			smtg+="@SP\n"
			smtg+="A=M-1\n"
			smtg+="M=0\n"
			smtg+="(equal"+c+")\n"
			
		elif(component=="gt"):
			c=str(self.count)
			self.count+=1;
			smtg+="@SP\n"
			smtg+="AM=M-1\n"
			smtg+="D=M\n"
			smtg+="@SP\n"
			smtg+="A=M-1\n"
			smtg+="D=M-D\n"
			smtg+="M=-1\n"
			smtg+="@gt"+c+"\n"
			smtg+="D;JGT\n"
			smtg+="@SP\n"
			smtg+="A=M-1\n"
			smtg+="M=0\n"
			smtg+="(gt"+c+")\n"
			
		elif(component=="lt"):
			c=str(self.count)
			self.count+=1;
			smtg+="@SP\n"
			smtg+="AM=M-1\n"
			smtg+="D=M\n"
			smtg+="@SP\n"
			smtg+="A=M-1\n"
			smtg+="D=M-D\n"
			smtg+="M=-1\n"
			smtg+="@lt"+c+"\n"
			smtg+="D;JLT\n"
			smtg+="@SP\n"
			smtg+="A=M-1\n"
			smtg+="M=0\n"
			smtg+="(lt"+c+")\n"
			
		elif(component=="and"):
			smtg+="@SP\n"
			smtg+="AM=M-1\n"
			smtg+="D=M\n"
			smtg+="@SP\n"
			smtg+="A=M-1\n"
			smtg+="M=D&M\n"
			
		elif(component=="or"):
			smtg+="@SP\n"
			smtg+="AM=M-1\n"
			smtg+="D=M\n"
			smtg+="@SP\n"
			smtg+="A=M-1\n"
			smtg+="M=D|M\n"
		
		elif(component=="not"):
			smtg+="@SP\n"
			smtg+="A=M-1\n"
			smtg+="M=!M\n"
			
		else:
			smtg="invalid command"
			
		self.outputfile.write(smtg+"\n")
		
	def writePushPop(self,command,segment,index):
		smtg=""
		if(command=="push"):
			self.outputfile.write("//push "+segment+" "+str(index)+"\n")
			if(segment=="local"):
				smtg+="@"+index+"\n"
				smtg+="D=A\n"
				smtg+="@LCL\n"
				smtg+="A=M+D\n"
				smtg+="D=M\n"
				smtg+="@SP\n"
				smtg+="A=M\n"
				smtg+="M=D\n"
				smtg+="@SP\n"
				smtg+="M=M+1\n"
				
			elif(segment=="argument"):
				smtg+="@"+index+"\n"
				smtg+="D=A\n"
				smtg+="@ARG\n"
				smtg+="A=M+D\n"
				smtg+="D=M\n"
				smtg+="@SP\n"
				smtg+="A=M\n"
				smtg+="M=D\n"
				smtg+="@SP\n"
				smtg+="M=M+1\n"
				
			elif(segment=="this"):
				smtg+="@"+index+"\n"
				smtg+="D=A\n"
				smtg+="@THIS\n"
				smtg+="A=M+D\n"
				smtg+="D=M\n"
				smtg+="@SP\n"
				smtg+="A=M\n"
				smtg+="M=D\n"
				smtg+="@SP\n"
				smtg+="M=M+1\n"
				
			elif(segment=="that"):
				smtg+="@"+index+"\n"
				smtg+="D=A\n"
				smtg+="@THAT\n"
				smtg+="A=M+D\n"
				smtg+="D=M\n"
				smtg+="@SP\n"
				smtg+="A=M\n"
				smtg+="M=D\n"
				smtg+="@SP\n"
				smtg+="M=M+1\n"
				
			elif(segment=="temp"):
				smtg+="@"+index+"\n"
				smtg+="D=A\n"
				smtg+="@5\n"
				smtg+="A=A+D\n"
				smtg+="D=M\n"
				smtg+="@SP\n"
				smtg+="A=M\n"
				smtg+="M=D\n"
				smtg+="@SP\n"
				smtg+="M=M+1\n"
				
			elif(segment=="constant"):
				smtg+="@"+index+"\n"
				smtg+="D=A\n"
				smtg+="@SP\n"
				smtg+="A=M\n"
				smtg+="M=D\n"
				smtg+="@SP\n"
				smtg+="M=M+1\n"
				
			elif(segment=="pointer"):
				smtg+="@"+index+"\n"
				smtg+="D=A\n"
				smtg+="@3\n"
				smtg+="A=A+D\n"
				smtg+="D=M\n"
				smtg+="@SP\n"
				smtg+="A=M\n"
				smtg+="M=D\n"
				smtg+="@SP\n"
				smtg+="M=M+1\n"
				
			elif(segment=="static"):
				smtg+="@"+self.fn+"."+index+"\n"
				smtg+="D=M\n"
				smtg+="@SP\n"
				smtg+="A=M\n"
				smtg+="M=D\n"
				smtg+="@SP\n"
				smtg+="M=M+1\n"
				
			else:
				smtg="invalid"
			self.outputfile.write(smtg+"\n")
				
		elif(command=="pop"):
			smtg=""
			self.outputfile.write("//pop "+segment+" "+str(index)+"\n")
			if(segment=="local"):
				smtg+="@"+index+"\n"
				smtg+="D=A\n"
				smtg+="@LCL\n"
				smtg+="D=M+D\n"
				smtg+="@R13\n"
				smtg+="M=D\n"
				smtg+="@SP\n"
				smtg+="AM=M-1\n"
				smtg+="D=M\n"
				smtg+="@R13\n"
				smtg+="A=M\n"
				smtg+="M=D\n"
				
			elif(segment=="that"):
				smtg+="@"+index+"\n"
				smtg+="D=A\n"
				smtg+="@THAT\n"
				smtg+="D=M+D\n"
				smtg+="@R13\n"
				smtg+="M=D\n"
				smtg+="@SP\n"
				smtg+="AM=M-1\n"
				smtg+="D=M\n"
				smtg+="@R13\n"
				smtg+="A=M\n"
				smtg+="M=D\n"
				
			elif(segment=="this"):
				smtg+="@"+index+"\n"
				smtg+="D=A\n"
				smtg+="@THIS\n"
				smtg+="D=M+D\n"
				smtg+="@R13\n"
				smtg+="M=D\n"
				smtg+="@SP\n"
				smtg+="AM=M-1\n"
				smtg+="D=M\n"
				smtg+="@R13\n"
				smtg+="A=M\n"
				smtg+="M=D\n"
				
			elif(segment=="argument"):
				smtg+="@"+index+"\n"
				smtg+="D=A\n"
				smtg+="@ARG\n"
				smtg+="D=M+D\n"
				smtg+="@R13\n"
				smtg+="M=D\n"
				smtg+="@SP\n"
				smtg+="AM=M-1\n"
				smtg+="D=M\n"
				smtg+="@R13\n"
				smtg+="A=M\n"
				smtg+="M=D\n"
				
			elif(segment=="temp"):
				smtg+="@"+index+"\n"
				smtg+="D=A\n"
				smtg+="@5\n"
				smtg+="D=A+D\n"
				smtg+="@R13\n"
				smtg+="M=D\n"
				smtg+="@SP\n"
				smtg+="AM=M-1\n"
				smtg+="D=M\n"
				smtg+="@R13\n"
				smtg+="A=M\n"
				smtg+="M=D\n"
				
			elif(segment=="pointer"):
				smtg+="@"+index+"\n"
				smtg+="D=A\n"
				smtg+="@3\n"
				smtg+="D=A+D\n"
				smtg+="@R13\n"
				smtg+="M=D\n"
				smtg+="@SP\n"
				smtg+="AM=M-1\n"
				smtg+="D=M\n"
				smtg+="@R13\n"
				smtg+="A=M\n"
				smtg+="M=D\n"
				
			elif(segment=="static"):
				smtg+="@SP\n"
				smtg+="AM=M-1\n"
				smtg+="D=M\n"
				smtg+="@"+self.fn+"."+index+"\n"
				smtg+="M=D\n"
				
			else:
				smtg="invalid"
			self.outputfile.write(smtg)
				
def main(args):
	source = sys.argv[1]
	parser = Parser(source + ".vm")
	codewriter = CodeWriter(source + ".asm")

	while(parser.hasMoreCommands()):
		parser.advance()
		commands = parser.commandType()
		
		if commands =="push" or commands == "pop":
			codewriter.writePushPop(commands, parser.arg1(), parser.arg2())
		elif (commands =="add" or commands == "sub" or commands == "neg" or commands == "eq" or commands == "gt" or commands == "lt" or commands == "and"  or commands == "or" or commands == "not" ) :
			codewriter.writeArithmetic(parser.components[0])
	codewriter.close()
	return 0

if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv))
