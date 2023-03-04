from enum import Enum

from typing import List

import datetime

class ExamType (Enum):
    MIDTERM = 1
    MAKEUP = 2
    FINAL = 3
    OTHER = 4

class Semester:
    def __init__ (
        self,
        year : str,
        quarter : str
    ):
        self.year = year
        self.quarter = quarter

    @classmethod
    def from_str (self, semester : str):
        year = semester[:4]
        quarter = semester[4:]
        return Semester(year, quarter)

class Exam:
    def __init__ (
        self,
        courseOpenedId : int,
        id : int,
        exam_type : str,
        semester : str,
        start_stamp : str,
        finish_stamp : str,
        description : str,
        student_count : int,
        roaming_assistant : str
    ):
        self.courseOpenedId = courseOpenedId
        self.id = id
        self.exam_type = ExamType[exam_type.upper()]
        self.semester = Semester.from_str(semester)
        self.start_stamp = datetime.datetime.strptime(
            start_stamp,
            "%Y%m%d%H%M%S"
        )
        self.finish_stamp = datetime.datetime.strptime(
            finish_stamp,
            "%Y%m%d%H%M%S"
        )
        self.description = description
        self.studentCount = student_count
        self.roamingAssistant = roaming_assistant


if __name__ == "__main__":
    data = {
        "submitterUserCode": "bilmezb",
        "courseOpenedId": 1461,
        "type": "makeup",
        "semester": "20221",
        "startStamp": "20230125133000",
        "finishStamp": "20230125160000",
        "id": 2798,
        "description": "CE241 Makeup",
        "studentCount": 10,
        "roamingAssistant": None
    }
    exam = Exam(
        courseOpenedId=data.get("courseOpenedId"),
        exam_type=data.get("type"),
        semester=data.get("semester"),
        start_stamp=data.get("startStamp"),
        finish_stamp=data.get("finishStamp"),
        id=data.get("id"),
        description=data.get("description"),
        student_count=data.get("studentCount"),
        roaming_assistant=data.get("roamingAssistant")
    )
    print(exam)
    print(exam.start_stamp, exam.finish_stamp)
        