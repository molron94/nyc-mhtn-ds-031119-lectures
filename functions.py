# Make a function to determine if a number is odd or even

def odd_even(number):
    if number %1 !=0: 
        return "not integer"
    elif number %2 ==0: 
        return "even"
    else: 
        return "odd"

# Make a function that takes in a list of numbers and returns the numbers that are even

def even_list(numbers):
    return list(filter(lambda number:number%2==0, numbers))

# Given a list return the unique names in the list

def unique_names(list_of_names):
    unique_list=[]
    for name in list_of_names:
        if name not in unique_list:
            unique_list.append(name)

    return unique_list

# Make a function that determines if a word is a palindrome

def palindrome_detector(string):
    backward=''
    for i in range(1,1+len(string)):
        backward=backward+string[-i]
    return backward==string

print(odd_even(4))
print(odd_even(139))
print(even_list([1,3,4,6,7]))
print(unique_names(['john', 'john', 'john']))
print(palindrome_detector('racecar'))
print(palindrome_detector('not'))