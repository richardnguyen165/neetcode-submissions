class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score_total = []

        for operation in operations:
            if operation == "D":
                score_total.append(score_total[-1] * 2)
            elif operation == "C":
                score_total.pop()
            elif operation == "+":
                score_total.append(score_total[-1] + score_total[-2])
            else:
                score_total.append(int(operation))

        return sum(score_total)