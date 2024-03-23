import scrapy
from scrapy import Request


class LoginSpider(scrapy.Spider):
    name = "login"
    allowed_domains = ["17k.com"]
    start_urls = ["https://user.17k.com/ck/author2/shelf?page=1&appKey=2406394919"]

    def start_requests(self):
        """子类对父类方法不满足，则重写方法"""
        # 走登录流程
        url = "https://passport.17k.com/ck/user/login"
        username = "17720900082"
        password = "H1665434994"
        form_data = {
            "loginName": username,
            "password": password,
        }
        headers = {
            'Referer': 'https://passport.17k.com/login/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
        }

        print("========================== start_requests ==========================")
        yield scrapy.FormRequest(
            url=url,
            formdata=form_data,
            headers=headers,
            callback=self.login_after_requests,
        )

    def login_after_requests(self, response):
        # 登录成功后发送请求
        print("========================== login_after_requests [Cookie] ==========================")

        # 检查响应头中的cookies
        for cookie in response.headers.getlist('Set-Cookie'):
            print("Cookie:", cookie)

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
        }

        yield Request(url=self.start_urls[0], headers=headers, callback=self.parse_data)

    def parse_data(self, response):
        print("========================== parse_data [cookie] ==========================")

        # 检查响应头中的cookies
        for cookie in response.headers.getlist('Set-Cookie'):
            print("Cookie:", cookie)

        print(response.text)


"""
========================== start_requests ==========================
2024-03-23 09:53:48 [scrapy.core.engine] DEBUG: Crawled (200) <POST https://passport.17k.com/ck/user/login> (referer: https://passport.17k.com/login/)
========================== login_after_requests [Cookie] ==========================
Cookie: b'acw_tc=276077e017111588259317990ec0dd91273a894ae7f8bc7295a8ef576bd8d6;path=/;HttpOnly;Max-Age=1800'
2024-03-23 09:53:48 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://user.17k.com/ck/author2/shelf?page=1&appKey=2406394919> (referer: https://passport.17k.com/ck/user/login)
========================== parse_data [cookie] ==========================
{"status":{"code":10103,"msg":"用户登录信息错误"},"time":1711158826000}
2024-03-23 09:53:48 [scrapy.core.engine] INFO: Closing spider (finished)
"""
