# Aliasing
print('==========='+'Aliasing'+'===========')
l1 = [1,2,3,4,5]
print(type(l1)) # type of l1 is list

l2 = l1 # we are just creating duplicate reference variable (aliasing)
print(id(l1))
print(id(l2))

"""
The process of creating duplicate reference variable
problem with aliasing is , by using one reference if we are perform any change,
automatically those changes will be reflected for the remaining references also

"""

# Cloning
print('==========='+'Cloning'+'===========')

l1 = [1,2,3,4,5]
l2 = l1.copy() # we are creating duplicate list object --> cloning
print(id(l1))
print(id(l2))

# Deep cloning and shallow cloning
# ------------------------------------

# Example of shallow cloning
import copy

l1 = [1,2,[1,2,3],3,4,5]
# l2 = l1.copy() or copy.copy(l1) # both are same
l2 = l1.copy()

print('id of l1 ',id(l1))
print('id of l2 ',id(l2))
print('id of nested list l1[2]', id(l1[2]))
print('id of nested list l2[2]', id(l2[2]))

"""
Output: 

    id of l1  139718766539584
    id of l2  139718766950656
    id of nested list l1[2] 139718767425344
    id of nested list l2[2] 139718767425344
here copy() created new reference reriable fo the same object like here l1 and l2 are reference value of same object.
but internally nested list are point same


"""
# Example of deep cloning
l1 = [1,2,[1,2,3],3,4,5]
l2 = copy.deepcopy(l1)

print('id of l1 ',id(l1))
print('id of l2 ',id(l2))
print('id of nested list l1[2]', id(l1[2]))
print('id of nested list l2[2]', id(l2[2]))

"""
Output: 
=========
id of l1  140407566768448
id of l2  140407566677952
id of nested list l1[2] 140407566676736
id of nested list l2[2] 140407566769152

Here, completely different objects.

"""

"""

When we should go for shallow cloning and deep cloning
==========================================================

If original object does not contain any nested objects then it is highly recommended to go for  ==> shallow cloning

if origin object contains any nested object then we should go for deep cloning 
"""

