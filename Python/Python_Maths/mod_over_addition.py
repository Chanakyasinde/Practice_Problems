def fun():
    a, b=map(int, input().split())
    result= a+b
    result=result%(10**9+7)
    print(result)
fun()
