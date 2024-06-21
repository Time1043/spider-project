import requests
import csv
import time

data_file = "job_data4.csv"
fields = [
    "bossName", "bossTitle", "jobName", "salaryDesc", "jobLabels",
    "jobDegree", "skills", "jobExperience", "cityName", "areaDistrict",
    "businessDistrict", "brandName", "welfareList"
]
with open(data_file, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()

"""
url = "https://www.zhipin.com/wapi/zpgeek/search/joblist.json?scene=1&query=%E5%A4%A7%E6%95%B0%E6%8D%AE&city=101230600&experience=&payType=&partTime=&degree=&industry=&scale=&stage=&position=&jobType=&salary=&multiBusinessDistrict=&multiSubway=&page=1&pageSize=30"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://www.zhipin.com/web/geek/job?query=%E5%A4%A7%E6%95%B0%E6%8D%AE&city=101230600",
    "Cookie": "lastCity=101230600; __zp_seo_uuid__=d7448d75-edd7-419a-927d-9c9ca868295c; __l=r=https%3A%2F%2Fcn.bing.com%2F&l=%2F&s=1; __g=-; wd_guid=b726aec3-62a8-4eda-b9a8-6a86cf0d4ad3; historyState=state; boss_login_mode=sms; wt2=DdVPIyfQ-GCDGIpGfdWzHDwPl7sN8fVQza5EeqmEK6jhEsapF1Dmagf815roi09HT_rZKnvfS2tWn9tpo_PsF-g~~; wbg=0; zp_at=yOOA8bLdNGK-IQzUAMosz7_VsI0gm4AEnYFh5WbOMJA~; register_unique_flag_656856751=1; __zp_stoken__=f21bfw5Fifwo4ZBQdXAppVklib2RqSVtaR8OAWcKAe8K7YsKwVcKhZ8KmUcKnY8Kff8Kywr%2FCol3DuMK6xILClsO3wpfCrMK9wp%2FCmsSNwrHCocSWw7jCvcK2ZV7CvMKvQz8UDAgGEgYeEhQIIAgLCR0fBwsJHR8HCwkdNyfCoXE3NkE4KElLUwZMWm1MWUgUV0tFNjZYcB8TNipodTZCwrrEj8ODw67CukTDkGrDjkLCuMK8OE5CRMOOVTExwrVkFMODwpUyw43DjxLDgsO%2FIMK4wqMGw5RiYUAhwrdrLEQ4w4TEu01DJDpNQU03NURBQzQ1R8OIcFcqG8ODYydELTlDN05PQUM3UE1PJzc8WidDQjRBEyAKDBQyUMK2SsK8w6RDNw%3D%3D; __c=1717638162; __a=30369362.1717638162..1717638162.7.1.7.7; geek_zp_token=V1R98hGeH73VtrVtRuzhoeKiKy7zvfzS4~"
}
"""
"""
url = "https://www.zhipin.com/wapi/zpgeek/search/joblist.json?scene=1&query=%E5%A4%A7%E6%95%B0%E6%8D%AE&city=100010000&experience=&payType=&partTime=&degree=&industry=&scale=&stage=&position=&jobType=&salary=&multiBusinessDistrict=&multiSubway=&page=1&pageSize=30"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://www.zhipin.com/web/geek/job?query=%E5%A4%A7%E6%95%B0%E6%8D%AE&city=100010000",
    "Cookie": "lastCity=101230600; __zp_seo_uuid__=d7448d75-edd7-419a-927d-9c9ca868295c; __l=r=https%3A%2F%2Fcn.bing.com%2F&l=%2F&s=1; __g=-; wd_guid=b726aec3-62a8-4eda-b9a8-6a86cf0d4ad3; historyState=state; boss_login_mode=sms; wt2=DdVPIyfQ-GCDGIpGfdWzHDwPl7sN8fVQza5EeqmEK6jhEsapF1Dmagf815roi09HT_rZKnvfS2tWn9tpo_PsF-g~~; wbg=0; zp_at=yOOA8bLdNGK-IQzUAMosz7_VsI0gm4AEnYFh5WbOMJA~; register_unique_flag_656856751=1; __c=1717638162; __a=30369362.1717638162..1717638162.7.1.7.7; __zp_stoken__=f21bfw5ITwqoeQloHHnAgc2FKVllafUpvcF3Cq1pswo3DgVXCr2HCl33DgMKxwqpWwrvCtcKJW8Kew41fdMKJwqTCnWrCiMKYwqVewonClsKVxKTEjsKqwrVswojDgsKcRCsGEhMFBhQIBRMUCh4gCgkJHSAKCQkdIAoJQT3ClnJDRDtDJ11dSRFLbltSbkcIYVFSNUJiVgwUQkB%2BwoI1NsOQw7XCuMOtw442wrZ9w402w4LDgkNNNjbCuGIyJcODWgfDhMKhKMK3wrwRwrbDqQbDg8KkEsOGXFY%2FLsODOz9DRMK2xYE6RBhQNzZOQ0M6NkQoQ3PDk29jQBrCtj0zNhdOREM8NTZEQzo3PChDO080RDYmOwgfHh4KJU%2FDgmDDgsOXREM%3D; geek_zp_token=V1R98hGeH73VtrVtRuzhoeLSu07z3RwS0~"
}
"""

for page in range(2, 11):
    url = f"https://www.zhipin.com/wapi/zpgeek/search/joblist.json?scene=1&query=%E5%A4%A7%E6%95%B0%E6%8D%AE&city=100010000&experience=&payType=&partTime=&degree=&industry=&scale=&stage=&position=&jobType=&salary=&multiBusinessDistrict=&multiSubway=&page={page}&pageSize=30"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Referer": f"https://www.zhipin.com/web/geek/job?query=%E5%A4%A7%E6%95%B0%E6%8D%AE&city=100010000&page={page}",
        "Cookie": "lastCity=101230600; __zp_seo_uuid__=d7448d75-edd7-419a-927d-9c9ca868295c; __l=r=https%3A%2F%2Fcn.bing.com%2F&l=%2F&s=1; __g=-; wd_guid=b726aec3-62a8-4eda-b9a8-6a86cf0d4ad3; historyState=state; boss_login_mode=sms; register_unique_flag_656856751=1; wt2=DNjPBPhn5PTkHgjeB5mtBxV5PIBWJvYcsw1mG9t_FlFrJqrYYetjduA93ZT49l0FxszGWi-Opk-LDAo9FqMQKjw~~; wbg=0; zp_at=k3lpTPjjQOFjTdgNYdAMXr9_8L1CHz8zn6vZJsAyWNw~; register_unique_flag_656866850=1; __zp_stoken__=f21bfw5IjTR04WggfbwpzYktVb1p%2BS3BaXcKsW2t7w4FWwq5iwqF9wrPDgcKRTMOOWsKwS8KTX8O3wqfEgUXChUXDgVXCssOEwpfCr8KWxJbEjsKpwrzCh8KTw4LCnEEsFBIUCAUGCAYSEyAeHwsKHx0fCwofHR8LCjc9wpVzRDY7RCZeS0kSSm1tUm1GB1dRUThBWFYLEUEqQkQ4NcK8QsK4asONRMK2fsOQNcK4w4JEUDVEwrhEMybCtVoIw4HCojLCt8K7FMK1w78Gw4TCoRHDlFxVIkrDhMOjIUJDw4TFgTlBFzo3NU9ENTo1QSc2w4LClMOIb1UYX8K4w4clQhU5RDVQN0FENU41Tyg1OnUnREQyORMfDAoMMk%2FCuEzDhMOkRDU%3D; __c=1717638162; __a=30369362.1717638162..1717638162.14.1.14.14; geek_zp_token=V1R98hGeL70ltqVtRuzhoeLSmz5TnQxSU~"
    }
    resp = requests.get(url=url, headers=headers)
    print(resp.json())

    resp_json = resp.json()
    jobList = resp_json["zpData"]["jobList"]
    # print(jobList)
    # print("================================================================================")
    for job in jobList:
        bossName = job["bossName"]
        bossTitle = job["bossTitle"]
        jobName = job["jobName"]
        salaryDesc = job["salaryDesc"]  # salary
        jobLabels = job["jobLabels"]
        jobDegree = job["jobDegree"]
        skills = job["skills"]  # skill
        jobExperience = job["jobExperience"]
        cityName = job["cityName"]  # city
        areaDistrict = job["areaDistrict"]
        businessDistrict = job["businessDistrict"]
        brandName = job["brandName"]  # company
        welfareList = job["welfareList"]  # welfare
        # print(bossName, bossTitle, jobName, salaryDesc, jobLabels, jobDegree, skills, jobExperience, cityName, areaDistrict, businessDistrict, brandName, welfareList)

        data = {
            "bossName": bossName,
            "bossTitle": bossTitle,
            "jobName": jobName,
            "salaryDesc": salaryDesc,
            "jobLabels": jobLabels,
            "jobDegree": jobDegree,
            "skills": skills,
            "jobExperience": jobExperience,
            "cityName": cityName,
            "areaDistrict": areaDistrict,
            "businessDistrict": businessDistrict,
            "brandName": brandName,
            "welfareList": welfareList,
        }
        with open(data_file, "a", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writerow(data)

    print("sleep 10 seconds")
    time.sleep(10)
