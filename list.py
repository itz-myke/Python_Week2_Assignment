my_list = []

#append my list
my_list.append("10")
my_list.append("20")
my_list.append("30")
my_list.append("40")

#inserting a value 
my_list.insert(1, "15")

#extending the list with another list
my_list.extend(["50", "60", "70"])

#removing the last element from the list
my_list.pop()

#sorting the list
my_list.sort()

#finding the index of an element
indexof30 = my_list.index("30")

print("index of 30 is:", indexof30)
