# with open('new 2.txt','w') as f:
#     f.write('test')
#     f.seek(0)
#     f.write('test')
#*******************************

# with open('new 1.txt','r') as rf:
#     with open('new 2.txt','w') as wf:
#         for line in rf:wf.write(line)
#
# with open('new 2.txt','r') as f:
#     print(f.read())

#******************************* for images

with open('hc.jpg','rb') as rf:
    with open('hc_copy.jpg','wb') as wf:
        chnkSize = 4000
        rfchunk = rf.read(chnkSize)
        while len(rfchunk) > 0:
            wf.write(rfchunk)
            rfchunk = rf.read(chnkSize)





#*******************************
# with open('new 1.txt','r+') as f:
    # fContents = f.read()
    # fContents = f.readlines()
    # fContents =f.readline()

    # for line in f:
    #     print(line, end = '')

    # fContents = f.read(100)
    # print(fContents)

    # sizeToRead = 10
    # fContents = ' '
    # while len(fContents)>0:
    #     fContents = f.read(sizeToRead)
    #     print(fContents, end = '\n')
    #     print(f.tell())

    # sizeToRead = 10
    # fContents = f.read(sizeToRead)
    # print(fContents, end='\n')
    # f.seek(0)
    # fContents = f.read(sizeToRead)
    # print(fContents)
