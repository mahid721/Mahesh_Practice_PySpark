#  -------------------------------------------- difference() -----------------------------------------
""""
 difference()	 :
        syntax -- set_obj.difference(set)
		functionality --  The difference between the two sets in Python is equal to the difference between the number of elements in two sets
		args -- one mandatory argument -- difference() takes single parameter(set) which needs to  be find difference in the set.
		returns -- The function difference() returns a set that is the difference between two sets.

"""

s12 = {1, 2, 3, 4, 5, 6, 7, 'mahesh'}
s13 = {1, 2, 3, 4, 5, 100, 200, 300, 400}

diff_set = s12.difference(s13)
print(diff_set)


#  -------------------------------------------- difference_update() -----------------------------------------
""""
 difference_update()	 :
        syntax -- set_obj.difference_update(set)
		functionality --  The difference_update find difference between the two sets in Python is equal to the difference between the number of elements in two sets 
		                    and it will update the set with unmatched elements
		args -- one mandatory argument -- difference_update() takes single parameter(set) which needs to  be find difference in the set.
		returns -- The function returns None and changes the value of the existing set.

"""
s14 = {1, 2, 3, 4, 5, 6, 7, 'mahesh'}
s15 = {1, 2, 3, 4, 5, 100, 200, 300, 400}

x = s14.difference_update(s15)
print(s14)


#  -------------------------------------------- intersection() -----------------------------------------
""""
 intersection()	 :
        syntax -- set_obj.intersection(one/more sets)
		functionality --  The intersection of two given sets is the largest set, which contains all the elements that are common to both sets.
		args -- one mandatory argument -- intersection() takes single parameter(set) which needs to  be find matched eles in the set.
		        we can give no of optional sets
		returns -- returns a new set with an element that is common to all set 

"""

s16 = {1, 2, 3, 4, 5, 6, 7, 'mahesh'}
s17 = {1, 2, 3, 4, 5, 100, 200, 300, 400}

match_set = s16.intersection(s17)
print(match_set)




#  -------------------------------------------- intersection_update() -----------------------------------------
""""
 intersection_update()	 :
        syntax -- set_obj.intersection_update(one/more sets)
		functionality --  The intersection of two given sets is the largest set, which contains all the elements that are common to both sets.
		                    and update set with removing all unmatched records with compared sets
		args -- one mandatory argument -- intersection() takes single parameter(set) which needs to  be find matched eles in the set.
		        we can give no of optional sets
		returns -- The function returns None and changes the value of the existing set.

"""

s18 = {1, 2, 3, 4, 5, 6, 7, 'mahesh'}
s19 = {1, 2, 3, 4, 5, 100, 200, 300, 400}
s20 = {1, 2, 3, 4,'mahesh', 11, 22, 33, 44}

s18.intersection_update(s19, s20)
print(s18)



#  -------------------------------------------- isdisjoint() -----------------------------------------
""""
 isdisjoint()	 :
        syntax -- set_obj.isdisjoint(set)
		functionality --  check whether the two sets are disjoint or not, if it is disjoint then it returns True otherwise it will return False. 
		                    Two sets are said to be disjoint when their intersection is null.
		args -- one mandatory argument -- isdisjoint() takes single parameter(set) which needs to  be find matched eles in the set.
		returns -- The function returns Boolean value(True/False) 

"""

s20 = {1, 2, 3, 4, 5, 6, 7, 'mahesh'}
s21 = {1, 2, 3, 4, 5, 100, 200, 300, 400}

x = s20.isdisjoint(s21)
print(x)


#  -------------------------------------------- issubset() -----------------------------------------
""""
 issubset()	 :
        syntax -- set_obj.issubset(set)
		functionality --  returns True if all items in the set exists in the specified set, otherwise it retuns False.
		args -- one mandatory argument -- issubset() takes single parameter(set) 
		returns -- The function returns Boolean value(True/False) --  returns True if all items in the set exists in the specified set, otherwise it retuns False.

"""
s22 = {1, 2, 3, 4, 5, 6, 7, 'mahesh'}
s23 = {1, 2, 3, 4, 5, 100, 200, 300, 400, 7, 'mahesh'}

x = s22.issubset(s23)
print(x)






#  -------------------------------------------- issuperset() -----------------------------------------
""""
 issuperset()	 :
        syntax -- set_obj.issuperset(set)
		functionality --  The issuperset() method returns True if all items in the specified set exists in the original set, otherwise it retuns False.
		args -- one mandatory argument -- issuperset() takes single parameter(set) 
		returns -- The function returns Boolean value(True/False) --  returns True if all items in the specified set exists in the original set, otherwise it retuns False.

"""
s23 = {1, 2, 3, 4, 5, 6, 7, 'mahesh'}
s24 = {1, 2, 3, 4, 5,}

x = s23.issuperset(s24)
print(x)





#  -------------------------------------------- symmetric_difference() -----------------------------------------
""""
 symmetric_difference()	 :
        syntax -- set_obj.symmetric_difference(set)
		functionality --  The symmetric difference of two sets set1 and set2 is the set of elements which are in either of the sets set1 or set2 but not in both
		args -- one mandatory argument -- symmetric_difference() takes single parameter(set) 
		returns -- Returns a set which is the symmetric difference (unmatched eles from both sets) between the two sets. 
"""
s25 = {1, 2, 3, 4, 5, 6, 7, 'mahesh'}
s26 = {1, 2, 3, 4, 5,100, 200, 400}

diff_set = s25.symmetric_difference(s26)
print(diff_set)

#  -------------------------------------------- symmetric_difference_update() -----------------------------------------
""""
 symmetric_difference_update()	 :
        syntax -- set_obj.symmetric_difference_update(set)
		functionality --  symmetric_difference() method returns a new set which contains symmetric difference of two sets. 
		                    The symmetric_difference_update() method updates the set calling symmetric_difference_update() with the symmetric difference of sets.
		args -- one mandatory argument -- symmetric_difference_update() takes single parameter(set) 
		returns -- returns None -- update the first set with symmetric differnce. 
"""
s27 = {1, 2, 3, 4, 5, 6, 7, 'mahesh'}
s28 = {1, 2, 3, 4, 5,100, 200, 400}

s25.symmetric_difference_update(s26)
print(s25)


