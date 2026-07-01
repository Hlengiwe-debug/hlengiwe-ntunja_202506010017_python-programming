1.1 Class- A blueprint for creating objects. It defines attributes(data) and methods (behaviour) and all instances will have.

1.2 Method- A function defined inside a class. It operates on instances of that clasds and can access instance data via 'self'.

1.3 Constructor- A special method '__int__()' that is automatically called when a new object is instantiated. It initializes the objects state.

1.4 Destructor- A special methos '__del__()' that is called when an object is about to be destroyed. It performs cleanup.

1.5 Class Method- A method bound to the class rather than the instance. It receives the cl;ass as the first argument ('cls'). Defined with '@classmethod'.

1.6 Static Method- A method that does not receive an implicit first argument (neither 'self' not 'cls'). Defined with '@staticmethod'. It behaves like a plain function but belongs to the class namespace.

1.7 Property- An attricute like accessor created with the '@property' decorator. It allows methods to be accessed as if they were attributes, enabling computed values and validation.

1.8 Decorator- A function that takes another function or class as an argument and extends or modifies its behaviour without changing its source code. Used with the '@' syntax.

1.9 Metaclass Method- The class of a class. It defines how a class behaves.The default metaclass in Python is 'type'.

1.10 Metaclass Method- A method defined inside a metaclass.It is invoked on the class itself(not on intances) and can customis class creation.

1.11 Class Variable- A variable that is shared across all instances of a class.It is defined inside the class but outside any method.

##Cafe Bill Program Analysis
## 1.1 Problem Statement
The cafe wants a simple program that automatically calculates a customers bilol based on the quantities of Coffee.Tea, and Sandwhich orded. The program should display a clear receipt.

## 1.2 Inputs
-Customer name (string)
-Number of Teas ordered (integer)
-Number of Sandwiches orded (integer)

## 1.3 Outputs
A receipt shpwing:
-Customer name 
-Quantity of each item
-Total bill amount (RM) formatted to two decimal places

## 1,4 Typical Process Flow
1. Prompy thje cashier for the customer name
2. Prompt for the quantity of each item.
3. Calculate the total:
 'total = cofee * 8.50 + tea * 6.00 + sandwhich * 12.00'
4. Print the receipt with all details.

## 1.5 Constraints
- Prices are fixed (*Cofee = RM8.50, Tea = RM6.00, Sandwhich = RM12.00).
- Quantities must be non-negative integers
- The total amount must be displayed with two decimal places.

## Decompostion into Smaller Tasks
1. Input handling - Get customer name and quantites from the user.
2. Business logic - Compute the total Bill.
3. Output- Format and print the receipt.
4. Seperation of concern- Keep calculation and printing in a seperate module ('utils.py') and the user-facing code in 'main.py'.

## Pseudeocode

BEGIN
PRINT "Enter customer name."
READ customer
PRINT "Enter number of coffee."
READ cofee 
PRINT "Enter number of tea."
READ tea
PRINT "Enter number of sandwhich."
READ sandwhich


total = coffee & 8.50 + tea * 6.00 + sandwhich * 12.00

PRINT "===== RECIEPT ===="
PRINT "Customer:" , customer
PRINT "Coffee:", cofee
PRINT "Tea:", tea
PRINT "Sandwhich:", sanwhich
PRINT "Total - RM", total (with 2 decimal places)

END

--- 

## Source Code
##  'utils.py'
Srr the seperate Python file.

## 'main.py"
See the seperate Python file.
