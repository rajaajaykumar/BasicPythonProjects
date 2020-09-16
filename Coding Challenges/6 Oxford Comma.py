# Oxford Comma

def commafy(list):
    list[-1] = "and " + list[-1]
    return ", ".join(list)
    #or
    #return list[0] + ", " + list[1] + ", and " + list[2]

list1 = ["Lions", "Tigers", "Bears"]
list2 = ["Apple", "Banana", "Mango"]

print(commafy(list1))
print(commafy(list2))
