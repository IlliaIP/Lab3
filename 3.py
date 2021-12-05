def Borda(mat, cand):
    Sum = 0
    for i in range(0, len(mat)):    
        for j in range(0, len(mat[0])):
            if mat[i][j] == cand:
                if mat[i].index(cand) == 1:
                    Sum += mat[i][0] * 2
                elif mat[i].index(cand) == 2:
                    Sum += mat[i][0] * 1
                elif mat[i].index(cand) == 3:
                    Sum += mat[i][0] * 0
    return Sum

def method_Condorce(mat, comp):
    res = list()
    for i in range(len(comp)):
        left = comp[i][0]
        right = comp[i][len(comp[i])-1]
        s = 0
        for i in range(0, len(mat)):
            if mat[i].index(left) < mat[i].index(right):
                s += mat[i][0]
        res.append(s)
    return res

data = open("3.txt", "r")
values = []
for aline in data:
    values.append(aline.split())
data.close()

print("Матриця виборців та їх переваг:")
for el in values:
    print(*el, sep='\t')
print()

for i in range(0, len(values)):    
    if values[i][0].isdigit() == True:
        values[i][0] = int(values[i][0])

A = Borda(values, 'A')
B = Borda(values, 'B')
C = Borda(values, 'C')
print("Метод Борда:")
print("Cума для кандидата А: ", A)
print("Cума для кандидата B: ", B)
print("Cума для кандидата C: ", C)
best_Borda = max([A, B, C])
if best_Borda == A:
    print('Переможцем за методом Борда є кандидат А з рахунком ', best_Borda)
elif best_Borda == B:
    print('Переможцем за методом Борда є кандидат B з рахунком ', best_Borda)
elif best_Borda == C:
    print('Переможцем за методом Борда є кандидат C з рахунком ', best_Borda)    
print()

compare = ["A > B", "B > A", "B > C", "C > B", "A > C", "C > A"]
res_Condorce = method_Condorce(values, compare)
print("Метод Кондорсе:")
for i in range(len(compare)):
    print(compare[i] + ": " + str(res_Condorce[i]))
print()    

best_compare = []
for i in range(0, len(compare), 2):
    if res_Condorce[i] > res_Condorce[i+1]:
        best_compare.append([compare[i], res_Condorce[i]])
    else:
        best_compare.append([compare[i+1], res_Condorce[i+1]])
for el in best_compare:
    print(*el, sep=': ')
print()

for i in range(0, len(best_compare)):
    str1 = best_compare[i][0]
    for j in range(0, len(best_compare)):
        str2 = best_compare[j][0]
        for k in range(0, len(best_compare)):
            str3 = best_compare[k][0]
            if best_compare[i][0] != best_compare[j][0] and best_compare[i][0] != best_compare[k][0] and best_compare[j][0] != best_compare[k][0]:
                if str1[len(str1) - 1] == str2[0]:
                    str1_str2 = str1 + ' > ' + str2[len(str2) - 1]
                    if str1_str2[0] == str3[0] and str1_str2[len(str1_str2) - 1] == str3[len(str3) - 1]:
                        print(str1_str2)
                        print('Переможець за методом Кондорсе: %s' %str1_str2[0])
                    else:
                        print('Неможливо визначити переможця!') 
                