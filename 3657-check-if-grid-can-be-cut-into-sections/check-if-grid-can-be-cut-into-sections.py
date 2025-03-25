class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def check_valid_cuts(div):
            sorted_rectangles = sorted(rectangles, key=lambda x: x[div])
            
            cut = 0
            current_end_line = sorted_rectangles[0][div + 2]

            for rect in sorted_rectangles[1:]:
                if current_end_line <= rect[div]:
                    cut += 1

                current_end_line = max(current_end_line, rect[div + 2])

            return cut >= 2
        
        return check_valid_cuts(0) or check_valid_cuts(1)
