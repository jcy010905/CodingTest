tree = {}

n = int(input())
for _ in range(n):
    root, left, right = input().split()
    tree[root] = (left, right)

def traverse(node, order):
    if node == '.':
        return ''
    left, right = tree[node]
    if order == '전위':
        return node + traverse(left, order) + traverse(right, order)  # 전위 순회
    elif order == '중위':
        return traverse(left, order) + node + traverse(right, order)  # 중위 순회
    elif order == '후위':
        return traverse(left, order) + traverse(right, order) + node  # 후위 순회

print(traverse('A', '전위'))
print(traverse('A', '중위'))
print(traverse('A', '후위'))
