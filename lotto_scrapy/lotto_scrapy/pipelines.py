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
