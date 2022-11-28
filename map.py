#map 없이
a = [1.1, 2.2, 3.3]
for i in range(len(a)):
    a[i] = int(a[i])
print(a)

#map 사용
a = [1.1, 2.2, 3.3]
a = list(map(int, a))
print(a)

#아직 map함수에 대해서 완벽히 이해하진 못했다..