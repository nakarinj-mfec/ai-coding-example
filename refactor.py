from typing import List

# example 1
students = [
    {"name": "Alice", "scores": [80, 75, 90]},
    {"name": "Bob", "scores": [60, 65, 70]},
    {"name": "Charlie", "scores": [95, 90, 85]},
    {"name": "Daisy", "scores": [40, 50, 45]}
]

# หาค่าเฉลี่ย และตรวจสอบว่าเกิน 70 ไหม
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


def refactor_calculate_average_and_status(students: List[dict]) -> None:
    for student in students:
        scores = student["scores"]

        student["average"] = 0
        student["is_passed"] = False

        if not scores:
            continue
        
        average = sum(scores) / len(scores)
        student["average"] = average
        student["is_passed"] = average >= 70



# Example 2 list comprehension and seperate function

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def square_if_even(num: int) -> List[int]:
    squares_of_evens = []
    for num in numbers:
        if num % 2 == 0:
            squares_of_evens.append(num ** 2)
        

def refactor_square_if_even(numbers: List[int]) -> List[int]:
    return [num ** 2 for num in numbers if num % 2 == 0]