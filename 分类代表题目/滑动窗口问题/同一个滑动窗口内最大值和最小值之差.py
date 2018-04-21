import sys


class MaxValueOFWindow:
    def get_diff_values(self, arr, window):
        if len(arr) == 0 or window < 1 or len(arr) < window:
            return list()

        index = 0
        # slide window
        max_deque = list()
        min_deque = list()
        # len(max_values) = len(arr) - window + 1
        max_values = list()
        min_values = list()

        while index < len(arr):
            # 保存队列的单调性，最大值为单调递减，最小值队列为单调递增
            while len(max_deque) > 0 and arr[max_deque[-1]] <= arr[index]:
                max_deque.pop()
            while len(min_deque) > 0 and arr[min_deque[-1]] >= arr[index]:
                min_deque.pop()
            max_deque.append(index)
            min_deque.append(index)

            # 清理过期的值
            if max_deque[-1] - max_deque[0] == window:
                max_deque.pop(0)
            if min_deque[-1] - min_deque[0] == window:
                min_deque.pop(0)

            # 窗口大小为window再开始收集结果
            if index >= window - 1:
                max_values.append(arr[max_deque[0]])
            if index >= window - 1:
                min_values.append(arr[min_deque[0]])

            index += 1

        index = 0
        res = list()
        while index < len(min_values):
            res.append(max_values[index] - min_values[index])
            index += 1

        return res


if __name__ == '__main__':
    line = sys.stdin.readline().strip()
    arr_len, window_len = list(map(int, line.split()))
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))
    res = MaxValueOFWindow().get_diff_values(values, window_len)
    index = 0
    while index < len(res):
        if index < len(res) - 1:
            print(res[index], end=' ')
        else:
            print(res[index])
        index += 1
