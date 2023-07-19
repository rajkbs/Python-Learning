# Python-Learning

## List of Topics
	1. Introduction to Python
	2. Python Variables and Token
	3. Python Data Types
	4. Conditional and Loop Statement
	5. Function in Python
	6. File Handling in Python
	7. Python Arrays
  
  ## 1. Introduction to Python
  It is an object-oriented, interpreted, high-level programming language. It is used to develop GUI and web applications.

	1. Python is simple and easy to learn.
	2. it has a lot of libraries.
	3. it is reliable, efficient, and time-saving
	4. it has a large active open-source community 
  
  ## 2. Python Variables
  The variable is a memory location where data can be stored, in python, the data type will be 	identified according to the data used. A variable starts with a letter or an underscore and cannot start with numbers, there are two 	ways of assigning values to a variable.
	
  	1. Assigning a value [click](https://github.com/rajkbs/Python-Learning/blob/master/Variable/f01.py)
	2. Multiple assignments
 
### Assigning a single value to a variable

	num = 10
	name = "Raj Kumar"
	code = 2000.23
	
	print(num)
	print(name)
	print(code)

### Assigning multiple values

	a=b=c=10
	x, y, z = 10, 20, 30
	print("a :",a)
	print("b :",b)
	print("c :",c)
	print("x :",x)
	print("y :",y)
	print("z :",z)

### Python Token

	Every logical line of code is broken into components known as Tokens

	_Token types:_
       		
	1. Keywords
	2. Identifiers
	3. Literals
	4. Operators

### Keyword:

	1. Special reserved words
	2. It gives special meaning to the compiler/interpreter as well as for specific operation
	3. NEVER use it as a variable.

### Identifier:

	An identifier is a name used to identify a variable, function, class, or object.

	_Rules:_

	1. No special character, except underscore(_), can be used as an identifier.
	2. Keywords should not be used as identifiers.
	3. Python is a case-sensitive language.
	4. The first character of an identifier can be an alphabet or underscore (_) but not a digit.

### Literals:

	Literals are the raw data given to a variable

	_Various Types:_

 	1. String Literals
		
		_String Literals_
  
		name = "Raj Kumar"
		Name = 'Raj Kumar'
		namE = '''Raj Kumar'''
	
		#'''  ''' can be used for multi-line string literals

		print("with double quote :",name)
		print("with single quote :",namE)
		print("with three quote :",Name)
		
	2. Numeric Literals

		1. Integer
		2. Long
		3. Float
		4. Complex

		#Numeric Literals

		mobileNo = 90909090909
		salary = 89000.75

		print("Mobile No :", mobileNo)
		print("Salary :", salary)
		print("Data Type :",type(mobileNo))
		print("Data Type :",type(salary))

	3. Boolean Literals

		True or False

	4. Specific Literals

		There is a special literal in Python called **None** which means that the variable is yet to be initialized.

		#Special Literals

		_name = None
		print(_name)

### Operators:

	Operators are special symbols that are used to carry out arithmetic and logical operations.

	_Arithmetic:_

	+  	Addition
	-  	Subtraction
	*  	Multiplication
 	/  	Division
	%  	Modulus
	** 	Exponentiation	

	_Assignment:_

	Used to assign values to variables

	=  	X=15
	+=  	X=X+15
	-=  	X=X-10
 	*=  	X=X*10
	/=  	X=X/4
	|= 	X=X|5

	_Comparison:_

	==	Equal
	!=	Not Equal
	<	Less Than	
	>	Greater Than
	>=	Greater Than or Equal To
	>=	Less Than or Equal To

	_Logical:_

	Used to combine conditional statements

	and	True if both statements are true.
	or	True if one of the statements is True.
	not	If True, then returns False.

		**and** operator
		num = 20
		if num <= 20 and num == 20:
	    		print("matched")
		else:
	    		print("not matched")

		**or** operator
		num = 20
		if num < 20 or num == 20:
	    		print("matched")
		else:
	    		print("not matched")

	_Bitwise:_

	Used to compare the binary number

		&	AND
		
		1 & 1 = 1
		1 & 0 = 0
		0 & 1 = 0
		0 & 0 = 0

		|	OR

		1 | 1 = 1
		1 | 0 = 1
		0 | 1 = 1
		0 | 0 = 0

	1. ^	XOR
	2. ~	NOT
	3. <<	Left Shift
	4. >>	Right Shift

		num = bin(8)
		print(num)
	
		Identity
		Membership

	
  
  
  
  
