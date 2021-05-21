def generator():
    yield 1
    yield 2
    yield 3
    
print(generator)        # 1

print(generator())      # 2

for i in generator():   # 3
    print(i)
    
g = generator()
print(next(g))          # 4
