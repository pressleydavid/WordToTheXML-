from lxml import etree

#combine runs from a bookmark element split
namespaces = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'} # add more as needed
sumtab= etree.parse('/Users/David/projects/python/toc/SummaryTablesExcerpt.xml')

# def rmBookmark_combineRuns(elementTree):
tabletext = []
for bmSt in sumtab.findall(".//w:tbl/w:tr/w:tc/w:p/w:bookmarkStart", namespaces=namespaces):
    bmParent = bmSt.getparent()
    prev = bmSt.getprevious()
    prevchild = bmSt.getprevious().getchildren()
    tabletext.append(prevchild[0].text)
    bmSt.getparent().remove(bmSt)
    prev.getparent().remove(prev)



for bmEnd in sumtab.findall(".//w:tbl/w:tr/w:tc/w:p/w:bookmarkEnd", namespaces=namespaces):
    next = bmEnd.getnext()
    nextchild = bmEnd.getnext().getchildren()
    tabletext.append(nextchild[0].text)
    bmEnd.getparent().remove(bmEnd)
    next.getparent().remove(next)


txt = ''.join(tabletext)

w = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
r = etree.SubElement(bmParent,"{" + w + "}" + "r", nsmap=namespaces)

SubE = etree.SubElement(r, "{" + w + "}" + "t", nsmap=namespaces)
SubE.text = ''.join(tabletext)

sumtab.write("/Users/David/Library/Mobile Documents/com~apple~CloudDocs/projects/XML/parsedTables.xml", pretty_print=True)
