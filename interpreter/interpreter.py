r=input("Expression: ")
r=r.split()
x=int(r[0])
y=r[1]
z=int(r[2])

ans = eval(f"{x} {y} {z}")
print(f"{ans:.1f}")


