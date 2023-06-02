# 1. 1부터 n까지의 합 계산하기
def sum(n):
    if n==1:
        return 1
    else:
        return sum(n-1)+n 
    
# 점화식: T(n)=T(n-1)+1 T(1)=1
# 바닥의 경우에 이를때까지 전개하면 T(n)=T(1)+(1+...+1)=n=O(n)

print(sum(3))