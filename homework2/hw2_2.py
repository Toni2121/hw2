number1: float = float(input("please enter a Decimal number: "));
number2: float = float(input("please enter another Decimal number: "));
diff: float = float(number1 - number2);
if diff > 0:
    print("The differnce is ", diff);
else:
    print("The differnce is ", -diff);