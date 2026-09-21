from adapters.base import AdapterContract
from agent import TestMedic

class ClaudeAdapter(AdapterContract):
    framework="claude"
    def run(self,path):
        return TestMedic().inspect(path).to_dict()
    def verify(self,path):
        result=self.run(path)
        return {"framework":self.framework,"mode":"portable","verified":super().verify(path),"result":result}
