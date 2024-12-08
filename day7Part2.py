with open("inputs\inputDay7.txt") as file:
    data = file.read().splitlines()
res =0
operators = []

def operationer(numbers, target):
    if len(numbers)<2:
        return numbers[0] == target
    valid = False
    numbersAdded = [numbers[0]+numbers[1]] + numbers[2:]
    valid = operationer(numbersAdded, target)
    numbersMul = [numbers[0]*numbers[1]] + numbers[2:]
    valid = valid or operationer(numbersMul, target)
    concat = str(numbers[0])+str(numbers[1])
    numbersConc = [int(concat)] + numbers[2:]
    valid = valid or operationer(numbersConc, target)
    return valid


for line in data :
    number, operator =line.split(': ')
    operators = list(map(int, operator.split(' ')))
    if operationer(operators, int(number)):
        res += int(number)

print(res)