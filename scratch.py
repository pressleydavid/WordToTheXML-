from lxml import etree

namespaces = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'} # add more as needed
# sumtab= etree.parse('/Users/David/projects/python/toc/SummaryTablesExcerpt.xml')
SAP = etree.parse('/Users/David/projects/XML/Statistical Analysis Plan - TDE-PH-310_20151223 clean.xml')
# etree.tostring(SAP)
xlist = []
context = etree.iterparse('/Users/David/projects/XML/Statistical Analysis Plan - TDE-PH-310_20151223 clean.xml')
for action, elem in context:
    if elem.text == 'Table Title':
        #this gets you back up the tree to tbl
        tbl = elem.getparent().getparent().getparent().getparent().getparent()
        print tbl.tag
        nsText = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
        #and this gets you the children of tbl, which contain the <r> which contain the numbers and titles

        for i in tbl.getchildren():
            for ei in i.findall("./w:tc/w:p/w:r/w:t", namespaces=namespaces):
                print ei.tag, ei.text
            print [ei.text for ei in i.findall("./w:tc/w:p/w:r/w:t", namespaces=namespaces)]


            # if i.tag == nsText+'tr':
            #     iter_ = i.getiterator(tag=nsText+'tr')
            #     print iter_
            #     break

for x in iter_:
    print x.text, x.tag
                # print i.getchildren()[0].text, i.getchildren()[0].tag
                # print [ei.text for ei in i.findall("./w:tc/w:p/w:r/w:t", namespaces=namespaces)]
                # [[ei.text for ei in i.findall("./w:tc/w:p/w:r/w:t", namespaces=namespaces)]]
                # print i.findall("./w:tc/w:p/w:r/w:t", namespaces=namespaces)[1].text
                # print i.findall
                # SAP.findall(".//w:tbl/w:tr/w:tc/w:p/w:r/w:t", namespaces=namespaces)
            # print i
        # print tbl.getchildren()[0].text
        #
        # root = etree.ElementTree(elem)
        #
        # iter_ = root.getiterator()
        # for elem in root.iter():
        #     print elem.tag, elem.text

        # print[ el.text for el in root.getiterator()]

        # print etree.ElementTree.getchildren()
        # print etree.tostring(parsed, pretty_print=True)
        # print etree.get
        # element_root = root.getroot()
        # print root.getroot().text
        # print etree.tostring(element_root, pretty_print=True)

    # for j in i.getchildren():
    #             # print j.tag, j.text
    #             for k in j.getchildren():
    #                 # print k.tag,k.text
    #                 for l in j.getchildren():
    #                     # print l.tag,l.text
    #                     for m in l.getchildren():
    #                         print m.tag,m.text