print("Введите N ")
try:
 N = int(input())
except ValueError:
 print('Ошибка ')
else:
  M = 0
  def abc ():
   global N
   N = N // 10
   return(N)
while N>0:
   N_1 = N % 10
   if N_1 % 2 == 1:
    M = M + N_1
    N = abc ()
   else:
    N = abc ()
print(M)