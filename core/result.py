class Result:
    def __init__(self,data,diagnosis):
        self.data=data
        self.diagnosis=diagnosis
    def to_dict(self):
        return {"data":self.data,"diagnosis":self.diagnosis}
    def summary(self):
        if self.diagnosis["status"]=="healthy":
            return "No known problems were detected."
        return f"{len(self.diagnosis.get('findings',[]))} problem(s) detected."
