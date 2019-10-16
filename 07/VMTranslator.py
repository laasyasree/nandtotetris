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
		count=0
		
	def close(self):
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
			self.count+=1
			c=str(self.count)
			smtg+="@SP\n"
			smtg+="A=M-1\n"
			smtg+="D=M\n"
			smtg+="@SP\n"
			smtg+="A=M-1\n"
			smtg+="M=-1\n"
			smtg+="D=D-M\n"
			smtg+="@equal"+c+"\n"
			smtg+="D;JEQ\n"
			smtg+="M=0\n"
			smtg+="(equal"+c+")\n"
			
		elif(components=="gt"):
			self.count+=1;
			c=str(self.count)
			smtg+="@SP\n"
			smtg+="A=M-1\n"
			smtg+="D=M\n"
			smtg+="@SP\n"
			smtg+="A=M-1\n"
			smtg+="M=-1\n"
			smtg+="D=D-M\n"
			smtg+="@gt"+c+"\n"
			smtg+="D;JGT\n"
			smtg+="M=0\n"
			smtg+="(gt"+c+")\n"
			
		elif(components=="lt"):
			self.count+=1
			c=str(self.count)
			smtg+="@SP\n"
			smtg+="A=M-1\n"
			smtg+="D=M\n"
			smtg+="@SP\n"
			smtg+="A=M-1\n"
			smtg+="M=-1\n"
			smtg+="D=D-M\n"
			smtg+="@lt"+c+"\n"
			smtg+="D;JLTn"
			smtg+="M=0\n"
			smtg+="(lt"+c+")\n"
			
		elif(components=="and"):
			smtg+="@SP\n"
			smtg+="A=M-1\n"
			smtg+="D=M\n"
			smtg+="@SP\n"
			smtg+="A=M-1\n"
			smtg+="M=D&M\n"
			
		elif(components=="or"):
			smtg+="@SP\n"
			smtg+="A=M-1\n"
			smtg+="D=M\n"
			smtg+="@SP\n"
			smtg+="A=M-1\n"
			smtg+="M=D|M\n"
		
		elif(components=="not"):
			smtg+="@SP\n"
			smtg+="A=M-1\n"
			smtg+="M=!M\n"
			
		else:
			smtg="invalid command"
			
		self.outputfile.write("//"+components+"\n"+smtg)
		
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
				smtg+="@"+outputfile[:-3]+"."+index+"\n"
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
				smtg+="A=M-1\n"
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
				smtg+="A=M-1\n"
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
				smtg+="A=M-1\n"
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
				smtg+="A=M-1\n"
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
				smtg+="A=M-1\n"
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
				smtg+="A=M-1\n"
				smtg+="D=M\n"
				smtg+="@R13\n"
				smtg+="A=M\n"
				smtg+="M=D\n"
				
			elif(segment=="static"):
				smtg+="@SP\n"
				smtg+="A=M-1\n"
				smtg+="D=M\n"
				smtg+="@"+outputfile[:-3]+"."+index+"\n"
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
		elif commands == "C_ARITHMETIC":
			codewriter.writeArithmetic(parser.components[0])
	codewriter.close()
	return 0

if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv)
