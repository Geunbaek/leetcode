class Solution:
    def kEmptySlots(self, bulbs: List[int], k: int) -> int:
        lights = []

        for day, bulb in enumerate(bulbs, 1):
            l, r = 0, len(lights) - 1

            while l <= r:
                mid = (l + r) // 2

                if lights[mid] <= bulb:
                    r = mid - 1
                else:
                    l = mid + 1

            for light in lights[l - (l > 0): l + 1]:
                if abs(light - bulb) - 1 == k:
                    return day
            lights.insert(l, bulb)
        return -1