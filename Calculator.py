"""
This Python program takes a user input mathematical expression, parses it, and evaluates the result.
It supports basic arithmetic operations (+, -, *, /, %) and uses the "=" sign to indicate the end of the calculation.

Usage:
1. Enter a valid mathematical expression, e.g., "2*45*67-5=".
2. The program will parse the input, evaluate the expression, and display the result.
3. Process the expression following the left-to-right precedence of operations.

Example:
eg:1+2+3%6=
ENTER THE CALCULATION: 2*45*67-5=
Result= 6025.0

Author: Pranav

"""

input_string = input("ENTER THE CALCULATION: ")
operations=["+","-","*","/","%","="] 
count=0 
i=0
while i<len(input_string):
    if input_string[i] in operations:
        count=count+1
    i=i+1

digits=[]
operators=[]
for j in range(0,count):
    digits.append("")

i=0  
for j in range(0,count):
    while i<len(input_string) and input_string[i] not in operations:
        digits[j]=digits[j] + input_string[i]
        i=i+1 
    operators.append(input_string[i])
    digits[j]= float(digits[j])
    i=i+1

result= digits[0]
for i in range(0,len(operators)):

    if operators[i]=="+":
        result=result+digits[i+1]

    elif operators[i]=="-":
        result=result-digits[i+1]

    elif operators[i]=="*":
        result=result*digits[i+1]

    elif operators[i]=="/":
        result=result/digits[i+1]
        
    elif operators[i]=="%":
        result=result%digits[i+1]

print("Result= ",result)


'''
OUTPUT

eg:1+2+3%6=
ENTER THE CALCULATION: 2*45*67-5=
Result=  6025.0

eg:1+2+3%6=                                                                                                                                                     
ENTER THE CALCULATION: 1+2-3+4-9=
Result=  -5.0

eg:1+2+3%6=
ENTER THE CALCULATION: 1+2+3+4=
Result=  10.0
'''
