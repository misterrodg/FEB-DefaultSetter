class FEBDefaults:
    def __init__(self, sourceFolder, fileName):
        self.defaultFileName = "./" + sourceFolder + "/" + fileName + ".txt"
        self.defaults = []
        self.read()

    def add(self,fileName,default):
        newItem = {"fileName": fileName, "default": default}
        self.defaults.append(newItem)

    def read(self):
        currentFile = ""
        currentDefaults = ""
        with open(self.defaultFileName) as lines:
            for line in lines:
                if line.endswith(".geojson\n"):
                    currentFile = line.strip()
                if line.startswith("{\"type\":\"Feature\","):
                    withoutComma = line.rstrip(',\n')
                    currentDefaults = withoutComma.strip()
                if currentFile != "" and currentDefaults != "":
                    self.add(currentFile,currentDefaults)
                    currentFile = ""
                    currentDefaults = ""