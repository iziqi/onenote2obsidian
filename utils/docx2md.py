# useful functions

import re, os, shutil, docx2txt

def clear_folder(folder):
    '''
    if 'folder' exists, clear it
    if 'folder' not exists, create it
    '''
    shutil.rmtree(folder, ignore_errors=True) # 清空目标文件夹，包括文件夹本身
    if not os.path.exists(folder): 
        os.makedirs(folder)


def docx2md(docx_note, md_note, new_notes_folder):
    '''
    extract text from word file and
    save images in ./new_note_folder/img_folder
    '''
    img_folder = os.path.join(new_notes_folder, 'img_folder')
    if not os.path.exists(img_folder): 
        os.makedirs(img_folder)
    text = docx2txt.process(docx_note, img_folder)
    with open(md_note,'a',encoding='utf-8') as f:
        f.write(text)
    return md_note


def format_md(old_note, new_note):
    '''
    transfer text from old_md to new_md and
    format the text with following rules:
        1月 → # 1月\n\n
        1.1 → ## 1.1\n\n
        正文 → 正文\n\n
        2021年1月1日 → delete
        23:10 → delete
        空行 → delete
    '''

    with open(old_note,'r',encoding='utf-8') as f:
        text = f.readlines()

    # 正则表达式
    p1 = re.compile(r'^\s*\w*月\s*$') # XX月 → # XX月\n\n
    p2 = re.compile(r'^\s*\d{1,2}\.\d{1,2}\s*$') # 1.1 → ## 1.1\n\n
    p3 = re.compile(r'[\u4E00-\u9FA5\w]+') # 正文 → 正文\n\n # 这个也会匹配2021年1月1日，p4要在p3前面
    p4 = re.compile(r'^\d{4}年\d{1,2}月\d{1,2}日$') # 2021年1月1日 → delete
    p5 = re.compile(r'^\d{1,2}:\d{1,2}$') # 23:10 → delete
    p6 = re.compile(r'.', re.DOTALL) # 空行 → delete

    new_text = ''
    for line in text: 
        if p4.search(line) or p5.search(line):
            line = ''
        elif p1.search(line):
            line = '# ' + line.strip() + '\n\n' #需要两个换行符
        elif p2.search(line):
            line = '## ' + line.strip() + '\n\n'
        elif p3.search(line):
            line = line.strip() + '\n\n'
        elif p6.search(line): # 匹配换行，这个必须放最后
            line = ''
        new_text += line

    with open(new_note,'w', encoding='utf-8') as f:
        f.write(new_text)
    return new_note


def split_md(note_to_be_splited, separate_notes_folder):
    '''
    按照分级标题分割文件，一级标题为文件夹，
    每个二级标题及其内容为该文件夹下的单独md文件
    Split the given markdown file: 
    First create different folders by top-level headings
    then split markdown files by second-level headings
    '''
    
    clear_folder(separate_notes_folder)
    with open(note_to_be_splited,'r',encoding='utf-8') as f:
        count = 0
        for line in f: 
            if re.search(r'^#\s.+$', line): # 匹配一级标题：'# XXXXX'
                tmp_folder_name = line[2:].replace('\n', '') # 提取一级标题作为文件夹名
                tmp_folder_path = os.path.join(separate_notes_folder, tmp_folder_name)
                shutil.rmtree(tmp_folder_path, ignore_errors=True) # 清空目标文件夹，包括文件夹本身
                if not os.path.exists(tmp_folder_path): os.makedirs(tmp_folder_path)
            elif re.search(r'^##\s.+$', line): # 匹配二级标题：'## XXXXX'
                if count != 0: # 排除第一次经过，保存上一个二级标题下的内容
                    with open(separate_note_path,'a', encoding='utf-8') as f:
                        f.write(seperate_note_text)
                count += 1
                separate_note_name = line[3:].replace('\n', '') # 提取二级标题为md文件名
                separate_note_path = os.path.join(tmp_folder_path, separate_note_name + '.md')
                seperate_note_text = '# ' + separate_note_name + '\n' # 二级标题名称作为md开头
            elif re.search(r'.', line, re.S): # 匹配正文和换行，匹配所有内容
                if count != 0:
                    seperate_note_text += line
        if count != 0: # 处理文件结尾的最后一个二级标题
            with open(separate_note_path,'a', encoding='utf-8') as f:
                f.write(seperate_note_text)