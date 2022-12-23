# 之前日记记录在Onenote里面，现在想要迁移到md笔记管理软件Obsidian  
# 可以将Onenote分区导出为docx文件，再转换为md文件

# docx2md：提取docx文件中的文本并储存为md文件
# format_md：将提取的文本内容格式化，设置一二级标题等等
# links_on2ob：将Onenote内链替换为Obsidian内链
# split_md：分割每年的日记，每月一个文件夹，每天的日记单独一个md文件

import os
from utils.docx2md import docx2md,format_md, split_md, clear_folder
from utils.on2ob import links_on2ob

if __name__ == '__main__':
    '''
    批量将Onenote笔记分区导出的docx文件按照一定格式要求转换为md文件
    '''
    # 初始化notes文件夹
    old_notes_folder = os.path.join(os.getcwd(), 'old_notes') # Onenote导出的word文件放在这里
    new_notes_folder = os.path.join(os.getcwd(), 'new_notes') # 最终的md文件都在这里
    clear_folder(new_notes_folder)

    # transfer from onenote-docx to markdown
    for note in os.listdir(old_notes_folder):
        print(f'Working on file: {note}') # 显示处理进度

        note_name = os.path.splitext(note)[0]
        note_ext = os.path.splitext(note)[1]
        old_note = os.path.join(old_notes_folder, note)
        new_note = os.path.join(new_notes_folder, note_name + '.md')

        if note_ext == '.docx':
            # 提取docx文件中的文本并储存为md文件
            old_note = docx2md(old_note, new_note, new_notes_folder)

        # 将提取的文本内容格式化，设置一二级标题等等
        new_note = format_md(old_note, new_note)

        # 将Onenote内链替换为Obsidian内链
        new_note = links_on2ob(new_note)

        # 分割每年的日记，每月一个文件夹，每天的日记单独一个md文件
        separate_notes_folder = os.path.join(new_notes_folder, note_name)
        split_md(new_note, separate_notes_folder)
        
    print('Done!') # 显示处理进度