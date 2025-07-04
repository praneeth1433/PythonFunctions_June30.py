#1. Create a Calculator — Use functions for operations like add, subtract, multiply, divide.

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if b == 0:
        return 'error! Division by zero'
    return a/b

def power(a,b):
    return a**b

print('select Operation: +, -, *, /, **')
operation = input("enter operation: ")
a = float(input("enter a: "))
b = float(input("enter b: "))

if operation == '+':
    print('sum is :', add(a,b))
elif operation == '-':
    print('sub is :', sub(a,b))
elif operation == '*':
    print('mul is :', mul(a,b))
elif operation == '/':
    print('div is :', div(a,b))
elif operation == '**':
    print('power is :', power(a,b))
else:
    print('Operator is not available')


#2. Student Management System — Use keyword and default arguments to input student data.

def studentData(name,age,grade,school='high School',):
    student={
        'name':name,
        'age':age,
        'grade':grade,
        'school':school,
    }
    return student

s1=studentData('praneeth',22,'A')
s2=studentData(name='ram',age=22,grade='B',school='high School')
print(s1)
print(s2)



def studentInfo(**kwargs):
    print('student details:')
    for key, value in kwargs.items():
        print(key, '=', value)

studentInfo(name='praneeth',age=25,grade='A',city='hyderabad')


#3. Invoice Generator — Use return functions and lambda to apply discounts and calculate totals.

applyDiscount = lambda total,discount: total - (total*discount/100)

def getTotalCost(price,quantity):
    return price*quantity

total=getTotalCost(price=10,quantity=5)
finalTotal= applyDiscount(total,discount=10)

print(total)
print(finalTotal)


#4. Dynamic Greetings System — Use arbitrary arguments to greet multiple users.

def greetingUsers(*names,message='Congratulations!'):
    for name in names:
        print(name,message)

names =['ram','kumar','praneeth']
greetingUsers(*names)

greetingUsers('raj','sekar')


#5.Recursive Task — Write a function to compute Fibonacci numbers recursively.

def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(5))


#6. Data Processor — Use *args and **kwargs to handle dynamic data fields.

def dataProcessor(*args,**kwargs):
    print('args :',args)
    print('kwargs :', kwargs)

dataProcessor(1,'praneeth',"webD",salary=50000,city='hyderabad')


#7. Lambda Sorting — Use lambda to sort a list of dictionaries by a specific key.

std = [
    {'name':'praneeth','age':22,'score':500},
    {'name':'ram','age':12,'score':600},
    {'name':'raj','age':18,'score':700},
    {'name':'sekar','age':20,'score':800},
    {'name':'kumar','age':17,'score':900},
]

sortbyScore = sorted(std, key=lambda x:x['score'], reverse=True)

for i in sortbyScore:
    print(i)

#8. Quiz Application — Functions to ask questions, validate answers, and keep score.

def askQuestion(question,answer):
    user_answer = input(question+'  ')
    if user_answer.lower() == answer.lower():
        print('Correct!')
        return 1
    else:
        print('WRONG!')
        return 0

def quiz():
    score = 0

    score+= askQuestion('1.which year is this :','2025')
    score+= askQuestion('2.what is the square root of 5 :','25')
    score+= askQuestion('3.what is the least number :','0')
    score+= askQuestion('4.what is the colour of moon :','white')
    print('your score is :',score)

quiz()


#9. String Analyzer — Function that counts vowels, consonants, spaces, and symbols.

def stringAnalyzer(text):
    vowels = 0
    consonants = 0
    spaces = 0
    symbols = 0

    for char in text:
        if char.lower() in 'aeiou':
            vowels += 1
        elif char.isalpha():
            consonants += 1
        elif char.isspace():
            spaces += 1
        else:
            symbols += 1

    print('vowels :', vowels)
    print('consonants :',consonants)
    print('spaces :',spaces)
    print('symbols :',symbols)

stringAnalyzer('hello! how are you?')


#10. Bank Transaction System — Simulate deposits and withdrawals using functions and return values.

balance = 10000
pin = "9999"

def checkPin():
    entered = input('enter pin :')
    return entered == pin

def deposit(amount):
    if checkPin():
        global balance
        balance = balance + amount
        print('Deposited amount is :',amount)
        print('Your total balance is :',balance)
    else:
        print('You entered wrong PIN,Try again')


def withdraw(amount):
    if checkPin():
        global balance
        if amount <= balance:
            balance = balance - amount
            print('Withdrawn amount is :',amount)
            print('Your total balance is :', balance)
        else:
            print('Not enough balance')

    else:
         print('You entered wrong PIN,Try again')

def checkBalance():
    if checkPin():
        print('Your balance is :',balance)
    else:
        print('You entered wrong PIN,Try again')


withdraw(500)


'''
Global variable: If we need to modify a variable inside the function
which was written in out of the function, we need to use global variable in the function
other wise it treats as local variable

'''
