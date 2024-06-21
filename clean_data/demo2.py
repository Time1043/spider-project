import re

"""
读取输入文件 将其中的每行都读取出来存储在列表lines中 (清洗后的数据全部存放在cleaned_lines中)
然后清洗数据 去除形如 "12分33秒 | 37290人学过" 的内容
在lines的元素，如果是以“第”开头，如“第11章 导读”，则去除“第11章”字，并在这个元素的开头加上“## ”，表示这是二级标题。
在lines的元素，如果是以数字加竖线开头，如“65｜希腊化”，则去除该内容“65｜”，且在这个元素的开头加上“### ”，表示这是三级标题。
在lines的元素，如果只是“\n”，没有实际内容的，则跳过。
在lines的元素，如果不是以上情况，则在这个元素的开头加上“### ”，表示这是三级标题。
最后将cleaned_lines中的元素写入到新的文本文件中，每行之间用两个换行符隔开。
"""


def clean_data_wj_wm(input_file_path, output_file_path):
    # 读取输入文件 将其中的每行都读取出来存储在列表lines中 (清洗后的数据全部存放在cleaned_lines中)
    with open(input_file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    print(lines)

    cleaned_lines = []
    for line in lines:
        # 然后清洗数据 去除形如 "12分33秒 | 37290人学过" 的内容
        if "人学过" in line:
            continue

        # 在lines的元素，如果包含形如“讲)”，则在这个元素的开头加上“## ”，表示这是二级标题。
        if "讲)" in line:
            new_line = "## " + line
            cleaned_lines.append(new_line)

        # 在lines的元素，如果是以数字加竖线开头，如“65｜希腊化”，则去除该内容“65｜”，且在这个元素的开头加上“### ”，表示这是三级标题。
        if re.match(r"\d+｜", line):
            pattern = r"\d+｜"
            new_line = re.sub(pattern, "", line)
            new_line = "### " + new_line
            cleaned_lines.append(new_line)
            continue

        # 在lines的元素，如果只是“\n”，没有实际内容的，则跳过。
        if line == "\n":
            continue

        # 在lines的元素，如果不是以上情况，则在这个元素的开头加上“### ”，表示这是三级标题。
        new_line = "### " + line
        cleaned_lines.append(new_line)

    # 最后将cleaned_lines中的元素写入到新的文本文件中，每行之间用两个换行符隔开。
    print(cleaned_lines)
    with open(output_file_path, 'w', encoding='utf-8') as f:
        f.write('\n\n\n'.join(cleaned_lines))


# 使用函数
input_file = 'crawl/1.txt'
output_file = 'crawl/output1.txt'
clean_data_wj_wm(input_file, output_file)
