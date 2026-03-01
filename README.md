# Day7
Still Basic syntax
## `create_student()`
```python
def create_student():                    # Function definition with no parameters
    return { "name" : "",               # Creates dict with "name" key, empty string value
             "age" : 0,                 # Adds "age" key with integer 0
             "marks" : [0,0,0,0,0]      # Adds "marks" key with list of 5 zeros
    }                                   # Returns the complete dictionary
```

## `calculate_average(marks)`
```python
def calculate_average(marks):            # Function takes a list of marks as parameter
    if len(marks) == 0:                 # Check if the list is empty
        return 0                        # If empty, return 0 (prevents division by zero)
    average = sum(marks) / len(marks)   # Sum all marks and divide by count to get average
    return average                      # Return the calculated average value
```

## `get_grade(average)`
```python
def get_grade(average):                 # Function takes an average (float) as parameter
    if average >= 75:                   # If average is 75 or above
        return "Distinction"            # Return this grade
    elif average >= 60 and average <= 74:  # Else if average is 60-74
        return "Pass"                   # Return this grade
    elif average >= 50 and average <= 59:  # Else if average is 50-59
        return "Supplementary"          # Return this grade
    else:                               # Otherwise (below 50)
        return "Fail"                   # Return this grade
```

## `even_numbers_only(numbers)`
```python
def even_numbers_only(numbers):         # Function takes a list of numbers as parameter
    new_list = []                       # Create an empty list to store even numbers
    for i in numbers:                   # Loop through each number in the input list
        if i % 2 == 0:                  # Check if number is even (remainder is 0 when divided by 2)
            new_list.append(i)          # If even, add it to the new list
    return new_list                     # Return the list containing only even numbers
```