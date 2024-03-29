# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ZonghengScrapyPipeline:
    def process_item(self, item, spider):
        if item['novel_Name'] is not None:
            item['novel_Name'] = item['novel_Name'].strip()

        if item['novel_State'] is not None:
            item['novel_State'] = item['novel_State'].strip()

        if item['novel_Lastupdate'] is not None:
            item['novel_Lastupdate'] = item['novel_Lastupdate'].replace('更新时间', '').strip()

        if item['novel_Synopsis'] is not None:
            item['novel_Synopsis'] = item['novel_Synopsis'].replace('\n', ' ').strip()
        return item
