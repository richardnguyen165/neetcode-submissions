class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Topological sort
        all_neighbours = [0] * numCourses

        all_prereqs = {}
        for n in range(numCourses):
            all_prereqs[n] = []
        for course, prereq in prerequisites:
            all_neighbours[course] += 1 # add the indegrees
            all_prereqs[prereq].append(course) # prereq -> course

        all_completed = set()
        current_courses = deque()
        all_attended = []

        # Add all zero degrees to queue
        for index, in_degree in enumerate(all_neighbours):
            if in_degree == 0:
                current_courses.append(index)
                all_completed.add(index)

        while current_courses:
            course = current_courses.popleft()
            all_attended.append(course)

            # Decrement all neighbors in degree
            all_neighbors = all_prereqs[course]
            for n in all_neighbors:
                all_neighbours[n] -= 1
                # Queue all courses that have the inbound degrees of 0, and are not visited
                if n not in all_completed and all_neighbours[n] == 0:
                    current_courses.append(n)
                    all_completed.add(n)

            # # Queue all courses that have the inbound degrees of 0, and are not visited
            # for n in range(numCourses):
            #     if n not in all_completed and all_neighbours[n] == 0:
            #         current_courses.append(n)
            #         all_completed.add(n)

        if len(all_attended) == numCourses:
            return all_attended
        return []


