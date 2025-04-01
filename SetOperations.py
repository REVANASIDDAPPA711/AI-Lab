#Set Operations
set1={1,2,3,4,5}
set2={3,4,5,6,7}
union_set=set1.union(set2)
print(union_set,"Union Set")
Intersection_set=set1.intersection(set2)
print(Intersection_set,"Intersection set")
Difference_set1=set1.difference(set2)
print("Difference_set1",set1-set2)
symmetric_difference_set=set1.symmetric_difference(set2)
print(symmetric_difference_set,"Symmetric Difference Set")
have_common_elements=set1.isdisjoint(set2)
print("Do set1 and set2 have common elements",not have_common_elements)
set1.add(6)
print(set1)
set1.remove(3)
print(set1)
