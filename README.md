# spider-project

- 介绍

  爬虫的应用：批量采集数据(文本 音频 视频)、模拟用户行为 (点赞 下单)

  爬虫的原理：模拟客户端、向服务器发送网络请求



- BigPicture

  基础爬虫：基础模块(req、bs、selenium)、爬虫框架scrapy

  逆向爬虫：防护绕过、js逆向、图片验证码、滑块验证、app逆向



- 参考

  [很好的教程](https://github.com/NanmiCoder/MediaCrawler)、[很好的教程](https://github.com/Gedanke/Reptile_study_notes/blob/master/notes/Module_3/lecture_16.md)、[破反爬的很好教程](https://github.com/Kr1s77/awesome-python-login-model)、[很好的教程](https://www.qixinbo.info/2023/01/15/web-crawler-4/)、[不错的教程](https://zhuanlan.zhihu.com/p/45478178)

  https://juejin.cn/post/7226187111329398839



# 基础爬虫

## 【案例】基础大杂烩

### 文本爬虫





### 图片视频爬虫





## 基础理论

- 网站全流程

- 爬虫：用代码伪装、发送请求得到响应

  爬虫全流程：

  发送请求

  得到响应

  解析数据

- 存在反爬：校验请求头

  User-Agent、Referer、Cookie；proxy





## 抓包分析

- 抓包工具：服务器和客户端的第三方中间件

  [reqable(国内)](https://reqable.com/en-US/download)、charles、fiddler

  

- 【案例】微信公众号

  ```python
  # -*- coding: utf-8 -*-
  # @Time    : 2024/3/31 8:46
  # @Author  : yingzhu
  # @FileName: gz.py
  
  import requests
  
  
  def req_gz():
      url = "https://mp.weixin.qq.com/s?__biz=MzA5NzI1ODkzNQ==&mid=2451450218&idx=1&sn=e5c06e14960e943742f2a0d07fe327b8&chksm=86d210a4cd5e203bfeac7014673c50b35c043e8d09b4a5e5cb75ec68ac4eb691807f14f1d774&scene=126&sessionid=1711847075&subscene=227&clicktime=1711847138&enterid=1711847138&key=7ac31fc11733e01d2e99e38980d687291a52150e8da78e0697f16e5e5c7c9f592148b4a039fa842b0f088971d6d0250167bb99d52440f40e0ab4e142ffcf2723dc8e8ac30cbf196dcd19a67972ec851ef54b637e1944b2fd0ee8b6dc209806afaf6d54c02ada36eda5bc428ac6f0d1016c74923c37e34aea045b98a3077b5aef&ascene=0&uin=MzEzNjEzNzc1Ng%3D%3D&devicetype=Windows+11+x64&version=6309092b&lang=zh_CN&countrycode=CN&exportkey=n_ChQIAhIQle4ypdFFq%2FQ2Vc8anb8e2hLgAQIE97dBBAEAAAAAADWCNo8vF0wAAAAOpnltbLcz9gKNyK89dVj0K3AGERusLseH1iBfU4IJzdrVz8226on%2BeySDZZGlCfgAqH8cTchGeQuArnaZIrPjGrsCVm2JOuYijS0vuN%2F9naHBKLDoo6MBTeaVIFHoDzlx97HPlws2yneBs2ev6HeTdnEy9%2F8cXItmV%2BBjz%2B5POMKX1fIiaSHJXX8Yjy0S2FPLv5FmNNL0V%2BwSyB2%2BFkrH2CBWb8FiaTbS5uUb0Q7nqZC3lMiYdtjx2X%2B6fJUSqFjuVTsf%2Fa41YTEE&acctmode=0&pass_ticket=np4ckNMKro5lryfLhSuw6h4YS%2FAhvXKb61q%2BNkH7w%2BWOXLXnXujMi%2FTMhIV4N3C7q7GS2juoRHfxDe3etPIJDg%3D%3D&wx_header=1&fasttmpl_type=0&fasttmpl_fullversion=7139752-zh_CN-zip&fasttmpl_flag=1"
      headers = {
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309092b) XWEB/9079 Flue',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
          'cache-control': 'max-age=0',
          'x-wechat-key': '7ac31fc11733e01d2e99e38980d687291a52150e8da78e0697f16e5e5c7c9f592148b4a039fa842b0f088971d6d0250167bb99d52440f40e0ab4e142ffcf2723dc8e8ac30cbf196dcd19a67972ec851ef54b637e1944b2fd0ee8b6dc209806afaf6d54c02ada36eda5bc428ac6f0d1016c74923c37e34aea045b98a3077b5aef',
          'x-wechat-uin': 'MzEzNjEzNzc1Ng%3D%3D',
          'exportkey': 'n_ChQIAhIQle4ypdFFq%2FQ2Vc8anb8e2hLgAQIE97dBBAEAAAAAADWCNo8vF0wAAAAOpnltbLcz9gKNyK89dVj0K3AGERusLseH1iBfU4IJzdrVz8226on%2BeySDZZGlCfgAqH8cTchGeQuArnaZIrPjGrsCVm2JOuYijS0vuN%2F9naHBKLDoo6MBTeaVIFHoDzlx97HPlws2yneBs2ev6HeTdnEy9%2F8cXItmV%2BBjz%2B5POMKX1fIiaSHJXX8Yjy0S2FPLv5FmNNL0V%2BwSyB2%2BFkrH2CBWb8FiaTbS5uUb0Q7nqZC3lMiYdtjx2X%2B6fJUSqFjuVTsf%2Fa41YTEE',
          'upgrade-insecure-requests': '1',
          'sec-fetch-site': 'same-origin',
          'sec-fetch-mode': 'navigate',
          'sec-fetch-dest': 'document',
          'accept-language': 'zh-CN,zh;q=0.9',
      }
      resp = requests.get(url=url, headers=headers)
      print(resp.text)
  
  
  if __name__ == '__main__':
      print("------------------ start ------------------")
  
      req_gz()
  
      print("------------------ end ------------------")
  
  ```

  

  ```python
  # -*- coding: utf-8 -*-
  # @Time    : 2024/3/31 8:46
  # @Author  : yingzhu
  # @FileName: gz.py
  
  import requests
  from requests.adapters import HTTPAdapter
  from urllib3 import Retry
  
  
  def req_gz():
      url = "https://mp.weixin.qq.com/s?__biz=MzA5NzI1ODkzNQ==&mid=2451450218&idx=1&sn=e5c06e14960e943742f2a0d07fe327b8&chksm=86d210a4cd5e203bfeac7014673c50b35c043e8d09b4a5e5cb75ec68ac4eb691807f14f1d774&scene=126&sessionid=1711847075&subscene=227&clicktime=1711847138&enterid=1711847138&key=7ac31fc11733e01d2e99e38980d687291a52150e8da78e0697f16e5e5c7c9f592148b4a039fa842b0f088971d6d0250167bb99d52440f40e0ab4e142ffcf2723dc8e8ac30cbf196dcd19a67972ec851ef54b637e1944b2fd0ee8b6dc209806afaf6d54c02ada36eda5bc428ac6f0d1016c74923c37e34aea045b98a3077b5aef&ascene=0&uin=MzEzNjEzNzc1Ng%3D%3D&devicetype=Windows+11+x64&version=6309092b&lang=zh_CN&countrycode=CN&exportkey=n_ChQIAhIQle4ypdFFq%2FQ2Vc8anb8e2hLgAQIE97dBBAEAAAAAADWCNo8vF0wAAAAOpnltbLcz9gKNyK89dVj0K3AGERusLseH1iBfU4IJzdrVz8226on%2BeySDZZGlCfgAqH8cTchGeQuArnaZIrPjGrsCVm2JOuYijS0vuN%2F9naHBKLDoo6MBTeaVIFHoDzlx97HPlws2yneBs2ev6HeTdnEy9%2F8cXItmV%2BBjz%2B5POMKX1fIiaSHJXX8Yjy0S2FPLv5FmNNL0V%2BwSyB2%2BFkrH2CBWb8FiaTbS5uUb0Q7nqZC3lMiYdtjx2X%2B6fJUSqFjuVTsf%2Fa41YTEE&acctmode=0&pass_ticket=np4ckNMKro5lryfLhSuw6h4YS%2FAhvXKb61q%2BNkH7w%2BWOXLXnXujMi%2FTMhIV4N3C7q7GS2juoRHfxDe3etPIJDg%3D%3D&wx_header=1&fasttmpl_type=0&fasttmpl_fullversion=7139752-zh_CN-zip&fasttmpl_flag=1"
      headers = {
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309092b) XWEB/9079 Flue',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
          'cache-control': 'max-age=0',
          'x-wechat-key': '7ac31fc11733e01d2e99e38980d687291a52150e8da78e0697f16e5e5c7c9f592148b4a039fa842b0f088971d6d0250167bb99d52440f40e0ab4e142ffcf2723dc8e8ac30cbf196dcd19a67972ec851ef54b637e1944b2fd0ee8b6dc209806afaf6d54c02ada36eda5bc428ac6f0d1016c74923c37e34aea045b98a3077b5aef',
          'x-wechat-uin': 'MzEzNjEzNzc1Ng%3D%3D',
          'exportkey': 'n_ChQIAhIQle4ypdFFq%2FQ2Vc8anb8e2hLgAQIE97dBBAEAAAAAADWCNo8vF0wAAAAOpnltbLcz9gKNyK89dVj0K3AGERusLseH1iBfU4IJzdrVz8226on%2BeySDZZGlCfgAqH8cTchGeQuArnaZIrPjGrsCVm2JOuYijS0vuN%2F9naHBKLDoo6MBTeaVIFHoDzlx97HPlws2yneBs2ev6HeTdnEy9%2F8cXItmV%2BBjz%2B5POMKX1fIiaSHJXX8Yjy0S2FPLv5FmNNL0V%2BwSyB2%2BFkrH2CBWb8FiaTbS5uUb0Q7nqZC3lMiYdtjx2X%2B6fJUSqFjuVTsf%2Fa41YTEE',
          'upgrade-insecure-requests': '1',
          'sec-fetch-site': 'same-origin',
          'sec-fetch-mode': 'navigate',
          'sec-fetch-dest': 'document',
          'accept-language': 'zh-CN,zh;q=0.9',
      }
      # 设置重试策略
      retry_strategy = Retry(
          total=3,  # 总重试次数
          read=2,  # 读取重试次数
          connect=2,  # 连接重试次数
          backoff_factor=0.1  # 退避因子
      )
      adapter = HTTPAdapter(max_retries=retry_strategy)
      # 创建带有重试策略的session对象
      with requests.Session() as session:
          session.mount("https://", adapter)
          session.mount("http://", adapter)
          
          try:
              resp = session.get(url=url, headers=headers, verify=False)
              print(resp.text)
          except requests.exceptions.RequestException as e:
              print(f"请求失败: {e}")
  
  
  if __name__ == '__main__':
      print("------------------ start ------------------")
  
      req_gz()
  
      print("------------------ end ------------------")
  ```

  1







## 发送请求 requests模块





## 解析数据 bs4 xpath css re







## 异步爬虫 Thread



## 自动化工具 selenium

- Download

  https://googlechromelabs.github.io/chrome-for-testing/







# 爬虫框架 scrapy

- 定位

  scrapy：工程化

- python环境

  ```
  conda create -n forspider python=3.10
  conda activate forspider
  
  pip install scrapy
  ```

  

- [scrapy官方文档](https://docs.scrapy.org/en/latest/)

  工作流程、核心组件、项目结构
  
  ```
  tutorial/
      scrapy.cfg            # deploy configuration file
  
      tutorial/             # project's Python module, you'll import your code from here
          __init__.py
  
          items.py          # project items definition file
  
          middlewares.py    # project middlewares file
  
          pipelines.py      # project pipelines file
  
          settings.py       # project settings file
  
          spiders/          # a directory where you'll later put your spiders
              __init__.py
  ```
  
  

## ch01_tutorial

- 【案例】[谚语网站](https://quotes.toscrape.com/)

  项目环境

  ```
  scrapy startproject ch01_tutorial
  cd ch01_tutorial
  
  scrapy genspider quotes quotes.toscrape.com
  
  ```
  
  拿到html文件
  
  ```python
  from pathlib import Path
  
  import scrapy
  
  
  class QuotesSpider(scrapy.Spider):
      name = "quotes"
  
      def start_requests(self):
          urls = [
              "https://quotes.toscrape.com/page/1/",
              "https://quotes.toscrape.com/page/2/",
          ]
          for url in urls:
              yield scrapy.Request(url=url, callback=self.parse)
  
      def parse(self, response):  # 回调
          page = response.url.split("/")[-2]
          filename = f"crawl/quotes-{page}.html"
          Path(filename).write_bytes(response.body)
          self.log(f"Saved file {filename}")
          
  ```
  
  ```python
  from pathlib import Path
  
  import scrapy
  
  
  class QuotesSpider(scrapy.Spider):
      name = "quotes"
      start_urls = [
          "https://quotes.toscrape.com/page/1/",
          "https://quotes.toscrape.com/page/2/",
      ]
  
      def parse(self, response):  # 回调
          page = response.url.split("/")[-2]
          filename = f"crawl/quotes-{page}.html"
          Path(filename).write_bytes(response.body)
  
  ```
  
  ```
  mkdir crawl
  scrapy crawl quotes
  
  ```
  
  
  
- 提取数据

  scrapy shell、Selector Gadget；
  
  解析数据：re、css、xpath

  解析数据css

  ```python
  import scrapy
  
  
  class QuotesSpider(scrapy.Spider):
      name = "quotes"
      start_urls = [
          "https://quotes.toscrape.com/page/1/",
          "https://quotes.toscrape.com/page/2/",
      ]
  
      def parse(self, response):
          for quote in response.css("div.quote"):
              yield {
                  "text": quote.css("span.text::text").get(),
                  "author": quote.css("small.author::text").get(),
                  "tags": quote.css("div.tags a.tag::text").getall(),
              }
              
  ```
  
  解析数据xpath (推荐)
  
  ```python
  import scrapy
  
  
  class QuotesSpider(scrapy.Spider):
      name = "quotes"
      allowed_domains = ["quotes.toscrape.com"]
      start_urls = [
          "https://quotes.toscrape.com/page/1/",
          "https://quotes.toscrape.com/page/2/",
      ]
  
      def parse(self, response):
          for quote in response.xpath("//div[@class='quote']"):
              yield {
                  "text": quote.xpath("./span[@class='text']/text()").get(),
                  "author": quote.xpath(".//small[@class='author']/text()").get(),
                  "tags": quote.xpath("./div[@class='tags']/a[@class='tag']/text()").getall(),
              }
  
  ```
  
  ```
  scrapy crawl quotes -O crawl/quotes.json
  
  ```
  
  
  
  

## ch02_ssr

- 【案例】[Python爬虫案例 Scrape Center](https://scrape.center/)

  项目环境

  ```
  scrapy startproject ch02_ssr
  cd ch02_ssr
  scrapy genspider ssr scrape.center
  
  ```
  
  ```python
  import scrapy
  
  
  class SsrSpider(scrapy.Spider):
      name = "ssr"
      allowed_domains = ["scrape.center"]
      # start_urls = [f"https://ssr1.scrape.center"]
      start_urls = [f"https://ssr1.scrape.center/page/{i}" for i in range(1, 11)]
  
      def parse(self, response):
          for item in response.xpath("//div[@class='el-card item m-t is-hover-shadow']"):
              title = item.xpath(".//h2[@class='m-b-sm']/text()").get(),
              rank = item.xpath("//p[@class='score m-t-md m-b-n-sm']/text()").get().strip(),
              label = item.xpath(".//div[@class='categories']/button/span/text()").getall(),
              area = item.xpath("//div[@class='m-v-sm info']/span[1]/text()").get(),
              time = item.xpath("//div[@class='m-v-sm info']/span[3]/text()").get(),
              duration = item.xpath(".//div[@class='m-v-sm info'][2]/span/text()").get(),
  
              yield {
                  "title": title,
                  "rank": rank,
                  "label": label,
                  "area": area,
                  "time": time,
                  "duration": duration,
              }
  
  ```
  
  ```
  mkdir crawl
  scrapy crawl ssr -O crawl/ssr.json
  
  ```
  
  

- 定义item

  ```python
  import scrapy
  
  
  class MovieItem(scrapy.Item):
      title = scrapy.Field()
      rank = scrapy.Field()
      label = scrapy.Field()
      area = scrapy.Field()
      time = scrapy.Field()
      duration = scrapy.Field()
  
  ```

  

- 翻页

  方法1：在parse中解析新的url、回调函数

  `scrapy.Request(url, callback)`：下一页、详情页

  ```python
  import scrapy
  from scrapy import Request
  
  from ch02_ssr.items import MovieItem
  
  
  class SsrSpider(scrapy.Spider):
      name = "ssr"
      allowed_domains = ["scrape.center"]
      start_urls = ["https://ssr1.scrape.center"]
  
      def parse(self, response):
          for item in response.xpath("//div[@class='el-card item m-t is-hover-shadow']"):
              movie_item = MovieItem()
              movie_item["title"] = item.xpath(".//h2[@class='m-b-sm']/text()").get()
              movie_item["rank"] = item.xpath("//p[@class='score m-t-md m-b-n-sm']/text()").get().strip()
              movie_item["label"] = item.xpath(".//div[@class='categories']/button/span/text()").getall()
              movie_item["area"] = item.xpath("//div[@class='m-v-sm info']/span[1]/text()").get()
              movie_item["time"] = item.xpath("//div[@class='m-v-sm info']/span[3]/text()").get()
              movie_item["duration"] = item.xpath(".//div[@class='m-v-sm info'][2]/span/text()").get()
  
              yield movie_item
  
          # 提取新一页url 下一页按钮
          next_url = response.xpath("//a[@class='next']/@href").get()
          if next_url is not None:
              next_url = "https://ssr1.scrape.center" + next_url
              yield Request(next_url, callback=self.parse)  # 回调
  
  ```

  方法2：url列表 (url高度一致性)

  ```python
  import scrapy
  
  from ch02_ssr.items import MovieItem
  
  
  class SsrSpider(scrapy.Spider):
      name = "ssr"
      allowed_domains = ["scrape.center"]
      start_urls = [f"https://ssr1.scrape.center/page/{i}" for i in range(1, 11)]
  
      def parse(self, response):
          for item in response.xpath("//div[@class='el-card item m-t is-hover-shadow']"):
              movie_item = MovieItem()
              movie_item["title"] = item.xpath(".//h2[@class='m-b-sm']/text()").get()
              movie_item["rank"] = item.xpath("//p[@class='score m-t-md m-b-n-sm']/text()").get().strip()
              movie_item["label"] = item.xpath(".//div[@class='categories']/button/span/text()").getall()
              movie_item["area"] = item.xpath("//div[@class='m-v-sm info']/span[1]/text()").get()
              movie_item["time"] = item.xpath("//div[@class='m-v-sm info']/span[3]/text()").get()
              movie_item["duration"] = item.xpath(".//div[@class='m-v-sm info'][2]/span/text()").get()
  
              yield movie_item
  
  ```

  设置item有序：settings.py

  ```python
  FEED_EXPORT_FIELDS = ["title", "rank", "label", "area", "time", "duration", ]
  
  ```

  ```
  scrapy crawl ssr -O crawl/ssr.csv
  
  ```

  

- 详情页

  `scrapy.Request(meta)`：前面数据的传递

  ```python
  import scrapy
  from scrapy import Request
  
  from ch02_ssr.items import MovieItem
  
  
  class SsrSpider(scrapy.Spider):
      name = "ssr"
      allowed_domains = ["scrape.center"]
      start_urls = ["https://ssr1.scrape.center"]
  
      def parse_detail(self, response):
          movie_item = response.meta["movie_item"]
  
          movie_item["introduction"] = response.xpath("//div[@class='drama']/p/text()").get().strip()
          movie_item["director"] = response.xpath("//p[@class='name text-center m-b-none m-t-xs']/text()").get()
          movie_item["actor"] = response.xpath("//p[@class='el-tooltip name text-center m-b-none m-t-xs item']/text()").getall()
          movie_item["role"] = response.xpath("//p[@class='el-tooltip role text-center m-b-none m-t-xs item']/text()").getall()
  
          yield movie_item  # 最终返回
  
      def parse(self, response):
          for item in response.xpath("//div[@class='el-card item m-t is-hover-shadow']"):
              movie_item = MovieItem()
              movie_item["title"] = item.xpath(".//h2[@class='m-b-sm']/text()").get()
              movie_item["rank"] = item.xpath(".//p[@class='score m-t-md m-b-n-sm']/text()").get().strip()
              movie_item["label"] = item.xpath(".//div[@class='categories']/button/span/text()").getall()
              movie_item["area"] = item.xpath(".//div[@class='m-v-sm info']/span[1]/text()").get()
              movie_item["time"] = item.xpath(".//div[@class='m-v-sm info']/span[3]/text()").get()
              movie_item["duration"] = item.xpath(".//div[@class='m-v-sm info'][2]/span/text()").get()
  
              # 详情页
              detail_utl = "https://ssr1.scrape.center" + item.xpath(".//a[@class='name']/@href").get()
              yield Request(detail_utl, callback=self.parse_detail, meta={"movie_item": movie_item})  # 前面数据传递
  
          # 提取新一页url 下一页按钮
          next_url = response.xpath("//a[@class='next']/@href").get()
          if next_url is not None:
              next_url = "https://ssr1.scrape.center" + next_url
              yield Request(next_url, callback=self.parse)  # 回调
              
  ```

  ```python
  import scrapy
  
  
  class MovieItem(scrapy.Item):
      title = scrapy.Field()
      rank = scrapy.Field()
      label = scrapy.Field()
      area = scrapy.Field()
      time = scrapy.Field()
      duration = scrapy.Field()
      introduction = scrapy.Field()
      director = scrapy.Field()
      actor = scrapy.Field()
      role = scrapy.Field()
      
  ```

  ```python
  FEED_EXPORT_FIELDS = ["title", "rank", "label", "area", "time", "duration",
                        "introduction", "director", "actor", "role", ]
  
  ```

  

- 管道 (分工专业化)

  pipelines 

  ```python
  class Ch02SsrPipeline:
      def process_item(self, item, spider):
          # 去掉空格
          if item["rank"] is not None:
              item["rank"] = item["rank"].split(" ")[-1]
          # 去掉单位
          if item["time"] is not None:
              item["time"] = item["time"].split(" ")[0]
          if item["duration"] is not None:
              item["duration"] = item["duration"].split(" ")[0]
  
          # area 直接返回列表
          item["area"] = item.get("area", "").split("、")
  
          # actor 已经是列表 保留前3个
          keep_count = 3
          role_list = item.get("actor", [])
          item["actor"] = role_list if (len(role_list) < keep_count) else role_list[:keep_count]
  
          # role 同理 但还需要处理字符串
          role_list = item.get("role", [])
          cleaned_roles = []
          for rl in role_list:
              cl_rl = rl.split("饰：")[-1]
              cleaned_roles.append(cl_rl)
          item["role"] = cleaned_roles if (len(cleaned_roles) < keep_count) else cleaned_roles[:keep_count]
  
          return item
      
  ```

  settings

  ```python
  ITEM_PIPELINES = {
     "ch02_ssr.pipelines.Ch02SsrPipeline": 300,
  }
  
  ```

  



- ajax请求

  https://spa1.scrape.center/

  ```
  cd ch02_ssr
  scrapy genspider spa1 spa1.scrape.center/
  
  ```

  selenium 写在下载中间件 (不能写在spiders或download) (settings注册)

  ```python
  class SeleniumDownloaderMiddleware:
      def __init__(self):
          """初始化"""
          print("__init__")
          service = Service(r'D:\soft\tool\chrome-help\chromedriver-win64\chromedriver.exe')
          self.driver = webdriver.Chrome(service=service)
  
      def process_request(self, request, spider):
          print("process_request")
          self.driver.get(request.url)  # 打开网址
          time.sleep(3)
  
          body = self.driver.page_source
          return HtmlResponse(
              url=self.driver.current_url,
              body=body,
              encoding="utf-8",
              request=request,
          )
  
      def process_response(self, request, response, spider):
          return response
  ```

  页面结构有所改变 需要重写spider

  ```python
  import scrapy
  from scrapy import Request
  
  from ch02_ssr.items import MovieItem
  
  
  class Spa1Spider(scrapy.Spider):
      name = "spa1"
      allowed_domains = ["spa1.scrape.center"]
      start_urls = [f"https://spa1.scrape.center/page/{i}" for i in range(1, 11)]
  
      def parse_detail(self, response):
          movie_item = response.meta["movie_item"]
  
          movie_item["introduction"] = response.xpath("//div[@class='drama']/p/text()").get().strip()
          movie_item["director"] = response.xpath("//p[@class='name text-center m-b-none m-t-xs']/text()").get()
          movie_item["actor"] = response.xpath(
              "//p[@class='el-tooltip name text-center m-b-none m-t-xs item']/text()").getall()
          movie_item["role"] = response.xpath(
              "//p[@class='el-tooltip role text-center m-b-none m-t-xs item']/text()").getall()
  
          yield movie_item  # 最终返回
  
      def parse(self, response):
          for item in response.xpath("//div[@class='el-card item m-t is-hover-shadow']"):
              movie_item = MovieItem()
              movie_item["title"] = item.xpath(".//h2[@class='m-b-sm']/text()").get()
              movie_item["rank"] = item.xpath(".//p[@class='score m-t-md m-b-n-sm']/text()").get().strip()
              movie_item["label"] = item.xpath(".//div[@class='categories']/button/span/text()").getall()
              movie_item["area"] = item.xpath(".//div[@class='m-v-sm info']/span[1]/text()").get()
              movie_item["time"] = item.xpath(".//div[@class='m-v-sm info']/span[3]/text()").get()
              movie_item["duration"] = item.xpath(".//div[@class='m-v-sm info'][2]/span/text()").get()
  
              # 详情页
              detail_utl = "https://spa1.scrape.center" + item.xpath(".//div[@class='el-row']/div/a/@href").get()
              yield Request(detail_utl, callback=self.parse_detail, meta={"movie_item": movie_item})  # 前面数据传递
  
  ```

  



## 【案例】500

- 【案例】[500双色球](https://datachart.500.com/ssq/)

  创建项目

  ```
  scrapy startproject lotto_scrapy
  cd lotto_scrapy
  scrapy genspider ssq 500.com
  
  ```

  spider：返回`request`、`item`、`None`；`dic`

  - 返回`request`(往调度器仍请求)
  - 返回`item`(往管道仍数据)
  - 返回`None`；
  - 返回`dic`(不推荐)

  ```python
  import scrapy
  
  from lotto_scrapy.items import LottoScrapyItem
  
  
  class SsqSpider(scrapy.Spider):
      name = "ssq"
      allowed_domains = ["500.com"]
      start_urls = ["https://datachart.500.com/ssq/"]
  
      def parse(self, response, **kwargs):
          # print(response.text)  # 验证成功
  
          trs = response.xpath("//tbody[@id='tdata']/tr")
          for tr in trs:
              if tr.xpath("./@class").extract_first() == "tdbck": continue
  
              lotto_item = LottoScrapyItem()
              lotto_item["issue"] = tr.xpath("./td[@align='center']/text()").extract_first().strip()
              lotto_item["red_ball"] = tr.xpath("./td[@class='chartBall01']/text()").extract()
              lotto_item["blue_ball"] = tr.xpath("./td[@class='chartBall02']/text()").extract_first()
              # print(issue, red_ball, blue_ball)  # 验证成功
  
              # data = {"issue": issue, "red_ball": red_ball, "blue_ball": blue_ball}
              # yield data  # 数据传送到管道 dic
              yield lotto_item  # scrapy.item
  
  ```

  items 自定义数据模型 规范 

  ```python
  import scrapy
  
  
  class LottoScrapyItem(scrapy.Item):
      issue = scrapy.Field()
      red_ball = scrapy.Field()
      blue_ball = scrapy.Field()
  
  ```

  pipelines

  存储数据：csv、mysql、mongodb、文件存储

  ```python
  import pymysql
  import pymongo
  from lotto_scrapy.settings import MYSQL
  
  
  class LottoScrapyCsvPipeline:
      def open_spider(self, spider):
          self.file = open("crawl/ssq.csv", "w")
          self.file.write("issue,red_ball,blue_ball\n")
  
      def close_spider(self, spider):
          self.file.close()
  
      def process_item(self, item, spider):
          # 写入csv  20180801, 1_5_9_17_28_32, 12
          line = f"{item['issue']},{'_'.join(item['red_ball'])},{item['blue_ball']}\n"
          self.file.write(line)
  
          return item
  
  
  class LottoScrapyMysqlPipeline:
      def open_spider(self, spider):
          self.conn = pymysql.connect(
              host=MYSQL["host"],
              port=MYSQL["port"],
              user=MYSQL["user"],
              password=MYSQL["password"],
              db=MYSQL["db"]
          )
  
      def close_spider(self, spider):
          self.conn.close()
  
      def process_item(self, item, spider):
          try:
              cursor = self.conn.cursor()
              sql = "insert into lotto_ssq (issue, red_ball, blue_ball) values (%s, %s, %s)"
              cursor.execute(sql, (item["issue"], "_".join(item["red_ball"]), item["blue_ball"]))
              self.conn.commit()
          except:
              self.conn.rollback()
          finally:
              cursor.close()
  
          return item
  
  
  class LottoScrapyMongoDBPipeline:
      def open_spider(self, spider):
          self.client = pymongo.MongoClient(host="localhost", port=27017)
          self.collection = self.client["forspider"]["ssq"]  # db collect
  
      def close_spider(self, spider):
          self.client.close()
  
      def process_item(self, item, spider):
          self.collection.insert_one({
              "issue": item["issue"],
              "red_ball": item["red_ball"],
              "blue_ball": item["blue_ball"]
          })
          return item
  
  ```

  settings

  ```python
  ITEM_PIPELINES = {
      "lotto_scrapy.pipelines.LottoScrapyMysqlPipeline": 100,
      "lotto_scrapy.pipelines.LottoScrapyMongoDBPipeline": 200,
      "lotto_scrapy.pipelines.LottoScrapyCsvPipeline": 300,
  }
  
  # log level
  LOG_LEVEL = "WARNING"
  
  # mysql config
  MYSQL = {
      "host": "localhost",
      "port": 3306,
      "user": "root",
      "password": "123456",
      "db": "forspider",
  }
  
  ```

  mysql数据库准备

  ```sql
  create table lotto_ssq
  (
      id        int(11) primary key auto_increment,
      issue     varchar(100),
      red_ball  varchar(100),
      blue_ball varchar(100)
  );
  
  ```

  ```
  mkdir crawl 
  scrapy crawl ssq
  
  ```

  

  

## 【案例】花瓣

- 【案例】[花瓣](https://huaban.com)、[图片之家](https://www.tupianzj.com/bizhi/fengjing/) (有js混淆)

  创建项目

  ```
  scrapy startproject hb_scrapy
  cd hb_scrapy
  scrapy genspider hb huaban.com
  
  ```

  spiders

  ```python
  import re
  from urllib.parse import quote
  
  import scrapy
  from scrapy import Request
  
  from hb_scrapy.items import HbScrapyItem
  
  
  class HbSpider(scrapy.Spider):
      name = "hb"
      allowed_domains = ["huaban.com"]
      start_urls = ["https://api.huaban.com/search/file"]
  
      def parse(self, response):
          """指定关键词、指定数量"""
  
          key_word = "风景"
          limit = "40"
          page = "1"
  
          params = {
              "text": key_word,
              "sort": "all",
              "limit": limit,
              "page": page,
              "position": "search_pin",
              "fields": "pins:PIN, total, facets, split_words, relations, rec_topic_material",
          }
          url_with_params = response.urljoin('?' + '&'.join([f'{k}={v}' for k, v in params.items()]))
          yield scrapy.Request(url_with_params, callback=self.parse_json, meta={"	key_word": key_word})
  
      def parse_json(self, response, **kwargs):
          """拿到详情页url，即url_detail，后将此url封装成Request对象给调度器"""
  
          key_word = response.meta["key_word"]
          count = 0
          for item in response.json()["pins"]:
              pin_id = item["pin_id"]
              title = f"{count}_" + item.get("raw_text", "")
              title_clean = re.sub(r'[<>:"/\\|?*\s]', '_', title).strip()
              url_detail = f"https://huaban.com/pins/{pin_id}?searchWord={quote(key_word)}"
              count += 1
  
              yield Request(url=url_detail, callback=self.pares_url, meta={"title": title_clean})
  
      def pares_url(self, response, **kwargs):
          """在详情页html中由xpath解析到图片的url，后封装成Item给管道"""
  
          hb_item = HbScrapyItem()
          hb_item["title"] = response.meta["title"]
          hb_item["tp_url"] = response.xpath('//*[@id="pin_detail"]/div/div/div/div/img/@src').extract_first()
          print(hb_item["tp_url"])
          yield hb_item
          
  ```

  pipelines

  ```python
  from itemadapter import ItemAdapter
  from scrapy.pipelines.images import ImagesPipeline
  from scrapy import Request
  
  
  class HbScrapyPipeline:
      def process_item(self, item, spider):
          return item
  
  
  class HbSaveImagePipeline(ImagesPipeline):
      """继承图片下载管道"""
  
      def get_media_requests(self, item, info):
          """负责下载图片：图片url存在item中，包装Request发请求并下载"""
          return Request(item["tp_url"])
  
      def file_path(self, request, response=None, info=None, *, item=None):
          """准备文件路径"""
          file_name = request.url.split("/")[-1]
          return f"fj/{file_name}.jpg"
  
      def item_completed(self, results, item, info):
          """返回文件的详情信息"""
          print(results)
          return item
          
  ```

  settings

  ```python
  # Obey robots.txt rules
  ROBOTSTXT_OBEY = False
  
  
  # Configure item pipelines
  ITEM_PIPELINES = {
      "hb_scrapy.pipelines.HbScrapyPipeline": 300,
      "hb_scrapy.pipelines.HbSaveImagePipeline": 301,
  }
  IMAGES_STORE = "./crawl"
  
  
  DOWNLOAD_DELAY = 2  # 下载延迟
  RANDOMIZE_DOWNLOAD_DELAY = True  # 随机化下载延迟
  
  ```

  数据库准备

  ```sql
  create table hb_img (
      id int auto_increment primary key,
      title varchar(255) not null,
      img_src varchar(255) not null,
      local_path varchar(255) not null
  );
  
  ```

  

## 【案例】bilibili

- 【案例】[bilibili](https://www.bilibili.com/)

  创建项目

  

  

  1





## 【案例】二手房

- 【案例】二手房

  新建项目

  ```
  scrapy startproject lianjia_home_scrapy
  cd lianjia_home_scrapy
  scrapy genspider lianjia bj.lianjia.com
  
  ```

  

  

  1





## 【案例】纵横小说

- 【案例】[纵横小说](https://book.zongheng.com/store/c0/c0/b0/u0/p1/v9/s9/t0/u0/i1/ALL.html)

  ```
  scrapy startproject zongheng_scrapy
  cd zongheng_scrapy
  scrapy genspider zongheng zongheng.com
  
  ```

  

  

  1















## 总结







































