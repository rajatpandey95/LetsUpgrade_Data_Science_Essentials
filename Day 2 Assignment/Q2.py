'''
 List comprehensions are used for creating new lists from other iterables.
 As list comprehensions return lists, they consist of brackets containing the expression,
 which is executed for each element along with the for loop to iterate over each element

 Syntax:
 variable=[expression  for-loop  condition]
 '''


h_letters = [ letter for letter in 'human' ]
print( h_letters)


even_list = [y for y in range(20) if y % 2 == 0 ]
print(even_list)
