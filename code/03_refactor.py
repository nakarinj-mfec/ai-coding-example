from typing import List

students = [
    {"name": "Alice", "scores": [80, 75, 90]},
    {"name": "Bob", "scores": [60, 65, 70]},
    {"name": "Charlie", "scores": [95, 90, 85]},
    {"name": "Daisy", "scores": [40, 50, 45]}
]

# TODO: Refactor this function to reduces complexity and improve readability.
# Refactor hints: reduces if else statements, default values
# API_URL: https://68458248fc51878754db82d7.mockapi.io/api/studentScores
def calculate_average_and_status(students: List[dict]) -> None:
    for student in students:
        total = 0
        count = 0
        for score in student["scores"]:
            total += score
            count += 1

        if count == 0:
            average = 0
        else:
            average = total / count

        student["average"] = average

        if average >= 70:
            student["is_passed"] = True
        else:
            student["is_passed"] = False


# TODO: Refactor this function to use list comprehension and improve readability.
# Refactor hints: use list comprehension to filter and map
# ex. [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# API_URL: https://68458248fc51878754db82d7.mockapi.io/api/squareIfEvenList
def square_if_even(numbers: List[int]) -> List[int]:
    squares_of_evens = []
    for num in numbers:
        if num % 2 == 0:
            squares_of_evens.append(num ** 2)
    return squares_of_evens
