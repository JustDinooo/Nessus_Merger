import os
import glob
import xml.etree.ElementTree as ET

# specify the directory containing the .nessus files
dir_path = 'foo/bar'

# create a list to store the xml trees of each report
xml_trees = []

# iterate through all .nessus files in the directory
for file in glob.glob(os.path.join(dir_path, '*.nessus')):
    # parse the xml of the report
    tree = ET.parse(file)
    xml_trees.append(tree)

# create a new xml tree to merge all the other trees into
merged_tree = ET.ElementTree(ET.Element('NessusClientData_v2'))

# get the root element of the merged tree
root = merged_tree.getroot()

# iterate through the xml trees of each report
for xml_tree in xml_trees:
    # iterate through the root element's children (reports)
    for child in xml_tree.getroot():
        # append each child (report) to the root element of the merged tree
        root.append(child)
    
# write the merged tree to a new file
merged_tree.write('merged_reports.nessus', xml_declaration=True)
