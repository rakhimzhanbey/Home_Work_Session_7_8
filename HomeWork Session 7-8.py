w = "azcbobobegghakl"
long = ""
temp = ""

for i in w:
    if len(temp) == 0:
        temp += i
        continue
    if i >= temp[-1]:
        temp += i
    else:
        long = temp
        temp = i

print(long)