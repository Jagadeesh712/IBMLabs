R = int(input("Enter the number of rows:")) 
C = int(input("Enter the number of columns:"))
matrix = []
print("Enter the entries for array 1:")
for i in range(R):
    a =[]
    for j in range(C):
         a.append(int(input()))
    matrix.append(a)
print("Enter the entries for array 2:")
for i in range(R):
        b = []
        for j in range(C):
             b.append(int(input()))
    matrix.append(b)
