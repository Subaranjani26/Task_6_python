#Question:1
#Creating two lists, one list having even numbers and other having odd numbers:

list = [10, 501, 22, 37, 100, 999, 87, 351]

evens = [num for num in list if num % 2 == 0]
print(evens)

odds = [num for num in list if num % 2 != 0]
print(odds)

#Question:2
#Count all the Prime numbers and create a python list contains all the prime numbers:

def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

list = [10, 501, 22, 37, 100, 999, 87, 351]
prime_number=[]
count = 0
for num in list:
    if prime(num):
        prime_number.append(num)
        count += 1
print("Count of all prime numbers:", count)
print("New Python list contains all the Prime numbers:", prime_number)

#Question:3
#Creating a python list having Happy Numbers in it:

def happy_number(n):
    base = set()
    while n != 1 and n not in base:
        base.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1

list = [10, 501, 22, 37, 100, 999, 87, 351]
happy_numbers = 0
for number in list:
    if happy_number(number):
        happy_numbers += 1
print("Original list:",list)
print("Total Number of Happy Numbers in the given original list:", happy_numbers)

#Question:4
#Sun of the first and last digit of an integer:

num = int(input("Enter the number:"))
last_digit = num % 10
while num != 0:
    first_digit = num % 10
    num = num // 10
sum = first_digit + last_digit

print(f"Sum of first and last digit is: ",sum)

#Question:5

mangoes = [2,4,6,8,10]
students = 4

mangoes.sort()
print(mangoes)
mininum_diff = float('inf')

for i in range(len(mangoes) - students + 1):
    diff = mangoes[i + students - 1] - mangoes[i]
    if diff < mininum_diff:
        mininum_diff = diff

print(f"The Minimum Difference:" , mininum_diff)

#Question:6

list1 = [2,4,6,8,10]
list2 = [5,10,15,20,25]
list3 = [10,20,30,0]

set1 = set(list1)
set2 = set(list2)
set3 = set(list3)

print(set1)
print(set2)
print(set3)

duplicates_list1 = set1.intersection(set2, set3)
final_list1 = duplicates_list1
print("Duplicates in the three lists:",final_list1)

#Question:7

def non_repeating_element(non_repeating_list):
    count = {}
    for number in non_repeating_list:
        if number in count:
            count[number] += 1
        else:
            count[number] = 1
    for number in non_repeating_list:
        if count[number] == 1:
            return number
    return None


non_repeating_list = [23, 5, 67, 89, 23, 60, 103, 5]

result = non_repeating_element(non_repeating_list)
if result is not None:
    print("Non-repeating element is:", result)
else:
    print("No non-repeating element")

#Question-8

numbers =[1,2,3,4,5,6,7,8,9]

print(numbers)

numbers.sort()

print(numbers)

print(f"The Minimum Number:",numbers[0])

#Question-9

def triplet(list, target):
    n = len(list)
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if list[i] + list[j] + list[k] == target:
                    return [list[i], list[j], list[k]]
    return


list = [10, 20, 30, 9]
target = 59
triplet = triplet(list, target)

if triplet:
    print(f"The Original value",triplet)
else:
    print("Not an Original value")

#Question:10

def has_zero_sum_sublist(lst):
    seen_sums=set()
    current_sum=0

    for num in lst:
        current_sum += num

        if current_sum == 0 or current_sum in seen_sums:
            return True
        seen_sums.add(current_sum)
        return False

my_list = [4,2,-3,1,6]
result=has_zero_sum_sublist(my_list)
print(result)




