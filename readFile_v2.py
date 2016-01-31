from lxml import etree
import zipfile

def get_word_xml(docx_filename):
   with open(docx_filename) as f:
      zip = zipfile.ZipFile(f)
      xml_content = zip.read('word/document.xml')
   return xml_content

#create an ElementTree from a string
def get_xml_tree(xml_string):
   return etree.ElementTree(etree.fromstring(xml_string))

namespaces = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'} # add more as needed
SAP = get_xml_tree(get_word_xml('/Users/David/projects/XML/Statistical Analysis Plan - TDE-PH-310_20151223 clean.docx'))

nsText = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
# print etree.tostring(context, pretty_print=True)
tables = SAP.find('//w:tbl/w:tr/w:tc/w:p/w:r/w:t[text()="Table Title"]/../../../../..', namespaces=namespaces)
for i in tables:
    print i.tag