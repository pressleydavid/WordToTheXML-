import os, fnmatch, itertools


def hyperLink(link,text):
    '''return a properly formatted hyperlink'''
    hyperlink_format = '<a href="file:///{link}">{text}</a>'
    print hyperlink_format.format(link=link, text=text)
    return hyperlink_format.format(link=link, text=text)

def find(pattern, path, TLFDict):
    splchar = '_'
    result = []
    names = []

    hrefList = []
    for root, dirs, files in os.walk(path):
        print "Root: " + str(root)
        print "Dirs: " + str(dirs)
        print "Files: " + str(files)

    for k in TLFDict:
        translate = splchar.join(k.split('.'))
        print translate
        if fnmatch.fnmatch(name, pattern):
            result.append(os.path.join(root, name))


    for item,name in itertools.izip_longest(result, files):
        hyperLink(item, name)


    # for x,y in result,files:
    #         hrefList.append()
    # print hrefList
    print result
    return result

# find('*.pdf', '/Users/David/projects/XML/output', Tdict)

# TODO: do the hyperlinking at the XML parsing level.Read the XML table title and number into

def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print "Output is: "
   print arg1
   for var in vartuple:
      print var
   return;

printinfo(50,60,'x')

