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
