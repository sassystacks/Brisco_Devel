strng = 'test1'
dict_test_keys = ['test1','test2','test3','test4','test5' ]
dict_test_values = ['1','2','3','4','5' ]

list_turn_int = ['test1','test2','test5']
dict_test = dict(zip(dict_test_keys,dict_test_values))

print dict_test
a = dict_test[strng]
print(a)
print(type(a))
b = [int(x) for x in dict_test_values if a in x]
print(b[0])
print(type(b[0]))
