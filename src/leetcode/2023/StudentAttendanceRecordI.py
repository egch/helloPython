# You are given a string s representing an attendance record for a student where each character signifies whether the
# student was absent, late, or present on that day. The record only contains the following three characters:
#
# 'A': Absent.
# 'L': Late.
# 'P': Present.


class StudentAttendanceRecordI:
    def checkRecord(self, s: str) -> bool:
        numA = 0
        numL = 0
        for c in s:
            if c == 'A':
                numA = numA + 1
                numL = 0
            elif c == 'L':
                numL = numL + 1
            else:
                numL = 0
            if numA >= 2 or numL >= 3:
                return False
        return True
