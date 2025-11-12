my_dict={'apple':4,'banana':2,'cherry':1,'mango':3}
asc_dict=dict(sorted(my_dict.items()))
desc_dict=dict(sorted(my_dict.items(),reverse=True))
print("original dictionary:",my_dict)
print("ascending order:",asc_dict)
print("Descending order:",desc_dict)
