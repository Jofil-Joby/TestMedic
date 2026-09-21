class AdapterContract:
    framework="unknown"
    def run(self,path):
        raise NotImplementedError()
    def verify(self,path):
        result=self.run(path)
        return isinstance(result,dict) and "data" in result and "diagnosis" in result
