m_dict={}

size = int(input("\nEnter number of keys in the dictionary:"))

for i in range(size):
    print("Key-Value #{}".format(i+1))
    key=input("Enter name of key:")
    value = input("Enter key value:")
    m_dict[key] = value
    print()

print("\nOriginal dictionary is:", m_dict)

copy_dict={}
for key,value in m_dict.items():
    if value not in copy_dict.values():
        copy_dict[key] = value


print("\n New Dictionary :",copy_dict)
