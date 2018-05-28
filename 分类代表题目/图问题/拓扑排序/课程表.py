"""
问题: 现在你总共有 n 门课需要选，记为 0 到 n-1。

在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，
你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]
给定课程总量以及它们的先决条件，判断是否可能完成所有课程的学习？

示例:
2, [[1,0],[0,1]] => False
2, [[1, 0]] => True

思路:
拓扑排序，找到入度为0的点，依次消除，如果最后可完全消除，那么则无环
"""


import operator


class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if not numCourses:
            return False

        if not prerequisites:
            return True

        while prerequisites:
            rs = self.find_root(prerequisites)
            if not rs:
                return False

            new_require = list()
            for item in prerequisites:
                if item[1] not in rs:
                    new_require.append(item)
            prerequisites = new_require
        return True

    def find_root(self, prerequisites):
        child_getter = operator.itemgetter(0)
        parent_getter = operator.itemgetter(1)
        return set(map(parent_getter, prerequisites)) - set(map(child_getter, prerequisites))
