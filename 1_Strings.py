message = 'HelloWorld'
# message1 = 'XYZ\'s House'

# Print Message
# print(message)



# Print the length
# print(len(message))



# Print First Character
# print(message[0])



# Print Specific Substring between a range
# Starting index is inclusive but ending is exclusive
# print(message[:6]) 
# or 
# print(message[0:6])



# Print all character in lowercase
# print(message.lower())



# Print all character in uppercase
# print(message.upper())



# Count the appearance of string or character
# print(message.count("Hello"))
# print(message.count('o'))




# Find the string
# print(message.find("World")) ## Return 5 because 'World' starts from index 5




# Replace character or substring
# new_msg = message.replace('o', 'X')
# print(new_msg)



# 1. Concatenate Strings
# firstName = "Rwitesh"
# lastName = "Bera"
# Name = firstName + " " + lastName + ' Welcome!'
# print(Name)



# 2. Concatenate Strings
firstName = "Rwitesh"
lastName = "Bera"
Name = '{} {}, Welcome!'.format(firstName, lastName)
print(Name)



# You can use 'f-string' mechanism to concatenate multiple strings
# greeting = "Hello"
# name = "Rwitesh"
# displayGreet = f'{greeting}, {name}. Welcome!'
# print(displayGreet)



# More Methods
a = "kolkata"
print(a.capitalize())


