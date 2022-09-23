x, y, w, h = map(int, input().split())
answers = [x, y, w - x, h - y]
print(min(answers))
