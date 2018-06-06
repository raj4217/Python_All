# import xml.etree.ElementTree as et
# import os

# # print(os.getcwd())
# root = et.parse('data.xml').getroot()
# # print(root.getchildren()[0].getchildren())

# print(dir(root))
# # products = [x for x in root.findall('product')]
# # print(products['name'])
# # for i in products:
# #     print(i.findtext('name'),i.findtext('cost'))
for a in range(10):
    if a % 2 != 0:
        next(a)
    print(next(a))
