from lxml import etree

namespaces = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'} # add more as needed

doc = etree.parse('MSDN example.xml')
sumtab= etree.parse('/Users/David/projects/python/toc/SummaryTablesExcerpt.xml')
# noNS = etree.parse('/Users/David/Library/Mobile Documents/com~apple~CloudDocs/projects/XML/SummaryTable_small_noNS')
elementList = sumtab.findall(".//w:tbl/w:tr/w:tc/w:p/w:r/w:t", namespaces=namespaces)
print elementList

tableIndex = 0
for elm in elementList:
    if elm.text == 'Table Number':
        print elementList.index(elm)
        print elm.text



    # print etree.tostring(sumtab,pretty_print=True )
# def removeBookmark():

for bad in sumtab.findall(".//w:tbl/w:tr/w:tc/w:p/w:bookmarkStart", namespaces=namespaces):
    print 'Now removing bookmark: ' + str(bad)
    x = bad.getnext()
    print x
    print bad.getparent()
    bad.getparent().remove(bad)


bookMark = sumtab.findall(".//w:tbl/w:tr/w:tc/w:p/w:bookmarkEnd", namespaces=namespaces)
bookMarkParent = bookMark[0].getparent()
print etree.tostring(bookMarkParent, pretty_print=True)
bookMarkPrevious = bookMark[0].getprevious()
print etree.tostring(bookMarkPrevious, pretty_print=True)

table = bookMarkParent.findall("./w:r/w:t", namespaces=namespaces)
tabletext = []

for elm in table:
    print elm.findtext("./w:r/w:t", namespaces=namespaces)
for i in table:
    tabletext.append(i.text)
print tabletext

txt = ''.join(tabletext)
print txt

bookMarkPrevious = bookMark[0].getprevious()
print etree.tostring(bookMarkPrevious, pretty_print=True)



# bookMark.remove(bookMarkPrevious)
# print etree.tostring(bookMark, pretty_print=True)
# E = etree.TreeBuilder("t", )

#use subelement here https://docs.python.org/2/library/xml.etree.elementtree.html#xml.etree.ElementTree.SubElement
ElementX = etree.Element("t", nsmap=namespaces)
ElementX.text = txt
print ElementX.text

SubE = etree.SubElement(bookMarkParent, "t", nsmap=namespaces)
SubE.text = txt
print etree.tostring(SubE, pretty_print=True)
print etree.tostring(bookMarkParent, pretty_print=True)

prev = SubE.getprevious().getprevious()
print prev.tag
bookMarkParent.remove(prev)
print prev.text
print etree.tostring(bookMarkParent, pretty_print=True)


    # return ElementX




# for bad in sumtab.findall(".//w:tbl/w:tr/w:tc/w:p/w:bookmarkEnd", namespaces=namespaces):
#     print 'Now removing bookmark: ' + str(bad)
#     bad.getparent().remove(bad)
#     print etree.tostring(sumtab,pretty_print=True)

# for elt in sumtab.getiterator(tag=W+'pStyle'):
#     # print elt.findall(".//[@val='TableHeadingRow']", W)
#     # if elt.attrib == 'TableHeadingRow':
#         print sumtab.getiterator(tag=W+'r')
#         print elt.tag
#         print elt.attrib
#         print elt.text

