from lxml import etree
# 实例化一个etree对象
tree = etree.parse('./爬虫/2.数据解析/test.html', etree.HTMLParser())
# r = tree.xpath('/html/body/div')
# r = tree.xpath('/html//div')
# r = tree.xpath('//div')

# r = tree.xpath('//div[@class="logo"]')

# r = tree.xpath('//div[@class="top_right"]/a[2]')

# r = tree.xpath('//div[@class="footer_first"]/a[1]//text()')
r = tree.xpath('//div[@class="product"]/a[3]/img/@src')

print(r)
