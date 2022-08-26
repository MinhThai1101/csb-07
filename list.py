#scores = [5, 6, 6.5, 10]
#print(scores[2])

#import math
#print(math.sqrt(9))
#add string
#print(len(scores))
#scores.append("abc")
#print(scores)
#de ten bien
#cach 1
#for i in range(len(scores)): # 0 1 2 3
#    print(f'item:{scores[i]}') 
#cach 2
#for item in scores:
 #   print(f'item:{item}')

str = input("nhap 1 so bat ki:")
listChuSo = ['0','1','2','3','4','5','6','7','8','9']
a = 0
for item in str:
    if item not in listChuSo:
        a+=4
if a == 0:
    print('no la so')
else:
    print('no khong la so')