# Calculator
The basic functions and operation of the calculator are modelled after [Casio SL300VC-BE](https://www.casio.com/products/calculators/basic/sl300vc-be).

Here are some key aspects of the operations:
1. If any arithmetic button is pressed when there are already two numbers inputted the value will be calculated and stored onto num1 ie.. 2 + 2 + 2 + ...  will give a result
2. The sqrt button will output the sqrt of the number presenet on the screen (just like [Casio SL300VC-BE](https://www.casio.com/products/calculators/basic/sl300vc-be)) so 9 * 9 sqrt will yield 3 instead of 9 since it will perfom sqrt on the 9 present on the screen

Here are some key points about the code:
1. num1 is empty until an arithmetic opertation has been given.
2. num2 unlike num1 will immediately get the value on the screen. This has been done so that once num1 is set num2 is always ready to be calculated. 


Issuing this command can make this calculator an environment command sudo cp ./calc.sh /usr/bin/calc
