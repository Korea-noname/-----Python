# 방법 1
print("나는 %d살입니다" % 27) # 숫자
print("나는 %s을 좋아해요" % "Python") # 문자열
print("Apple은 %c로 시작해요" % "A") # 문자

# %s
print("나는 %s살입니다" % 27) # %s는 숫자도 가능

print("나는 %s색과 %s색을 좋아해요" % ("검정", "하양")) # 괄호안의 순서대로 적용

# 방법 2
print("나는 {}살입니다".format(27))
print("나는 {}색과 {}색을 좋아해요".format("검정","하양"))
print("나는 {1}색과 {0}색을 좋아해요".format("검정","하양")) # 괄호안의 인덱스 번호기준, 숫자대로 위치를 변경가능

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요".format(age = 27, color = "검정"))
print("나는 {age}살이며, {color}색을 좋아해요".format(color = "검정", age = 27)) # 순서가 바뀌어도 괄호안의 정의되어 있어 값은 변하지 않음

# 방법 4 (v3.6 이상)
age = 27
color = "검정"
print(f"나는 {age}살이며, {color}색을 좋아해요")
