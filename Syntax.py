def create_student():
    """
    Create and return a dictionary representing a student.

    Requirements:
    - name (string)
    - age (integer)
    - marks (list of 5 integers)

    Return the dictionary.
    """
    return { "name" : "",
             "age" : 0,
             "marks" : [0,0,0,0,0]

    }


def calculate_average(marks):
    """
    Calculate the average of the marks list.

    Requirements:
    - Return the average as a float
    - Handle empty list (return 0)
    """
    if len(marks) == 0:
        return 0
    average = sum(marks) / len(marks)
    return average



def get_grade(average):
    """
    Return grade based on average:

    75+  -> "Distinction"
    60+  -> "Pass"
    50+  -> "Supplementary"
    below 50 -> "Fail"
    """
    if average >= 75:
        return "Distinction"
    elif average >= 60 and average <= 74:
        return "Pass"
    elif average >= 50 and average <= 59:
        return "Supplementary"
    else:
        return "Fail"


def clean_numbers(values):
    """
    Given a list that may contain numbers as STRINGS,
    convert everything to integers.

    Example:
    ["10", 20, "30"] -> [10, 20, 30]

    """
def clean_numbers(values):
    ls = []
    for i in values:
        try:
            ls.append(int(i))
        except (ValueError, TypeError):
            pass   # skip values that can't be converted
    return ls

print(clean_numbers(["10", 20, "30", "bad", 40.5]))

def even_numbers_only(numbers):
    """
    Return a NEW list containing only even numbers.
    Use a loop (not list comprehension).
    """
    new_list = []
    for i in numbers:
        if i % 2 == 0:
            new_list.append(i)
    return new_list