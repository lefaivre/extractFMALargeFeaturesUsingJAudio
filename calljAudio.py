import os
import glob
import copy
import subprocess

def getFilesInDirWithExt(dir, ext):
    toreturn = []
    os.chdir(dir)
    for file in glob.glob(ext):
        toreturn.append(dir + file)
    return toreturn

batchTemplate = []
with open('D:\\jAudio\\batchfiles\\template.xml') as f:
    batchTemplate = f.readlines()

mainpath = "F:\\fma_large\\" 

allAudioFolders = os.listdir(mainpath)

# Need to create all batch files first.
for num in allAudioFolders:

    folder = mainpath + num + "\\"
    wavFilesInFolder = getFilesInDirWithExt(folder, "*.wav")

    output = batchTemplate[0:27]
    output.append("\t<batch ID=\"" + num + "\">\n")

    fileSetStrings = []
    fileSetStrings.append("\t\t<fileSet>\n")
    for wavFile in wavFilesInFolder:
        fileSetStrings.append("\t\t\t<file>" + wavFile + "</file>\n")
    fileSetStrings.append("\t\t</fileSet>\n")
    output.extend(fileSetStrings)
    output.extend(batchTemplate[31:770])
    output.append("\t\t<destination>" + "D:\\jAudio\\fma_large\\" + num + ".arff</destination>\n")
    output.append("\t\t<destination>" + "D:\\jAudio\\fma_large\\" + num + ".arff</destination>\n")
    output.extend(batchTemplate[772:775])

    with open('D:\\jAudio\\batchfiles\\' + num + ".xml", 'w') as f:
        f.writelines(output)


# run batch files!
batchFileDir = "D:\\jAudio\\batchfiles\\"
allBatchFiles = os.listdir(batchFileDir)

for batchFile in allBatchFiles:
    if not (batchFile == "template"):
        thisBatchFile = batchFileDir + batchFile
        os.chdir("D:\\jAudio")
        FNULL = open(os.devnull, 'w')
        subprocess.call('java -mx500M -jar jAudio-1.0.4.jar -b ' + thisBatchFile, shell=True,  stdout=FNULL, stderr=subprocess.STDOUT)



