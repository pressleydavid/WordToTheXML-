import zipfile
from lxml import etree
import json
from searchFiles import find



# .docx files are XML underneath. zipfile gets at the directory which contains the document.xml
def get_word_xml(docx_filename):
   with open(docx_filename) as f:
      zip = zipfile.ZipFile(f)
      xml_content = zip.read('word/document.xml')
   return xml_content

# create an ElementTree from a string
def get_xml_tree(xml_string):
   return etree.ElementTree(etree.fromstring(xml_string))


# Namespace for WordML
namespaces = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}

# Open and parse the document
SAP = get_xml_tree(get_word_xml('/Users/David/projects/XML/Statistical Analysis Plan - TDE-PH-310_20151223 clean.docx'))
# uncomment and print to have a look
# print etree.tostring(SAP, pretty_print=True)

# XPath for text elements corresponding to Table Title, Listing Number and Figure Number. Returns an list of elements.
# XPath says :find Table Title, then back up the tree to the <w:tbl> element, which is the parent of all tables in the document,
#     then traverses back down the tree to the <w:tc> (table column element)
tables = SAP.xpath('//w:tbl/w:tr/w:tc/w:p/w:r/w:t[text()="Table Title"]/../../../../../w:tr/w:tc', namespaces=namespaces)
listings = SAP.xpath('//w:tbl/w:tr/w:tc/w:p/w:r/w:t[text()="Listing Number"]/../../../../../w:tr/w:tc', namespaces=namespaces)
figures = SAP.xpath('//w:tbl/w:tr/w:tc/w:p/w:r/w:t[text()="Figure Number"]/../../../../../w:tr/w:tc', namespaces=namespaces)

# Initialize Lists
T = []
L = []
F = []
# get all text, making sure to perform a join on <w:t> (text) element which have been split across <w:r> (runs)
for tr in tables:
    newList =[]
    [newList.append(t.text) for t in tr.findall('./w:p/w:r/w:t', namespaces=namespaces)]
    cat = ''.join(newList[0:])
    T.append(cat)

for tr in listings:
    newList =[]
    [newList.append(t.text) for t in tr.findall('./w:p/w:r/w:t', namespaces=namespaces)]
    cat = ''.join(newList[0:])
    L.append(cat)

for tr in figures:
    newList =[]
    [newList.append(t.text) for t in tr.findall('./w:p/w:r/w:t', namespaces=namespaces)]
    cat = ''.join(newList[0:])
    F.append(cat)

# put lists into dictionaries to further create JSON output (and text file)
Tdict = dict(T[i:i+2] for i in range(0, len(T), 2))
print Tdict
find('*.pdf', '/Users/David/projects/XML/output', Tdict)
print json.dumps(Tdict, sort_keys=True, indent=4, separators=(',', ': '))
Ldict = dict(L[i:i+2] for i in range(2, len(L), 2))
print Ldict
print json.dumps(Ldict, sort_keys=True, indent=4, separators=(',', ': '))
Fdict = dict(F[i:i+2] for i in range(2, len(F), 2))
print Fdict
print json.dumps(Fdict, sort_keys=True, indent=4, separators=(',', ': '))

#  create tab separated output files, ensuring that encoding is used for expected results
outfile = open('Tables', 'w' )
for key, value in sorted(Tdict.items()):
    outfile.write(str(key) + '\t' + str(value.encode('utf-8')) + '\n' )

outfile = open('Listings', 'w' )
for key, value in sorted(Ldict.items()):
    outfile.write(str(key) + '\t' + str(value.encode('utf-8')) + '\n' )

outfile = open('Figures', 'w' )
for key, value in sorted(Fdict.items()):
    outfile.write(str(key) + '\t' + str(value.encode('utf-8')) + '\n' )


