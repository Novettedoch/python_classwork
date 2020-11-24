# import operator
# from functools import reduce

# number_list = {1, 2, 3, 4, 5, 6}

# operators = {
#   '+':operator.add,
#   '-':operator.sub,
#   '*':operator.mul,
#   '/':operator.truediv,
# }

# reduce = (number_list, '+')

# print(reduce)


# users = ['nova', 'wade', 'kayla']

# print(users)

# users.insert(3, 'jasper')

# print(users)

# users.append('star')

# print(users)

# print([users[4]])

# users.remove('kayla')

# print(users)

# popped_users = users.pop()
# print(popped_users)
# print(users)

# del users[0]

# print(users)

# users = ['things', 'and', 'stuff']

# ids = [0,1,2]

# mixed_list = [42, 10.4, 'what', users]

# print(mixed_list)

# user_list = mixed_list.pop()

# print(user_list)
# print(mixed_list)


# palindrome_maybe =('aibohphobia')

# def palindrome():
#   if palindrome_maybe == palindrome_maybe[::-1]:
#     return f'yes, {palindrome_maybe} is a palindrome'

#   else: 
#     return f'no, {palindrome_maybe} is a no,'


# print(palindrome())

# thing_list = {
#   'google': 20 * '$',
#   'twiter' : 5 * '$',
#   'facebook' : 10 * '$',
#   'ozmos' : 4 * '$'
# }
# print (thing_list.items())

# python loops

# names = 'Bottega University'

# string_length = 0
# for _ in names:
#   string_length += 1

# print(string_length)

# omi = [1, 4, 6]
# number_list = []

# for num in range(21):
#   if num in omit:
#     pass
#   else:
#     number_list.append(num)
# print(number_list)
# median of even list
# even_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# li = len(even_list)
# even_list.sort()

# if li % 2 == 0:
#     median1 = even_list[li//2]
#     median2 = even_list[li//2 - 1]
#     median = (median1 + median2) / 2
# else:
#     median = even_list[li//2]
# print("median is: " + str(median))

# def heading_generator(title, heading_type):
#   return f'<h{heading_type}>{title}</h{heading_type}>'

# print(heading_generator('hados', '1'))


# import random

# correct = random.randint(1, 11)

# guess = input("enter your guess: ")
# guess = int(guess)

# while guess != correct:
#     if guess > correct:
#         print("you've guessed too high, try guessing lower.")
    
#     else:
#         print("you've guessed too low, try guessing higher.")

# print("congrats, you got it.")

# class Invoice:

#   def __init__(self, client, total):
#     self.client = client
#     self.total = total
#   def formatter(self):
#     return f'{self.client} owes: ${self.total}'

# google = Invoice('google', 100)
# snapchat = Invoice('Snapchat', 200)
# print(google.formatter())
# print(snapchat.formatter())
