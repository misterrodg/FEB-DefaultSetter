from modules.FEBDefaults import FEBDefaults
from modules.FileHandler import FileHandler
from modules.GeoJSON import GeoJSON

def processDefaults(sourceDir, fileName):
    print("\nGetting Defaults from FEB Defaults File")
    febDefaults = FEBDefaults(sourceDir, fileName)
    return febDefaults.defaults

def processFiles(sourceDir, outputDir, defaultsArray):
    fileHandler = FileHandler()
    fileHandler.checkDir(outputDir)
    fileHandler.deleteAllInSubdir(".geojson", outputDir)
    fileList = fileHandler.searchForType(".geojson", sourceDir)
    numFiles = str(len(fileList))
    print("Found " + numFiles + " .geojson files in ./" + sourceDir)
    fileCount = 0
    for f in fileList:
        fileData = fileHandler.splitFolderFile(f, sourceDir)
        folder = fileData[0]
        fileName = fileData[1].replace(".geojson", "")
        defaults = next((item for item in defaultsArray if item["fileName"] == fileData[1]), False)
        if defaults:
            print("[" + str(fileCount + 1) + "/" + numFiles + "] " + "Processing " + fileName + ".geojson")
            GeoJSON(sourceDir,outputDir,fileName, defaults["default"])
            fileCount += 1
    print("\n>>>>> Defaults are now set. Files located in ./" + outputDir + "<<<<<\n")

def main():
    # Set up Defaults
    SOURCE_DIR = "feb_source"
    OUPUT_DIR = "output"
    FEB_DEFAULTS = "FE-BUDDY AIRAC OUTPUT CRC DEFAULTS"
    print("\nInitializing DefaultSetter")
    # Read the defaults from the FEB List
    defaultsArray = processDefaults(SOURCE_DIR,FEB_DEFAULTS)
    # Process the files from the FEB List
    processFiles(SOURCE_DIR,OUPUT_DIR,defaultsArray)

if __name__ == "__main__":
    main()