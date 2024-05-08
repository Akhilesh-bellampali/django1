L=eval(input('Enter list of integer:'))
print('List is',L)
print('Total number of items in the list is',len(L))
L.reverse()
print('List in reverse order',L)
del L[0]
del L[-1]
print('List after removing first and last element',L)
L.sort()
print('List after sorting',L)
