import math
import random
import json

class Assignment:
    def __init__(self, AssignmentName, Class, DueDate, Platform):
        self.AssignmentName = AssignmentName
        self.Class = Class
        self.DueDate = DueDate
        self.Class = Platform


def load_model(path):
    with open(path, "r") as f:
        data = json.load(f)
    return data 
def upload_List(CurrentList):
    with open("model.json", "w") as f:
        json.dump({"DataList": CurrentList}, f)
