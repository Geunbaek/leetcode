class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        def get_hour_angle(h, m):
            return (h * 360 / 12) + (m * (360 / 60 / 12))

        def get_minute_angle(m):
            return (m * (360 / 60))
        print(360 - get_hour_angle(hour % 12, minutes))
        print(get_minute_angle(minutes))
        return min(
            abs(get_hour_angle(hour % 12, minutes) - get_minute_angle(minutes)),
            360 - get_minute_angle(minutes) + get_hour_angle(hour % 12, minutes),
            360 - get_hour_angle(hour % 12, minutes) + get_minute_angle(minutes)
        )

