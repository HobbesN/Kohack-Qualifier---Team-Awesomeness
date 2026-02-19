import math
import random
import json

class Assignment:
    def __init__(self, AssignmentName, Class, DueDate, Platform):
        self.AssignmentName = AssignmentName
        self.Class = Class
        self.DueDate = DueDate
        self.Class = Platform


def load_model():
    output = []
    with open("model.json", "r") as f:
        data = json.load(f)
        for i in range(0,len(data)):
            output= data["DataList"]
    return Turn_List_to_list_of_assignments(output)
def upload_List(CurrentList):
    if( math.floor(len(CurrentList)/4))!=len(CurrentList)/4:
        print("Error: List length is not a multiple of 4")
        return
    with open("model.json", "w") as f:
        json.dump({"DataList": CurrentList}, f)
def Turn_List_to_list_of_assignments(DataList):
    AssignmentList = [0]*math.floor(len(DataList)/4)
    for i in range(0, math.floor(len(DataList)/4)):
        AssignmentList[i]=Assignment(DataList[4*i],DataList[4*i+1], DataList[4*i+2], DataList[4*i+3])
    return AssignmentList
def sortByQuality(AssignmentList,quality):
    outputlist = [0]*len(AssignmentList)
    if quality == "DueDate":
        outputlist = AssignmentList.sort(key=lambda x: x.DueDate)
    elif quality == "Class":
        outpuList = ClassSort(AssignmentList)
    elif quality == "Platform":
        outputlist = PlatformSort(AssignmentList)
    return outputlist
def PlatformSort(OurList):
    List = OurList
    OutputList = []
    for i in range(0, len(List)):
        if List[i].Platform=="Google Classroom":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Platform=="GClassroom":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Platform=="Google Class":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Platform=="בשביל העברית":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Platform=="Bishvil HaIvrit":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Platform=="Bishvil Haivrit":
            OutputList.append(List[i]) 
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Platform=="Blackbaud":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Platform=="BlackBaud":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
            OutputList.append(List[i])
    return OutputList
def ClassSort(OurList):
    List = OurList
    OutputList = []
    for i in range(0, len(List)):
        if List[i].Class=="Hebrew":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="hebrew":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="עברית":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="English":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="English":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="History":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="history":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="American Studies":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="american studies":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="Euro":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="euro":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="European History":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="european history":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="Chumash":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="חומש":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="Navi":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="Nach":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="נביים":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="נכ":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="Judaic Studies":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="Gemara":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="gemara":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="גמרא":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="math":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="Math":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="Mathematics":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="mathematics":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="algebra":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="Algebra":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="Geometry":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="geometry":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="precalc":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="Precalc":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="pre-calc":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="Pre-calc":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="Pre-Calc":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="pre-calculus":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="Calculus":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="calculus":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="Calc":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="calc":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="calc AB":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="Calc AB":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="calc ab":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="Calc ab":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="calculus AB":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="Calculus AB":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="calculus ab":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="Calculus ab":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="calc BC":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="Calc BC":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="calc bc":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="Calc bc":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="calculus BC":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="Calculus BC":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="calculus bc":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="Calculus bc":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="Science":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="science":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="sci":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="Biology":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="biology":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="bio":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="Chem":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="chem":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="Chemistry":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="chemistry":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="Physics":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="physics":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
        if List[i].Class=="AP physics":
            OutputList.append(List[i])
            List.remove(List[i])
    for i in range(0, len(List)):
            OutputList.append(List[i])
    return OutputList
newlist= load_model()
print(newlist)
print(len(newlist))
print(len(sortByQuality(newlist,"Class")))
dataList = ["Hebrew Work Sheet 1", "Hebrew", 2026228, "Google Classroom", "Math Homework 1", "Math", 2026310, "Blackbaud"]
upload_List(dataList)