# spider-project

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
          yield scrapy.Request(url_with_params, callback=self.parse_json, meta={"key_word": key_word})
  
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





## 总结







































