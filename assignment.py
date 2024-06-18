my_dict = {'jenish':'7304795581','robin':'7304795582','venus':'7304795583',
           'adhithya':'7304795584'}
print(sorted(my_dict.items()))
name = input('enter name : ')
no = int(input('enter no. : '))
if name in my_dict:
    print('Name is already present in my dict')
else:
    my_dict[name] = no

print(my_dict)
