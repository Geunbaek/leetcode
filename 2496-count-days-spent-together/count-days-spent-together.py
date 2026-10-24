class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        cache = [0 for _ in range(sum(days) + 1)]

        def dtoi(month, date):
            return sum(days[:month - 1]) + date

        def visit(arrive, leave):
            am, ad = map(int, arrive.split("-"))
            lm, ld = map(int, leave.split("-"))

            for i in range(dtoi(am, ad), dtoi(lm, ld) + 1):
                cache[i] += 1

        visit(arriveAlice, leaveAlice)     
        visit(arriveBob, leaveBob)   

        answer = 0
        for v in cache:
            if v == 2:
                answer += 1
        return answer