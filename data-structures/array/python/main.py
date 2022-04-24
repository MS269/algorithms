array1 = []  # 빈 리스트 선언
array2 = [1, 2, 3, 4, 5]  # 리스트 초기화

# 맨 뒤에 원소를 삽입하는 데에 드는 시간 복잡도는 O(n)이다.
for i in range(5):
    array1.append(i + 1)
# array1 = [1, 2, 3, 4, 5]

# 원소에 접근하는 데에 드는 시간 복잡도는 O(1)이다.
print(array1[4])
# 5

# 원소를 삽입하는 데에 드는 시간 복잡도는 O(n)이다.
array1.insert(0, 10)
# array1 = [10, 1, 2, 3, 4 , 5]

# 원소를 삭제하는 데에 드는 시간 복잡도는 O(n)이다.
del array1[0]
# array1 = [1, 2, 3, 4, 5]
