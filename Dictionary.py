#Dictionary Operatioons
sample_dict={'a':1,'b':2,'c':3,'d':4}
key_to_check='b'
if key_to_check in sample_dict:
    print(f'The key{key_to_check} exists in the dictionary')
print("Traversing the dictionary")
for key,value in sample_dict.items():
    print(f'Keys:{key},Values:{value}')
keys_list=list(sample_dict.keys())
values_list=list(sample_dict.values())
items_list=list(sample_dict.items())
print("using the dictionary methods")
print(f'Keys:{keys_list}')
print(f'Values:{values_list}')
print(f'items:{items_list}')
