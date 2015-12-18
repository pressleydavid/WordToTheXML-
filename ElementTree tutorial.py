__author__ = 'David'

from lxml import etree
from io import BytesIO, StringIO

root = etree.XML('<?xml version="1.0"?> <!DOCTYPE root SYSTEM "test" [ <!ENTITY tasty "parsnips"> ]> <root> <a>&tasty;</a> </root>')
tree = etree.ElementTree(root)
print etree.tostring(tree, pretty_print=True)

some_xml_data = "<root>data</root>"
root = etree.fromstring(some_xml_data)
print etree.tostring(root,pretty_print=True)

# file = BytesIO("/Users/David/projects/python/toc/SAPv2.docx")

# root = etree.fromstring(file)

parser = etree.XMLParser(remove_blank_text=True)
root = etree.XML("<root>  <a/>   <b>  </b>     </root>", parser)
print etree.tostring(root, pretty_print=True)

class DataSource:
    data = [ b"<roo", b"t><", b"a/", b"><", b"/root>" ]
    def read(self, requested_size):
        try:
            return self.data.pop(0)
        except IndexError:
            return b''
tree = etree.parse(DataSource())
etree.tostring(tree, pretty_print=True)

parser = etree.XMLParser()
parser.feed("<roo")
parser.feed("t><")
parser.feed("a/")
parser.feed("><")
parser.feed("/root>")
root = parser.close()

print etree.tostring(root)

some_file_like = BytesIO("<root><a>data</a></root>")

for event,element in etree.iterparse(some_file_like):
    print "%s, %8s, %s" % (event, element.tag, element.text)

xml_file = etree.XML("<root><a><b>ABC</b><c>abc</c></a><a><b>MORE DATA</b><c>more data</c></a><a><b>XYZ</b><c>xyz</c></a></root>")
print etree.tostring(xml_file, pretty_print=True)


parser = etree.XMLPullParser(tag="element")
parser.feed('<root><element key="value">text</element>')
parser.feed('<element><child /></element>')
parser.feed('<empty-element xmlns="http://testns/" /></root>')
