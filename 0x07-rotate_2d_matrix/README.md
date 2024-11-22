Data Structures
This chapter describes some things you’ve learned about already in more detail, and adds some new things as well.

5.1. More on Lists
The list data type has some more methods. Here are all of the methods of list objects:

list.append(x)
Add an item to the end of the list. Similar to a[len(a):] = [x].

list.extend(iterable)
Extend the list by appending all the items from the iterable. Similar to a[len(a):] = iterable.

list.insert(i, x)
Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).

list.remove(x)
Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.
