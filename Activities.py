from string import Template
import json

class Activities:
    
    def createActivities(self, dataDict):
        ret = dict()
        with open('../Pages/Activities.html', 'r') as file:
            content = file.read()
            ret["content"] = (Template(content)).safe_substitute(dataDict)
        return ret
