import pymysql
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline

from hb_scrapy.settings import MYSQL


class HbSaveImagePipeline(ImagesPipeline):
    """继承图片下载管道"""

    def get_media_requests(self, item, info):
        """负责下载图片：图片url存在item中，包装Request发请求并下载"""
        return Request(item["tp_url"])

    def file_path(self, request, response=None, info=None, *, item=None):
        """准备文件路径"""
        file_name = request.url.split("/")[-1]
        return f"spring/{file_name}.jpg"

    def item_completed(self, results, item, info):
        """返回文件的详情信息"""
        ok, file_info = results[0]
        item["local_path"] = file_info["path"]
        return item


class HbMysqlPipeline:
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
            sql = "insert into hb_img (title, img_src, local_path) values (%s, %s, %s)"
            cursor.execute(sql, (item["title"], item["tp_url"], item["local_path"]))
            self.conn.commit()
        except:
            self.conn.rollback()
        finally:
            cursor.close()

        return item
