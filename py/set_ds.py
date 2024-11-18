"""
What is set?

it is a python class, as we know in python everything are an object.
it is one of the most popular data type in python.
It contains only unique values,and there order is not preserved (un ordered).
it is a mutable that means we can modify the objects.

NB : set object has not indexing and slicing because order are not preserved

how to create set object?

way - 1:

s1 = s1 = {10,20,30,40,50}

way - 2:
s1 = set()

# list of sets function
1. add(value)
    this is a method of set object and
    it will take argument as value that will add into the set that object and there are no gurantee of index

2. remove(value)
    this is method of set object and it will take argument as value,
    remove method is use to remove the value from set and it will not return anything if exists and its raised ValueError if not exists then

3. discard(value)
     this is same as remove(value) method , but it will not raise any error even though value is not exists if value is exists then i will discard/remove from the set.

4. pop()
    pop will remove any one item from set object, and it will not return anything.
    It will raise KeyError if set object is empty then.

5. clear()
    clear will return the all the item from set

6. s1.union(s2)
    it will return all the value from both set1 and set 2
7. s1.intersection(s2)
    It will return only common value from given both sets

8. s1.difference(s2)
    It will return new set of difference value from both set1 and set 2

9. s1.issubset(s2)
    It will return True is s1 is subset of s2 else False
10. s1.issuperset(s2)
    It will return True is s1 is super subset of s2 else False

11. s1.isdisjoint(s2)
    It will return True if both sets are items are not same, if any of items are  matched from any of set then it will return False.
    so by using is_disjoint() method we can check any of items are same or not
12. s1.intersection_update(s2)
    It will update the common value into the s1 without creating new object,

    s1.intersection_update and s1 = s1.intersection_update(s2) both are same?

    Answer: both are doing same thing but internally both are not same
    :exception
    here, s1.intersection_update(s2) not creating new object, updating intersection value into s1.

    and s1 = s1.intersection(s2) creating new object with s1 existing value along with intersection value.


13. s1.difference_update(s2)
    It is same the difference() method but it will just perform the modification in s1 object itself, that means it will update he differece into s1

14. s1.update(s2)
    It is same as union() method but it will just perform modification of s1 object


15. s1.symmetric_difference(s2)
16. s1.symmetric_difference_update(s2)
"""
def set_add(s1, value):
    s1.add(value)
    return s1

def set_remove(s1, value):
    s1.remove(value)
    return s1

def set_discard(s1, value):
    s1.discard(value)
    return s1

def set_pop(s1):
    s1.pop()
    return s1

def set_clear(s1):
    s1.clear()
    return s1

def set_union(s1,s2):
    return s1.union(s2)

def set_intersection(s1,s2):
    return s1.intersection(s2)

def set_difference(s1,s2):
    return s2.difference(s1)
def set_issubset(s1,s2):
    return s1.issubset(s2)

def set_issuperset(s1,s2):
    return s2.issuperset(s1)

def set_isdisjoint(s1,s2):
    return s1.isdisjoint(s2)

def set_intersection_update(s1,s2):
    s1.intersection_update(s2)
    print('"intersection_update : "Id of s1 ', id(s1))
    return s1

def set_intersection_update_without(s1,s2):
    # without using intersection_update() method
    s1 = s1.intersection(s2)
    print('"intersection_update : "Id of s1 ', id(s1))
    return s1

def set_difference_update(s1,s2):
    s1.difference_update(s2)
    return s1

def set_update(s1,s2):
    s1.update(s2)
    return s1

def set_symmetric_difference(s1, s2):
    return s1.symmetric_difference(s2)

s1 = {'binary', 'bridge', 'tech', 'best', 'learning', 'portal'}
s2 = {'Across', 'World',}
print('Existing Set1: ', s1)
print('Existing Set2: ', s2)

print('Answer : ', set_symmetric_difference(s1,s2))



