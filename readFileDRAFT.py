import zipfile
from lxml import etree


#.docx files are XML underneath. zipfile gets at the directory which contains the document.xml
def get_word_xml(docx_filename):
   with open(docx_filename) as f:
      zip = zipfile.ZipFile(f)
      xml_content = zip.read('word/document.xml')
   return xml_content

#create an ElementTree from a string
def get_xml_tree(xml_string):
   return etree.ElementTree(etree.fromstring(xml_string))


# Open and parse the document
namespaces = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
nsText = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
print etree.tostring(get_xml_tree(get_word_xml('/Users/David/projects/python/toc/SAPv2.docx')), pretty_print=True)
SAP = get_xml_tree(get_word_xml('/Users/David/projects/python/toc/SAPv2.docx'))


tabletext = []
for bmSt in SAP.findall(".//w:tbl/w:tr/w:tc/w:p/w:bookmarkStart", namespaces=namespaces):
    bmParent = bmSt.getparent()
    prev = bmSt.getprevious()
    try:
        prevchild = bmSt.getprevious().getchildren()
        if prevchild[0].text != None:
            tabletext.append(prevchild[0].text)
        bmSt.getparent().remove(bmSt)
        prev.getparent().remove(prev)
    except:
        pass


for bmEnd in SAP.findall(".//w:tbl/w:tr/w:tc/w:p/w:bookmarkEnd", namespaces=namespaces):
    next = bmEnd.getnext()
    try:
        nextchild = next.getchildren()
        if nextchild[0].text != None:
            tabletext.append(nextchild[0].text)
        bmEnd.getparent().remove(bmEnd)
        next.getparent().remove(next)
    except:
        pass


txt = ''.join(tabletext)

w = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
r = etree.SubElement(bmParent,"{" + w + "}" + "r", nsmap=namespaces)

SubE = etree.SubElement(r, "{" + w + "}" + "t", nsmap=namespaces)
SubE.text = ''.join(tabletext)


SAP.write("/Users/David/Library/Mobile Documents/com~apple~CloudDocs/projects/XML/parsedSAP.xml", pretty_print=True)

elementList = SAP.findall(".//w:tbl/w:tr/w:tc/w:p/w:r/w:t", namespaces=namespaces)

tables = SAP.xpath('.//w:tbl/w:tr/w:tc/w:p/w:r/w:t[text()="Table Title"]', namespaces=namespaces)

for elm in elementList:
        if elm.text == 'Table Number':
            print elementList.index(elm)
            print elm.text
            tableList = elementList[elementList.index(elm):]
            break


tableList2 = []
for item in tableList:
    tableList2.append(item.text)


T = []
L = []
F = []
figure_index = 0
listing_index = 0
table_index = 0
for item in tableList2:
    if item == 'Figure Number':
        figure_index = tableList2.index(item)
    elif item == 'Appendix Number':
        listing_index = tableList2.index(item)
    elif item == 'Table number':
        table_index = tableList2.index(item)
F = tableList2[figure_index:]
L = tableList2[listing_index:figure_index]
T = tableList2[table_index:listing_index]


Tdict = dict(T[i:i+2] for i in range(2, len(T), 2))
Ldict = dict(L[i:i+2] for i in range(2, len(L), 2))
Fdict = dict(F[i:i+2] for i in range(2, len(F), 2))

outfile = open('Tables', 'w' )
for key, value in sorted(Tdict.items()):
    outfile.write(str(key) + '\t' + str(value.encode('utf-8')) + '\n' )

outfile = open('Listings', 'w' )
for key, value in sorted(Ldict.items()):
    outfile.write(str(key) + '\t' + str(value.encode('utf-8')) + '\n' )

outfile = open('Figures', 'w' )
for key, value in sorted(Fdict.items()):
    outfile.write(str(key) + '\t' + str(value.encode('utf-8')) + '\n' )
