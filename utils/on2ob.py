# 将字符串里面的Onenote内链替换为Obsidian内链
# from: [千钧一发](onenote:观影笔记.one#千钧一发&.........)
# to  : [[千钧一发]]

import re
from datetime import datetime

def links_on2ob(note):
    '''
    将text里面的Onenote内链替换为Obsidian内链，比如
    from: [千钧一发](onenote:观影笔记.one#千钧一发&.........)
    to  : [[千钧一发]]
    '''
    with open(note,'r',encoding='utf-8') as f:
        text = f.read()
    
    text = replace_links_on2ob(text, new_text='')

    with open(note,'w+', encoding='utf-8') as f:
        f.write(text)
    return note


def replace_links_on2ob(text, new_text):
    '''
    将text里面的Onenote内链替换为Obsidian内链，比如
    from: [千钧一发](onenote:观影笔记.one#千钧一发&.........)
    to  : [[千钧一发]]
    '''
    if not re.search(r'\[.*?\]\(onenote:.+?\)', text):
        return text
    text_part1, text_part2 = seperate_text(text)
    text_part1 = replace_first_link(text_part1)
    text_part2 = replace_links_on2ob(text_part2, new_text)
    new_text = text_part1 + text_part2
    return new_text

def seperate_text(text):
    '''
    分割字符串，返回包含第一个Onenote内链的text1，和剩下的字符串text2
    '''
    link = re.search(r'\[.*?\]\(onenote:.+?\)', text)
    text_part1 = text[: link.end()] # link前
    text_part2 = text[link.end(): ] # link后
    return text_part1, text_part2

def get_date(year, on_title):
    '''
    将原来'MM.DD'格式的日期转换为'YYYY.MM.DD ddd'格式
    '''
    month = on_title.split('.')[0]
    day = on_title.split('.')[1]
    if int(month) < 10:
        month = '0' + month
    if int(day) < 10:
        day = '0' + day
    weekday_dict = {1: '周一', 2: '周二', 3: '周三', 4: '周四', 5: '周五', 6: '周六', 7: '周日'}
    weekday = datetime.strptime(year + month + day, "%Y%m%d").isoweekday()
    weekday = weekday_dict[weekday]
    on_title = year + '.' + month + '.'+ day + ' ' + weekday
    return on_title

def replace_first_link(text):
    '''
    将text里面的第一个Onenote内链替换为Obsidian内链
    '''
    p1 = re.compile(r'\[.*?\]\(onenote:.+?\)')
    link = p1.search(text)
    text1 = text[: link.start()] # link前字符串
    text2 = text[link.start(): ] # link本身

    on_word = re.search(r'\[.+?\]', text2).group()[1:-1] # 定位原替换文字
    if re.search(r'#.+?&', text2):
        on_title = re.search(r'#.+?&', text2).group()[1:-1] # 定位原页面标题
    else:
        return text

    if re.search(r'20[12]\d{1}', text2):
        # 原链接为日记链接，包含20XX年份
        year = re.search(r'20[12]\d{1}', text2).group()
        on_title = get_date(year, on_title) # 将原来'MM.DD'格式的日期转换为'YYYY.MM.DD ddd'
    elif re.search(r'观影笔记.one|读书笔记.one', text2):
        # 原链接为观影笔记，读书笔记
        ob_link = '[[' + on_title + ']]' # 决定Obsidian里面的链接形式
        text2 = re.sub(p1, ob_link, text2) # 更新text2
        text = text1 + text2
        return text
    ob_link = on_word + '（[[' + on_title + ']]）' # 决定Obsidian里面的链接形式
    text2 = re.sub(p1, ob_link, text2) # 更新text2
    text = text1 + text2
    return text