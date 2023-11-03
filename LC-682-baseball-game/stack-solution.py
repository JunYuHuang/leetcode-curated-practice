# O(N) T and O(N) S stack solution
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []
        for op in operations:
            if op == '+':
                records.append(records[-1] + records[-2])
            elif op == 'D':
                records.append(records[-1] * 2)
            elif op == 'C':
                records.pop()
            else: # op is an int char
                records.append(int(op))
        return sum(records)
