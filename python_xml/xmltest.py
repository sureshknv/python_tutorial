#import xml.etree.ElementTree as ET
#from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from xml.dom import minidom
import xml.etree.ElementTree as ET
def prettify(elem):
        """Return a pretty-printed XML string for the Element.
        """
        rough_string = ET.tostring(elem, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="  ")
#from ElementTree_pretty import prettify
root=ET.Element("root")
doc=ET.SubElement(root,"doc")
ET.SubElement(doc, "field1",name="blah").text="some value1"
ET.SubElement(doc,"field2",name="hey").text="some value 2"
tree = ET.ElementTree(root)
#tree.write("/home/suresh/Desktop/file.xml")
print prettify(root)
