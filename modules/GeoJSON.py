import json

class GeoJSON:
    def __init__(self, sourceFolder, outputFolder, fileName, defaults):
        self.fileName = sourceFolder + "/" + fileName + ".geojson"
        self.outputFileName = outputFolder + "/" + fileName + ".geojson"
        self.defaults = json.loads(defaults)
        self.read()

    def read(self):
        with open(self.fileName, "r") as geoJsonFile:
            data = json.load(geoJsonFile)
            data['features'].insert(0,self.defaults)
            with open(self.outputFileName, "w") as outputFile:
                json.dump(data,outputFile,separators=(',', ':'), indent=None)
