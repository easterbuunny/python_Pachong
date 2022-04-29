# 写入文件
def writer(filename, content):
    file = open(filename, "a")
    file.write(content)
    file.close()
