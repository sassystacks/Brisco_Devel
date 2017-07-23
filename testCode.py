strng = 'test1'
dict_test_keys = [['test1','test2','test3','test4','test5'],[1,2,3,5,7],[4,34,6,4,3] ]
dict_test_values = ['1','2','3','4','5' ]
lst3 = [5,3,7,8,8]
lst4 = [23,53,234,123,123]

# list_turn_int = ['test1','test2','test5']
# dict_test = dict(zip(dict_test_keys,dict_test_values))

dict_test_keys.insert(0,lst3)
dict_test_keys.insert(2,lst4)

print(dict_test_keys)

print(dict_test_keys[0])
