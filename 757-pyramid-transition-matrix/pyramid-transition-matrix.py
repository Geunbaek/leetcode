class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        allewed_cache = defaultdict(list)

        for bottom_left, bottom_right, top in allowed:
            allewed_cache[bottom_left, bottom_right].append(top)
        
        seen = set()
        def solve(line):
            if len(line) == 1:
                return True
            if line in seen: return False
            seen.add(line)
            return any(solve(cand) for cand in build(line, []))
        
        def build(line, parent_line, i = 0):
            if i + 1 == len(line):
                yield "".join(parent_line)
            else:
                for top in allewed_cache[line[i], line[i + 1]]:
                    parent_line.append(top)
                    for result in build(line, parent_line, i + 1):
                        yield result
                    parent_line.pop()

        return solve(bottom)
