''' 1)
Write a Python program to filter a list of integers using Lambda. Go to the editor
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]
'''

int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_even = list(filter(lambda num: (num % 2 == 0), int_list))
filtered_odd = list(filter(lambda num: (num % 2 == 1), int_list))

print("Original list of integers:")
print(int_list)

print("Even numbers from the said list:")
print(filtered_even)

print("Odd numbers from the said list:")
print(filtered_odd)


''' 2)
find which days of the week have exactly 6 characters.
'''

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

result = list(filter(lambda day: (len(day) == 6), weekdays))

print(result)




''' 3)
remove specific words from a given list 
Original list:
['orange', 'red', 'green', 'blue', 'white', 'black']

Remove words:
['orange', 'black']

After removing the specified words from the said list:
['red', 'green', 'blue', 'white']

'''

original_list = ['orange', 'red', 'green', 'blue', 'white', 'black']

remove_words = list(filter(lambda color: (color == 'orange' or color == 'black'), original_list))
new_list =  list(filter(lambda color: (color != 'orange' and color != 'black'), original_list))

print("Original list:")
print(original_list)

print("Remove words:")
print(remove_words)

print("After removing the specified words from the said list:")
print(new_list)



''' 4)
 remove all elements from a given list present in another list
Original lists:
list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2: [2, 4, 6, 8]

Remove all elements from 'list1' present in 'list2:
[1, 3, 5, 7, 9, 10]
 '''

og_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
og_list2 = [2, 4, 6, 8]

remove_list = [1, 3, 5, 7, 9, 10]

result = list(filter(lambda elem: elem not in og_list2, og_list1))

print(result)



''' 5)
find the elements of a given list of strings that contain specific substring using lambda
Original list:
['red', 'black', 'white', 'green', 'orange']
Substring to search:
ack
Elements of the said list that contain specific substring:
['black']
Substring to search:
abc
Elements of the said list that contain specific substring:
[]

'''
og_list = ['red', 'black', 'white', 'green', 'orange']
search = list(filter(lambda sub: 'ack' in sub, og_list))
print(search)

search2 = list(filter(lambda sub: 'abc' in sub, og_list))
print(search2)


''' 6)
check whether a given string contains a capital letter, a lower case letter, a number and a minimum length of 8 characters.
(This is like a password verification function, HINT: Python function 'any' may be useful)
'''




''' 7)
Write a Python program to sort a list of tuples using Lambda.

# Original list of tuples:
original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Expected Result:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
'''

original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

print(original_scores)
original_scores.sort(key = lambda score: score[1])
print(original_scores)