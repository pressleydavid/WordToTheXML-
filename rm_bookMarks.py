from lxml import etree

#combine runs from a bookmark element split
namespaces = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'} # add more as needed
sumtab= etree.parse('/Users/David/projects/python/toc/SummaryTablesExcerpt.xml')

# def rmBookmark_combineRuns(elementTree):
tabletext = []
for bmSt in sumtab.findall(".//w:tbl/w:tr/w:tc/w:p/w:bookmarkStart", namespaces=namespaces):
    # print 'Now removing bookmark: ' + str(bmSt)
    # x = bmSt.getnext()
    # print x
    # print bmSt.getparent()
    bmParent = bmSt.getparent()
    prev = bmSt.getprevious()
    # print bmSt.getprevious().getchildren()
    prevchild = bmSt.getprevious().getchildren()
    tabletext.append(prevchild[0].text)
    bmSt.getparent().remove(bmSt)
    prev.getparent().remove(prev)
    # print etree.tostring(bmParent,pretty_print=True)



for bmEnd in sumtab.findall(".//w:tbl/w:tr/w:tc/w:p/w:bookmarkEnd", namespaces=namespaces):
    next = bmEnd.getnext()
    # print next.tag
    # print next
    nextchild = bmEnd.getnext().getchildren()
    tabletext.append(nextchild[0].text)
    bmEnd.getparent().remove(bmEnd)
    next.getparent().remove(next)


# print etree.tostring(bmParent,pretty_print=True)

# print etree.tostring(r,pretty_print=True)
# print etree.tostring(bmParent,pretty_print=True,inclusive_ns_prefixes=True)
#write the tree out to file for safe keeping and easy reference

# bookMark =  sumtab.findall(".//w:tbl/w:tr/w:tc/w:p", namespaces=namespaces)
# bookMarkParent = bookMark[0].getparent()
# print etree.tostring(bookMarkParent, pretty_print=True)
# bookMarkPrevious = bookMark[0].getprevious()
# print etree.tostring(bookMarkPrevious, pretty_print=True)
#
# table = bmParent.findall("./w:r/w:t", namespaces=namespaces)


# for elm in table:
#     print elm.findtext("./w:r/w:t", namespaces=namespaces)
# for i in table:
#     tabletext.append(i.text)
# print tabletext

txt = ''.join(tabletext)
# print txt
w = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
r = etree.SubElement(bmParent,"{" + w + "}" + "r", nsmap=namespaces)

SubE = etree.SubElement(r, "{" + w + "}" + "t", nsmap=namespaces)
SubE.text = ''.join(tabletext)

# print etree.tostring(bmParent, pretty_print=True)

# for elm in bmParent.findall("./w:r/w:t", namespaces=namespaces):
#     elm.remove(elm)

# print etree.tostring(sumtab, pretty_print=True, inclusive_ns_prefixes="w")
sumtab.write("/Users/David/Library/Mobile Documents/com~apple~CloudDocs/projects/XML/parsedTables.xml", pretty_print=True)
