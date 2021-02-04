# Question2
# Q2.Write a function in python in python, which will return maximum ?
# Ans:
a={1: 'name1',2 :'name2',3 : 'name3'}            
b={'1':90,'2':60,'3':70}
def dic (b):
    a= max(b.values())

    for dict_key, dict_value in b.items():
        if a == dict_value:
            return (dict_key,dict_value)
print(dic(b))