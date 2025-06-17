# define constants

pointer = 0

data = {
	"pointers":[],
	"stack":[]
}

tokens = {
	"printing":["print"],
	"ending":["end"]
}

conditiion = ""

code = ""
	
# define function

def function(token):
	global pointer
	global data
	global tokens
	global code
	global condition
	
	condition = ""
	pointer += 1
	if token in tokens["printing"]:
		return ""
		while condition != "ending":
			if code[pointer] != "\\":
				data["stack"].append(code[pointer]+" ")
			else:
				pointer += 1
				data["stack"].append(function(code[pointer])+"")
	elif token in tokens["ending"]:
		condition = "ending"
		return ""
	elif token in tokens["debug"]:
		print(f"Pointer: {pointer} \n Data: {data} \n Tokens:{tokens} Code:{code}")
				

# run BASE-Code Files
while input("Do you want to quit? Type y if yes") != "y":
	with open(str(input("What BASE Code file would you like to open? Type it here: \n")),"rt") as file:
		code = file.read()
		print("BASE Code: "+str(code))

# make code useable

	code = code.split()

# run the code

	while pointer > len(code):
		function(code[pointer])
