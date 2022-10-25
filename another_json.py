#!/usr/bin/python3
from typing import List
import json


class GFG_User(object):
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

user = GFG_User(first_name="Jake", last_name="Doyle")
json_data = json.dumps(user.__dict__)
print(json_data)
print(GFG_User(**json.loads(json_data)))
print('-------------------------')

class Student(object):
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

class Team(object):
    def __init__(self, students: List[Student]):
        self.students = students


student1 = Student(first_name="Geeky", last_name="Guy")
student2 = Student(first_name="GFG", last_name="Rocks")
team = Team(students=[student1, student2])

#serialization
json_data = json.dumps(team.__dict__, default=lambda o:o.__dict__, indent=4)
print(json_data)

#deserialization
decoded_team = json.loads(json_data)
print(decoded_team)
