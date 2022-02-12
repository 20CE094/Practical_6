#NAME: NEHAL PATEL
#ID: 20CE094
#Githun link: https://github.com/20CE094/Practical_6.git
#Repeated Words
N = int(input())
str_list = []
cnt_dict = {}

for i in range(N):
    s = input()
    str_list.append(s)

    if s in cnt_dict:
        cnt_dict[s] += 1
    else:
        cnt_dict[s] = 1
    
print(len(cnt_dict))
print(' '.join([str(cnt_dict[s]) for s in cnt_dict]))
