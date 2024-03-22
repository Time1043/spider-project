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
