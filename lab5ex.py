import re
# #task1
# x=r'ab*'
# list=["a", "ab", "abb", "ac", "b"]
# for i in list:
#     if re.fullmatch(x, i):
#         print(i)
# #task2
# x=r'ab{2,3}'
# list=["abb", "abbb", "ab", "abbbb", "a", "agr"]
# for i in list:
#     if re.fullmatch(x, i):
#         print(i)
# #task3 
# x=r'[a-z]+_[a-z]+'
# list="ledi_gaga Jojo_pose school_13 amanbol_moldash messi_ronalDo"
# i=re.findall(x, list)
# print(i) 
# #task4
# x=r'[A-Z][a-z]+'
# list="Vsem privet, eto python Code"
# i=re.findall(x, list)
# print(i)
# #task5
# x=r'a.*b$'
# list=["a123b", "acb", "a-b", "ab", "abc"]
# for i in list:
#     if re.fullmatch(x, i):
#         print(i)   
# #task6
# list="Vsem privet, eto python Code."  
# x=re.sub(r"[ ,.]", ":", list)
# print(x) 
# #task7
# list="snake_case_peremennaya"
# x=re.split(r'_', list)
# camel_case=x[0] + ''.join(word.capitalize() for word in x[1:])
# print(camel_case)
# #task8
# list="SplitAtUpperCaseLettersExample"
# x=re.split(r'(?=[A-Z])', list)
# print(x)
#task9
text = "IphoneAndroidMacNvidiaIntel"
result = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
print(result)
#task10
def camel_to_snake(s):
    s = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', s)
    return s.lower()
print(camel_to_snake("CamelCaseExample"))
