import zipfile
from lxml import etree

#.docx files are XML underneath. zipfile gets at the directory which contains the document.xml
def get_word_xml(docx_filename):
   with open(docx_filename) as f:
      zip = zipfile.ZipFile(f)
      xml_content = zip.read('word/document.xml')
   return xml_content

#create an etree from a string
def get_xml_tree(xml_string):
   return etree.fromstring(xml_string)

#Example from SO:
# http://stackoverflow.com/questions/4210730/how-do-i-use-xml-namespaces-with-find-findall-in-lxml


# Open and parse the document
namespaces = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
nsText = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
print etree.tostring(get_xml_tree(get_word_xml('/Users/David/projects/python/toc/SAPv2.docx')), pretty_print=True)
SAP = get_xml_tree(get_word_xml('/Users/David/projects/python/toc/SAPv2.docx'))

elementList = SAP.findall(".//w:tbl/w:tr/w:tc/w:p/w:r/w:t", namespaces=namespaces)
# print elementList
for elm in elementList:
    if elm.text == 'Table Number':
        print elementList.index(elm)
        print elm.text
        tableList = elementList[elementList.index(elm):]

for i in tableList:
    print i.text
#now read the rest of the table into another XML structure
count = 0
for i in elementList:
    print i.text

# print etree.tostring(SAP,pretty_print=True )
# zf = zipfile.ZipFile('SAP.docx')
# tree = etree.parse(zf.open('word/document.xml'))




# try to use this to create the tree from docx file, in _init_ method
from xml.etree import ElementTree

with open('/Users/David/projects/python/toc/SummaryTablesExcerpt.xml', 'rt') as f:
    tree = ElementTree.parse(f)

print tree

for node in tree.iter():
    print node.tag, node.text

for node in tree.iter():
    if node.tag == nsText+'bookmarkStart':
        tree.remove(nsText+'bookmarkStart')
#         remove bookmarkStart
#         get next element and verify it is bookmarkEnd. Delete that bitch.
#           get previous element and combine with next element of same tag
#   return ElementTree (or do you modify the tree in place and simply return the original tree as an object?)

# from xml.etree import ElementTree
#
# with open('podcasts.opml', 'rt') as f:
#     tree = ElementTree.parse(f)
#
# for node in tree.iter():
#     print node.tag, node.attrib