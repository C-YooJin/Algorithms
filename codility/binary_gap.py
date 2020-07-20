def solution(N):
     # write your code in Python 3.6
     binary = bin(N)
     real_bin = binary[2:]

     idx_lst = []
     for index, value in enumerate(real_bin):
         if value == '1':
             idx_lst.append(index)

     result_lst = []
     for i in range(0, len(idx_lst)-1):
         tmp = idx_lst[i+1] - idx_lst[i] - 1
         result_lst.append(tmp)

     if result_lst == []:
         return 0

     return max(result_lst)