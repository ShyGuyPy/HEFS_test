#grab HEFS xml data manually

import xml.etree.ElementTree as et
from pathlib import Path
import os

#print("running")
#test = Path('C:/Users/icprbadmin/Documents/Python_Scripts/HEFS/data/2017121112_BRKM2POT_hefs_export.xml')
#print(test)




file_string = "test.xml" #"2017121112_BRKM2POT_hefs_export.xml"
base_path = os.path.dirname(os.path.realpath(__file__))
print("This is the base_path: " + base_path)
xml_file = os.path.join(base_path, file_string)
print("This is the xml file " + xml_file)

tree = et.parse(xml_file)
root = tree.getroot()

def print_child(parent):
    for child in root:
        print(child, child.tag)

print_child(root)
#my_data = ET.parse(Path('C:/Users/icprbadmin/Documents/Python_Scripts/HEFS/data/2017121112_BRKM2POT_hefs_export.xml'))

