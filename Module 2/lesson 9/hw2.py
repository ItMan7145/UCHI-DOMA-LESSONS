try:
    masha, misha, n = map(int, input().split())
    div = (masha + misha) / n
except Exception as e:
    print(e.__class__.__name__)
else:
    print(div)
