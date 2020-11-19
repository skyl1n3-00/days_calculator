## Days calculator project
This project is written using Python, the idea of this project
 it's to calculate the number of days between two given dates.
<br>
This project doesn't have an interactive shell, which well ask
 you to give two dates and give you the result, the project is 
 a set of functions with their tests
  ([units tests file](days_calculator_tests.py)).
<br>
The main function of the project is `number_days_between_two_dates(date_1, date_2)`, 
and the other functions are just helper functions meant to 
simplify and organize the code, and every function has a docstring
inside to explain what it does.
<br>
The file [costume_exceptions.py](custom_exceptions.py) contains two 
exceptions two output same errors.

##### To use the function just import it from the file: 
```python
from days_calculator import number_days_between_two_dates
number_of_days = number_days_between_two_dates((1, 1, 1993), (31, 12, 1994))
```
##### To run the unit tests:
```shell script
 python3.7 -m unittest days_calculator_tests.py
```
or just 
```shell script
 python3.7 days_calculator_tests.py
```

