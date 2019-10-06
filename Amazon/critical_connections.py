from collections import defaultdict

class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        disc = [None for _ in range(n+1)]
        low = [None for _ in range(n+1)]

        graph = defaultdict(list)
        for c in connections:
            graph[c[0]].append(c[1])
            graph[c[1]].append(c[0])
        
        self.time = 0
        bridges = []

        def dfs(node, parent):
            if disc[node] is None:
                disc[node] = self.time
                low[node] = self.time
                self.time += 1
                for n in graph[node]:
                    if disc[n] is None:
                        dfs(n, node)
                if parent is not None:
                    l = min([low[i] for i in graph[node] if i!=parent]+[low[node]])
                else:
                    l = min(low[i] for i in graph[node]+[low[node]])
                low[node] = l

        dfs(1, None)

        for v in connections:
            if disc[v[0]]<low[v[1]] or disc[v[1]]<low[v[0]]:
                bridges.append(v)

        return bridges

if __name__ == '__main__':
    n = 9
    edges = [[1, 2], [1, 3], [2, 3], [3, 4], [3, 6], [4, 5], [6, 7], [6, 9], [7, 8], [8, 9]]
    solution = Solution()
    print solution.criticalConnections(n, edges)
    
    