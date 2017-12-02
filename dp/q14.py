"""
问题描述：给定一个整型数组arr，代表数值不同的纸牌排成一条线。玩家A和玩家B依次拿走每张
纸牌，规定玩家A先拿，玩家B后拿，但是每个玩家每次只能拿走最左或最右的纸牌，玩家A和玩家
B都绝顶聪明，请返回最后获胜者的分数。

举例：
arr=[1, 2, 100, 4]
开始时玩家A只能拿走1或者4，如果玩家A拿走1，则排列变成[2, 100, 4]，接下来玩家B可以拿走
2或者4，然后继续轮到玩家A。如果开始时玩家A拿走4，则排列变成[1, 2, 100]，接下来B可以拿
走1或者100，然后继续轮到玩家A。玩家A作为聪明绝顶的人不会先拿走4，因为拿走4后，玩家B将拿
走100。所以玩家A会先拿走1，让排列变成[2, 100, 4]，接下来玩家B不管怎么选，100都会被玩
家A拿走。玩家A获胜，分数是101，则返回101.
arr=[1,100,2]
开始时玩家A不管拿走1还是2，玩家B作为聪明绝顶的人，都会把100拿走，玩家B会获胜。分数为100，
所以返回100。
"""


class MaxCardNum:
    @classmethod
    def get_max_num_way_1(cls, arr):
        if not arr:
            return 0

        return max([cls.first_fetch(arr, 0, len(arr)-1), cls.last_fetch(arr, 0, len(arr)-1)])

    @classmethod
    def first_fetch(cls, arr, i, j):
        if i == j:
            return arr[i]
        return max([arr[i]+cls.last_fetch(arr, i+1, j), arr[j]+cls.last_fetch(arr, i, j-1)])

    @classmethod
    def last_fetch(cls, arr, i, j):
        if i == j:
            return 0

        return min([cls.first_fetch(arr, i+1, j), cls.first_fetch(arr, i, j-1)])

    @classmethod
    def get_max_num_way_2(cls, arr):
        if not arr:
            return 0

        first_fetch = [[0 for _ in arr] for _ in arr]
        last_fetch = [[0 for _ in arr] for _ in arr]

        for j in range(len(arr)):
            first_fetch[j][j] = arr[j]
            i = j - 1
            while i >= 0:
                first_fetch[i][j] = max([arr[i]+last_fetch[i+1][j], arr[j]+last_fetch[i][j-1]])
                last_fetch[i][j] = min([first_fetch[i+1][j], first_fetch[i][j-1]])
                i -= 1

        return max([first_fetch[0][len(arr)-1], last_fetch[0][len(arr)-1]])


if __name__ == '__main__':
    my_arr = [1, 9, 1]
    print(MaxCardNum.get_max_num_way_1(my_arr))
    print(MaxCardNum.get_max_num_way_2(my_arr))