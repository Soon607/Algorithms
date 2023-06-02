# 5. 리스트의 모든 부분집합 출력하기
# 부분집합의 갯수가 2**n 이므로 그 이상의 수행시간이 필요하다.

def print_subsets(arr,subset=[],index=0):
    if index==len(arr): # 모든 요소를 처리
        print(subset)
    else: # 그렇지 않은 경우, 현재 요소를 제외한 부분집합을 생성하기 위해 index를 증가시켜 함수 호출
        print_subsets(arr,subset,index+1)
        print_subsets(arr,subset+[arr[index]],index+1) # 현재 요소를 포함한 부분집합을 생성하기 위해 index를 증가시키고 subset에 현재 요소를 추가한 상태로 함수 재귀호출
        
        
# index=0에서 시작
# index=0일때 print_subsets(arr,subset,index+1) 호출하여 다음요소를 제외한 부분집합 생성 [2,3]부분집합 생성
# print_subsets(arr, subset + [arr[index]], index + 1)을 호출하여 현재 요소를 포함한 부분집합을 생성합니다. 즉, [1, 2, 3] 부분집합이 생성
# index = 1일 때, [3] 부분집합과 [1, 3] 부분집합이 생성
# 마지막으로 index = 2일 때, [1]과 [2] 부분집합이 생성

a=[1,2,3]
print_subsets(a)