class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        rooms = [0] * n # end time of meetings in rooms
        meeting_count = [0] * n

        for s, e in meetings:
            min_room = 0
            found = False
            for i in range(n):
                if rooms[i] <= s:
                    found = True
                    meeting_count[i] += 1
                    rooms[i] = e
                    break

                if rooms[min_room] > rooms[i]:
                    min_room = i
            if found:
                continue
            meeting_count[min_room] += 1
            rooms[min_room] += e - s

        return meeting_count.index(max(meeting_count))