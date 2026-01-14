def digitsSum(inputInt: int) -> int:
    suma = 0
    for num in str(abs(inputInt)):
        suma += int(num)
    return suma

print(digitsSum(12345))
print(digitsSum(999))
print(digitsSum(9184501))
