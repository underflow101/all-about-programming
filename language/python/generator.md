# Generator

- 제너레이터 함수는 일반 함수와는 다르게, 함수의 코드 블록을 한 번에 실행하지 않고, 함수 코드 블록의 실행을 일시중지했다가 필요한 시점에 재시작할 수 있는 특수한 함수이다. 일반 함수를 호출하면 return문으로 반환값을 리턴하지만 제너레이터 함수를 호출하면 제너레이터를 반환한다.
  - 특히, 파이썬에서는 제너레이터 객체를 반환한다.

### 예시 소스코드
<pre><code>def generator():
    yield 1
    yield 2
    yield 3
    
print(generator)        # 1

print(generator())      # 2

for i in generator():   # 3
    print(i)
    
g = generator()
print(next(g))          # 4</code></pre>

### 예시 output
  - output 1
    <br><code><function generator at 0x7f23d896b1f0></code><br>
  - output 2
    <br><code><generator object generator at 0x7f23d87fc270></code><br>
  - output 3
    <br><pre><code>1
    2
    3</code></pre>
  - output 4
    <br><pre><code>1</code></pre>
