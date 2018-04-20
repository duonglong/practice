import xml.etree.ElementTree
e = xml.etree.ElementTree.parse('sap.xml').getroot()
for atype in e.findall('xsd'):
    print atype