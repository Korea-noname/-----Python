python = "Python is Amazing"
print(python.lower()) # 모두 소문자로 출력
print(python.upper()) # 모두 대문자로 출력
print(python[0].isupper()) # 0번째 자리가 대문자가 맞는지 확인, 맞다면 True, 다르면 False
print(python[0].islower())
print(len(python)) # python변수의 전체 길이를 반환
print(python.replace("Python", "C")) # Python이라는 문자를 찾아서 C로 변환

index = python.index("n") # python 변수에서 n이라는 문자가 몇 번째에 위치했는지 출력
print(index)
index = python.index("n", index + 1) # 위의 위치에서 + 1 자리 이후부터 다시 n을 찾아서 출력
print(index)

print(python.find("n")) # index와 동일하게 n을 찾아서 출력

# ↓ find와 index의 차이
print(python.find("Java")) # python 변수안에 해당 문자가 없다면 -1을 출력하며 그대로 실행
# print(python.index("Java")) python 변수안에 Java가 없다면 에러를 내버림

print(python.count("n")) # python 변수안에서 n이 총 몇 개 있는지 출력
