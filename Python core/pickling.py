import pickle as p
dic = {'a':100,'b':200,'c':300}
lst = [400,500,600]
print(dic,lst)

with open('save.pkl','wb') as pk:
    p.dump(dic,pk)
    p.dump(lst,pk)

print('..........................')

with open('save.pkl','rb') as pk:
    dc = p.load(pk)
    ls = p.load(pk)

print(dc,ls)
p
