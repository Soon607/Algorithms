# 1~n 까지 합 다르게 구하기
# 함수에 두값이 주어질때 (a,b)
# a,b사이의 값은 m
# a<=b 라 가정

def sum(a,b):
    if a==b:
        return a
    if a>b:
        return 0
    m=(a+b)//2
    return sum(a,m)+sum(m+1,b)

print(sum(1,3))