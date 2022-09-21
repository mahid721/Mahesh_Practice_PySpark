
#  -------------------------------------------- add() -----------------------------------------



"""
add() :
		Syntax -- set.add(elmnt)
		functionality --  Adds an element to the set and If the element already exists, the add() method does not add the element.
		args -- one mandatory argument -- add() takes single parameter(elem) which needs to  be added in the set.
		returns -- The add() method doesn't return any value. --  None type

"""

set_1 = {1, 'dileep', 'dasari', 2, 5, 'mahesh', 4, 5, 6, 7}

print(set_1)

x = set_1.add(1000)

print(set_1)

print(x)

#  -------------------------------------------- copy() -----------------------------------------

"""
 copy()	 :	
        syntax -- new_set = old_set.copy()
		functionality --  Returns a copy of the set
                The copy() method returns a shallow copy of the set in python. If we use “=” to copy a set to another set, 
                when we modify in the copied set, the changes are also reflected in the original set. 
                So we have to create a shallow copy of the set such that when we modify something in the copied set, 
                changes are not reflected back in the original set.
		args -- The copy() method for sets doesn’t take any parameters.
		returns -- The function returns a shallow copy of the original set

"""

s2 = {1, 2, 3, 4, 5, 6, 7}
s3 = s2.copy()
print(s3)

s3.add(122)
print(s3)


#  -------------------------------------------- clear() -----------------------------------------
""""
 clear()	 :	
        syntax -- set.clear()
		functionality --  Python Set clear() method removes all elements from the set.
		args -- The clear() method for sets doesn’t take any parameters.
		returns -- The clear() method doesn't return any value. --  None type

"""

s4 = {1, 2, 3, 4, 5, 6, 7}
x = s4.clear()
print(x)



#  -------------------------------------------- update() -----------------------------------------
""""
 update()	 :	
        syntax -- set1.update(set2) 
		functionality --  set adds elements from a set (passed as an argument) to the set.
		args -- Update() method takes only a single argument. The single argument can be a set, list, tuples or a dictionary. It automatically converts into a set and adds to the set. 
		returns -- The clear() method doesn't return any value. --  None type

"""

s5 = {1, 2, 3, 4, 5, 6, 7}
s6 = {10, 20, 30, 40, 50}
s5.update(s6)
print(s5)

#  -------------------------------------------- union() -----------------------------------------
""""
 union()	 :	
        syntax -- set1.union(one/more sets) 
		functionality --  it merge to sets or 
		args -- zero or more sets 
		returns -- Returns a set, which has the union of all sets(set1, set2, set3…) with set1. It returns a copy of set1 only if no parameter is passed.

"""

s7 = {1, 2, 3, 4, 5, 6, 7}
s8 = {10, 20, 30}
s9 = {50, 60, 70}

s10 = s7.union(s8, s9)
print(s10)

#  -------------------------------------------- pop() -----------------------------------------
""""
 pop()	 :	
        syntax -- set.pop()
		functionality --  Method removes any a random element from the set and returns the removed element.
		args -- doesn’t take any parameter.
		returns -- Returns the popped/removed element from the set

"""

s11 = {1, 2, 3, 4, 5, 6, 7}
x = s7.pop()
print(s7)
print(x)


#  -------------------------------------------- remove() -----------------------------------------
""""
 remove()	 :	
        syntax -- set.remove(ele)
		functionality --  method removes the specified element from the set. 
		                This method is different from the discard() method, 
		                because the remove() method will raise an error if the specified item does not exist, and the discard() method will not.
		args -- one mandatory argument -- remove() takes single parameter(elem) which needs to  be removed in the set.
		returns -- The remove() method doesn't return any value. --  None type

"""

s12 = {1, 2, 3, 4, 5, 6, 7, 'mahesh'}
x = s12.remove('mahesh')
s12.remove('100')
print(x)
print(s12)

#  -------------------------------------------- discard() -----------------------------------------
""""
 discard()	 :	
        syntax -- set.discard(ele)
		functionality --  method removes the specified element from the set. 
		                This method is different from the discard() method, 
		                because the remove() method will raise an error if the specified item does not exist, and the discard() method will not.
		args -- one mandatory argument -- discard() takes single parameter(elem) which needs to  be removed in the set.
		returns -- The discard() method doesn't return any value. --  None type

"""

s12 = {1, 2, 3, 4, 5, 6, 7, 'mahesh'}
x = s12.discard('mahesh')
s12.discard('100')
print(x)
print(s12)







