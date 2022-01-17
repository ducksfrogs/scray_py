import lxml.html


tree = lxml.html.parse('dp.html')


tree


html = tree.getroot()


html


html.make_links_absolute('https://gihyo.jp/')


for a in html.cssselect('#listBook > li >a[itemprop="url"]'):
    url = a.get('href')
    p = a.cssselect('p[itemprop="name"]')[0]
    title = p.text_content()
    print(url,title)



