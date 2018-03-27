import os
import re


def codeCounts(filepath):
    # file = open(filepath, 'r', encoding='utf-8')
    # text = file.read()
    pyList = []
    filelist = os.listdir(filepath)
    for file in filelist:
        Path = filepath + "/" + file
        if os.path.isfile(Path) and file.endswith('.py'):
            pyList.append(Path)
        elif os.path.isfile(Path) and not file.endswith('.py'):

            print('%s不是.py代码文件' % file)
        elif os.path.isdir(Path):
            filePath = Path
            # print('%s是文件夹' % file)
            pyList += codeCounts(filePath)
    return pyList


def fileCodeStatistics(path):
    file = open(path, 'r', encoding='utf-8')
    totalLine = 0
    emptyLine = 0
    commentLine = 0
    validLine = 0
    multipleComment = False
    lineList = file.readlines()
    file.close()
    for line in lineList:
        totalLine += 1
        pattern = r"^\s*'''"
        pattern2 = r".*'''\s*$"

        if line == '\n':
            emptyLine += 1
        elif re.match(r"^\s*'''.*'''\s*$", line) != None:
            multipleComment = False
            commentLine += 1
            # print('=========', line)
        elif re.match(pattern, line) != None and multipleComment == False:
            multipleComment = True
            commentLine += 1
            # print('————',line)
        elif re.match(pattern2, line) != None:
            multipleComment = False
            commentLine += 1
            # print('+++++', line)
        elif multipleComment:
            commentLine += 1

        elif re.match(r"^\s*#", line) != None and multipleComment == False:
            commentLine += 1


        validLine = totalLine - emptyLine - commentLine
    print('%s文件下总共有%d行，其中%d行是空行，%d行是注释，%d行是代码' % (path, totalLine, emptyLine, commentLine, validLine))
    if validLine < commentLine:
        print('%s是可疑对象' % path)
    return {'totalLine': totalLine, 'emptyLine': emptyLine, 'commentLine': commentLine, 'validLine': validLine}


if __name__ == '__main__':
    filepath = r"E:/爬虫/1"
    # flist = os.listdir(filepath)
    # print(flist)
    totalLine = 0
    emptyLine = 0
    commentLine = 0
    validLine = 0
    pyList = codeCounts(filepath)
    print('>>>>>>>>>>>>>>>>>>>>>>>')
    # fileCodeStatistics('./test2.py')
    for path in pyList:
        resdict = fileCodeStatistics(path)
        totalLine += resdict['totalLine']
        emptyLine += resdict['emptyLine']
        commentLine += resdict['commentLine']
        validLine += resdict['validLine']
    print('''
    %s文件下
    总共有%d行文档
    其中%d行是python代码占比%0.2f%%
    %d行是空行占比%0.2f%%
    %d行是注释占比%0.2f%%
    
    ''' % (filepath, totalLine, validLine, validLine/totalLine*100, emptyLine,emptyLine/totalLine*100, commentLine, commentLine/totalLine*100))



