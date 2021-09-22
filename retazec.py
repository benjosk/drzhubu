# text = "lastovička"
# t1 = text[:2] + "STO" + text[5:]
# print(t1)

# for i in range(len(meno)):
#     print(meno, end=" ")
#
# for i in range(len(meno)):
#     print(meno)

# print("*" * (len(meno)+6))
# print(f"*  {meno}  *")
# print("*" * (len(meno)+6))

meno = input("meno:")
for i in range (len(meno)):
    print(meno[i] * (i+1))


