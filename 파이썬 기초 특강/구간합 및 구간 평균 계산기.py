A = int(input("A의 값을 입렧해주세요 : "))
B = int(input ("B의 값을 입력해주세요 : "))
if A > B: A,B = B,A
range = range(A,B+1)
print('합계는 : %d' % sum(range))
print('평균은 : %.2f' % (sum(range) / len(range)))