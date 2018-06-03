# 拓扑排序
def indegree0(v, e):
    if not v:
        return None
    tmp = v[:]
    # 找出入度为0的节点
    for i in e:
        if i[1] in tmp:
            tmp.remove(i[1])

    if not tmp:
        return -1

    # 在关系图中标记出入度为0的节点
    for t in tmp:
        for i in range(len(e)):
            if t in e[i]:
                e[i] = 'useless'

    if v:
        for t in tmp:
            v.remove(t)
    return tmp


def top_sort(v, e):
    result = []
    while True:
        nodes = indegree0(v, e)
        if nodes == -1:
            print('there\'s a circle.')
            return
        elif not nodes:
            break
        else:
            result.extend(nodes)
    return result


if __name__ == '__main__':
    v = ['a', 'b', 'c', 'd', 'e']
    e = [('a', 'b'), ('a', 'd'), ('b', 'c'), ('d', 'c'), ('d', 'e'), ('e', 'c')]
    res = top_sort(v, e)
    print(res)

