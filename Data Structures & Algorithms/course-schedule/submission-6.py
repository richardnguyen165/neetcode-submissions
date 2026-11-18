class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Kahn's Algorithm

        '''
        Each course is a node
        each preresiquite is a directed edge

        if a course has no preresiquites, can be take immediately,
        we remove its dependency effect from other courses
        '''

        # [course, preresiquite]

        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]

        for course, preresiquite in prerequisites:
            indegree[preresiquite] += 1
            adj[course].append(preresiquite) # We want to get all the preresiquites of the course
        
        courses_stack = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                courses_stack.append(n)
        
        finish = 0
        while courses_stack:
            node = courses_stack.popleft()
            finish += 1
            for n in adj[node]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    courses_stack.append(n)
        
        return finish == numCourses


        