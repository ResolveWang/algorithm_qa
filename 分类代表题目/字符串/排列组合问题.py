class Solution:
    def conbition(self, input_str):
        if not input_str:
            return list()

        length = len(input_str)
        res = list()
        for i in range(1, length+1):
            self.pick_n_from_str(input_str, '', i, res)
        return res

    def pick_n_from_str(self, input_str, pre_str, n, res):
        # f(n, m) = f(n-1, m-1) + f(n-1, m)
        if len(pre_str) == n:
            res.append(pre_str)
            return

        if not input_str:
            return

        self.pick_n_from_str(input_str[1:], pre_str, n, res)
        self.pick_n_from_str(input_str[1:], pre_str+input_str[0], n, res)


    def Permutation(self, ss):
        if not ss:
            return list()
        res = list()
        self.process(ss, '', res)
        return sorted(list(set(res)))

    def process(self, ss, pre_ss, res):
        if len(ss) == 1:
            new_str = pre_ss + ss
            res.append(new_str)
            return

        index = 0
        while index < len(ss):
            cur_str = pre_ss + ss[index]
            new_ss = ss[:index] + ss[index + 1:]
            self.process(new_ss, cur_str, res)
            index += 1

