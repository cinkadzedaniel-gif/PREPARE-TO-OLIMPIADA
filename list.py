numbers = []

numbers.append(10)
numbers.append(20)

another_number = [
    "30", "40", "50"
]

numbers.extend(another_number)

print("Довжина:", len(numbers))
print("Список:", *numbers)

