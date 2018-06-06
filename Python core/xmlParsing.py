
import os
import xml.etree.ElementTree as et

base_path = os.path.dirname(os.path.realpath(__file__))
xml_file = os.path.join(base_path, 'data.xml')
print(xml_file)

tree = et.parse(xml_file)
root = tree.getroot()

# for child in root:
#     print(child.tag, child.attrib)

# for child in raw:
#     for element in child:`
#         print(element.tag, ":", element.text)

new_elem = et.SubElement(root, "product", attrib={"id": "4"})
new_elem_name = et.SubElement(new_elem, "name")
new_elem_desc = et.SubElement(new_elem, "description")
new_elem_cost = et.SubElement(new_elem, "cost")
new_elem_ship = et.SubElement(new_elem, "shipping")

new_elem_name.text = "Python Jeans"
new_elem_desc.text = "The jeans is to cover your legs"
new_elem_cost.text = "$50.95"
new_elem_ship.text = "$4.00"

tree.write(xml_file)

for child in root:
    print(child.tag, child.attrib)
