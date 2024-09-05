sting = input("Введите строку: ").lower()

odd_chars = set()

for char in sting:
    if char in odd_chars:
        odd_chars.remove(char)

    else:
        odd_chars.add(char)

if len(odd_chars) <= 1:
    print("Строка является полиндромом")

else:
    print("Строка не является полиндромом")