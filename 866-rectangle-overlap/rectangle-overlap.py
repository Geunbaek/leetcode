class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        def to_dict(rec):
            x1, y1, x2, y2 = rec
            return { "x1": x1, "y1": y1, "x2": x2, "y2": y2 }

        rec1 = to_dict(rec1)
        rec2 = to_dict(rec2)

        if (rec1["x1"] == rec1["x2"] or rec1["y1"] == rec1["y2"] or \
            rec2["x1"] == rec2["x2"] or rec2["y1"] == rec2["y2"]):
            return False

        return not (rec1["x2"] <= rec2["x1"] or  
                    rec1["y2"] <= rec2["y1"] or 
                    rec1["x1"] >= rec2["x2"] or  
                    rec1["y1"] >= rec2["y2"])   