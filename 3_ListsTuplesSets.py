# List : List is just like array which is used to store a collection of data. Items in a list do not need to be of the same type.
courses = ['History', 'Math', 'Physics', 'Chemistry']
# print(courses)

# Access specific element in list
# print(courses[0])
# print(courses[1])



# Access last element
# print(courses[len(courses)-1])
# OR
# print(courses[-1])


# print(courses[1:3]) # From range 1 to 2 (Not 3 because second index is exclusive)


# Append Element
# courses.append("ComputerScience")
# print(courses)

# Remove Element
# courses.remove("ComputerScience")
# print(courses)


# Insert Element at specific position
# courses.insert(1, "English")
# print(courses)


# Insert Elements from another list
courses_2 = ['Art', "Education"]
# courses.extend(courses_2)
# print(courses)



# Pop Element from the end
# courses.pop()
# print(courses)


# Reverse 
# courses.reverse()
# print(courses)


# Sort
# Ascending Order
nums = [5,1,8,3,9,4,6,2,7]
# nums.sort()
# print(nums)

# Descending Order
# nums.sort(reverse=True)
# print(nums)