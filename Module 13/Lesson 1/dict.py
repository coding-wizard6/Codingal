def test(lst):
    result={}
    for item in lst:
        result[item[0]] = item[1:]
    return result

students=[[1,'abc','V'],[2,'zxy','VI'],[3,'asd','VII']]

print("Original list:",students)
print("\n\n\n COnverted list to dictionary:",test(students))