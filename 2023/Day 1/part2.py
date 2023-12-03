with open('input.txt') as file:
    input_data = file.read().split()

total_sum = 0

num2words = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

key_size = len(max(num2words, key=len))


def get_digits(data):
    digits = []
    for position, character in enumerate(data):
        if character.isdigit():
            digits.append(character)
        for number in num2words:
            if data[position:position + key_size].startswith(number):
                digits.append(num2words[number])
    return digits


for case in input_data:
    digits = get_digits(case)
    total_sum += int(digits[0] + digits[-1])

print(total_sum)
