# 리스트의 값을 거꾸로 배치하기
# 1.
def reverse1(a):
    if len(a)==1:
        return a
    else:
        return reverse1(a[1:])+a[:1]
    
# 2.
def reverse2(a,start,stop): #stop-1까지 범위
    if start<stop-1: # 2개 이상의 값이 있는 경우에만 의미가 있다.
        a[start],a[stop-1]=a[stop-1],a[start]
        reverse2(a,start+1,stop-1)
    return a
        
A=[1,2,3,4,5,6]
print(reverse1(A))
print(reverse2(A,0,6))