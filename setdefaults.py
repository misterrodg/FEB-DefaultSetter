import argparse

from modules.FEBDefaults import FEBDefaults
from modules.FileHandler import FileHandler
from modules.GeoJSON import GeoJSON


def processDefaults(sourceDir, fileName):
    print("\nGetting Defaults from FEB Defaults File")
    febDefaults = FEBDefaults(sourceDir, fileName)
    return febDefaults.defaults


def processFiles(sourceDir, useSourceLocal, outputDir, useOutputLocal, defaultsArray):
    fileHandler = FileHandler()
    fileHandler.checkDir(outputDir, useOutputLocal)
    fileHandler.deleteAllInSubdir(".geojson", outputDir, useOutputLocal)
    fileList = fileHandler.searchForType(".geojson", sourceDir, useSourceLocal)
    print(f"Checking in {sourceDir} with useSourceLocal {useSourceLocal}")
    numFiles = str(len(fileList))
    print(f"Found {numFiles} .geojson files in {sourceDir}")
    fileCount = 0
    for f in fileList:
        fileData = fileHandler.splitFolderFile(f, sourceDir)
        folder = fileData[0]
        fileName = fileData[1].replace(".geojson", "")
        defaults = next(
            (item for item in defaultsArray if item["fileName"] == fileData[1]), False
        )
        if defaults:
            print(f"[{str(fileCount + 1)}/{numFiles}] Processing {fileName}.geojson")
            GeoJSON(sourceDir, outputDir, fileName, defaults["default"])
            fileCount += 1
    print("\n>>>>> Defaults are now set. Files located in " + outputDir + "<<<<<\n")


def main():
    # Set up Defaults
    SOURCE_DIR = "feb_source"
    OUTPUT_DIR = "output"
    FEB_DEFAULTS = "vNAS_Defaults.txt"
    # Set up Argmument Handling
    parser = argparse.ArgumentParser(description="FEB-DefaultSetter")
    parser.add_argument(
        "--sourcedir", type=str, help="The path to the source directory."
    )
    parser.add_argument(
        "--outputdir", type=str, help="The path to the output directory."
    )
    parser.add_argument(
        "--defaultsfile", type=str, help="The filename of the FEB Defaults File."
    )
    args = parser.parse_args()
    sourceDir = SOURCE_DIR
    useSourceLocal = True
    outputDir = OUTPUT_DIR
    useOutputLocal = True
    if args.sourcedir != None:
        sourceDir = args.sourcedir
        useSourceLocal = False
    if args.outputdir != None:
        outputDir = args.outputdir
        useOutputLocal = False
    febDefaults = args.defaultsfile if args.defaultsfile != None else FEB_DEFAULTS
    print("\nInitializing DefaultSetter")
    # Read the defaults from the FEB List
    defaultsArray = processDefaults(sourceDir, febDefaults)
    # Process the files from the FEB List
    processFiles(sourceDir, useSourceLocal, outputDir, useOutputLocal, defaultsArray)


if __name__ == "__main__":
    main()
