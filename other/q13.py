"""
问题描述:给定一个路劲paths,表示一张图.paths[i]=j代表城市i连向城市j,如果paths[i]=i,则表示
i城市是首都,一张图里只会有一个首都且图中除首都指向自己之外不会有环.例如,paths=[9,1,4,9,0,4,8,9,0,1],
由题意可知，城市１是首都,所以距离是0,离首都距离为1的城市只有9,离首都距离为2的城市有城市0、３和7,离首都
距离为３的城市有4和8,离首都距离为４的城市有2、５和６.所以距离为0的城市有１座，距离为１的城市有１座，距
离为２的城市有３座，距离为３的城市有２座，距离为４的城市有３座。那么统计数组为nums=[1,1,3,2,3,0,0,0,0,0],
nums[i]==j代表距离为i的城市有j座.
要求实现一个void类型的函数,输入一个路径数组paths,直接在原数组上调整，使之变成nums数组，即paths=[9,1,4,0,4,8,9,0,1],
经过这个函数处理后变成[1,1,3,2,3,0,0,0,0,0]
"""


class PathProblem:
    @classmethod
    def get_res(cls, paths):
        if not paths:
            return

        distances = cls.get_distances(paths)
        return cls.get_nums_by_distances(distances)

    @classmethod
    def get_distances(cls, paths):
        cap = 0
        for i in range(len(paths)):
            if paths[i] == i:
                cap = i
            else:
                tmp = i
                if paths[tmp] > 0:
                    # 初始位置为-1
                    pre_index = -1
                    # 当没跳到首都的时候
                    while paths[tmp] != tmp:
                        # 如果是未跳过的位置（为正）
                        if paths[tmp] > -1:
                            # 下一个位置
                            next_index = paths[tmp]
                            # 保存前一个位置的index
                            paths[tmp] = pre_index
                            # 记录当前位置为前一个位置
                            pre_index = tmp
                            # 将当前位置设置为下一个位置
                            tmp = next_index
                        else:
                            # 如果tmp是跳过的位置,则直接跳出循环
                            break

                    # 如果是跳到了首都
                    if paths[tmp] > 0:
                        value = -1
                    else:
                        # 跳到一个已经跳到过的位置
                        value = paths[tmp] - 1

                    while paths[pre_index] != -1:
                        pre_pos = paths[pre_index]
                        paths[pre_index] = value
                        value -= 1
                        pre_index = pre_pos
                    else:
                        paths[pre_index] = value
                else:
                    continue

        paths[cap] = 0
        return paths

    @classmethod
    def get_nums_by_distances(cls, distances):
        print(distances)
        for i in range(len(distances)):
            if distances[i] == 0:
                distances[0] = 1
                continue
            if distances[i] > 0:
                continue

            index = distances[i]
            distances[i] = 0
            while True:
                index = -index
                if distances[index] > -1:
                    distances[index] += 1
                    break
                else:
                    next_index = distances[index]
                    distances[index] = 1
                    index = next_index

        return distances


if __name__ == '__main__':
    my_path = [9, 1, 4, 9, 0, 4, 8, 9, 0, 1]
    print(PathProblem.get_res(my_path))
