import os
from tools.scanner import scan_target
from tools.checker import check
from core.result import Result

class TestMedic:
    def inspect(self,path):
        if not os.path.exists(path):
            return Result({}, {"status":"error","message":"The specified project path does not exist."})
        data=scan_target(path)
        return Result(data,check(path,data))

if __name__=="__main__":
    result=TestMedic().inspect("tests/broken_project")
    print("TestMedic Agent")
    print("================")
    print("Summary:",result.summary())
    print("Status:",result.diagnosis["status"])
    for i,finding in enumerate(result.diagnosis.get("findings",[]),1):
        print(f"\nProblem {i}")
        for key in ["problem","cause","evidence","suggested_fix","confidence"]:
            print(f"{key.title()}: {finding[key]}")
