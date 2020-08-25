# Python_Spider_Study
Python爬虫全套学习流程+源码+笔记，初学者可以参考学习
# requests模块基础
* requests模块
    * urllib模块
    * requests模块

* requests模块：
    *Python中原生的一款基于网络请求的模块，功能非常强大，简单便捷，效率及高。
    * 作用：模拟浏览器请求

* 使用步骤：
    1. 指定url
        * UA伪装
        * 请求参数的处理
    2. 发起请求
    3. 获取响应数据
    4. 持久化存储

* 实战编码：
    * 需求：爬取搜狗首页的页面数据
    * 源码：01.requests第一血.py


* 实战巩固：
    * 需求：爬取搜狗指定词条对应的搜索结果页面（简易网页采集器）
        * 拓展：
            UA：User-Agent（请求载体的身份标识）
            UA检测
            UA伪装

    * 需求：破解百度翻译
        * popst请求
        * 响应数据是一组json数据

    * 需求：爬取豆瓣电影分类排行榜

    * 需求：爬取肯德基餐厅查询

    * 需求：爬取国家药品监督管理局中基于中华人名共和国化妆品生产许可证相关数据
        * 动态加载数据
        * 首页中对应企业信息数据是通过ajax动态请求到的

        * 通过对详情页url的观察发现
            * url的域名都是一样的，只有携带参数（id）不一样
            * id值可以从首页对应的ajax请求到的json串中获取
            * 域名和id值拼接出一个完整的企业详情页的url
            
# 数据解析
* 聚焦爬虫：爬取页面中指定的内容

* 数据解析分类
    * 正则
    * bs4
    * Xpath（重点）

* 数据解析原理概述
    * 解析的局部内容都会在标签之间或者标签对应的属性中找到
    * 进行指定标签的定位
    * 对标签或者标签对应的属性中的数据进行提取（解析）

* 编码流程
    1. 指定url
    2. 发起请求
    3. 获取响应数据
    4. 数据解析
    5. 持久化存储

* 正则解析：掌握正则表达式

* bs4解析：
    * 数据解析的原理
        1. 标签的定位
        2. 提取标签、标签属性中的数据值

    * bs4实现数据解析的原理：
        1. 实例化一个BeautifulSoup对象，并且将页面源码加载到该对象中
        2. 通过调用BeautifulSoup对象中为徐昂管的属性或者方法进行标签定位和数据解析

    * 环境安装：
        * pip install bs4
        * pip install lxml

    * 如何实例化BeautifulSoup对象
        * 导包：from bs4 import BeautifulSoup
        * 对象的实例化
            1. 将本地的html文档中的数据加载到该对象中
                fp = open('./爬虫/2.数据解析/test.html', 'r', encoding='utf-8')
    soup = BeautifulSoup(fp, 'lxml')
            2. 将互联网上获取的页面源码加载到该对象中
                page_text = response.text
                soup = BeautifulSoup(page_text, 'lxml')
        *  提供的用于数据解析的方法和属性：
            1. soup.tagName：返回的是文档中第一次出现的tagName对应的标签
            2. soup.find()
                soup.find('a')等同于soup.a
                soup.find('a', id='id')
            3. soup2.find_all('tagName')：返回符合要求的所有标签（列表）
            4. select: css选择器
                soup.select('某种选择器（id，class，标签...选择器）') 返回一个列表
                层级选择器：soup2.select('.tang > ul > li > a')
            5. 获取标签间的文本数据：
                soup.xxx.text/get_text()：获取某一个标签中所有的文本内容
                soup.xxx.string：获取该标签下直系文本内容
            6. 获取标签中属性值：
                soup.xxx['attribute']

* Xpath解析：最常用且最便捷高效的一种解析方式，通用性也强
    * Xpath解析原理：
        1. 实例化一个etree的对象，且需要将被解析的页面加载到该对象中
        2. 调用etree对象的xpath方法结合着xpath表达式实现标签的定位和内容的抓取
    * 环境的安装
        * pip install lxml
    * 如何实例化一个etree对象:from lxml import etree
        1. 将本地的html文档源码数据加载到etree对象中
            etree.parse(filePath)
        2. 将从互联网获取的源码数据加载到etree对象中
            etree.HTML('page_text')
        3. xpath('xpath表达式')

    * xpath表达式
        * 标签定位：
            * /：作用在最左侧表示的是从根节点开始定位；作用在标签之间表示的是一个层级
            * //：作用在最左侧表示从根节点一直定位到此节点；作用在标签之间表示的是多层级
            * 属性定位：//div[@class='xxx']、//p[id='xxx']
            * 索引定位：//div[@xxx="xxx"]/a[2]
        
        * 取内容：注意取回来的值都为列表
            * 取文本：/text()直系文本内容；//text()非直系，本身即字标签所有文本内容
            * 取属性值：/@src、/@href

* 发生中文乱码解决方案
    1. response. = 'utf-8'
    2. response.encoding = response.apparent_encoding
    3. str = str.encode('iso-8859-1').decode('gbk')
