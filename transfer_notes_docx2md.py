# 之前日记记录在Onenote里面，现在想要导出为md，迁移到其他笔记管理软件
# 每年的日记为一个Onenote分区，可以先导出为docx文件，再格式化为md文件

# docx2md：提取docx文件中的文本并储存为md文件
# format_md：将提取的文本内容格式化，设置一二级标题等等
# split_md：分割每年的日记，每月一个文件夹，每天的日记单独一个md文件

import os
from utils.docx2md import docx2md,format_md, split_md, create_folder

if __name__ == '__main__':
    '''
    批量将Onenote笔记分区导出的docx文件按照一定格式要求转换为md文件
    '''
    # 初始化notes文件夹
    old_docx_folder = os.path.join(os.getcwd(), 'old_docx_notes') # Onenote导出的word文件放在这里
    old_md_folder = os.path.join(os.getcwd(), 'old_md_notes')
    new_md_folder = os.path.join(os.getcwd(), 'new_md_notes') # 最终的md文件都在这里

    create_folder(new_md_folder)
    create_folder(old_md_folder)

    # transfer from onenote-docx to markdown
    for note in os.listdir(old_docx_folder):
        print(f'Working on file: {note}') # 显示处理进度

        note_name = os.path.splitext(note)[0]
        old_docx = os.path.join(old_docx_folder, note)
        old_md = os.path.join(old_md_folder, note_name + '_old.md')
        new_md = os.path.join(new_md_folder, note_name + '.md')

        # 提取docx文件中的文本并储存为md文件
        old_md = docx2md(old_docx, old_md, new_md_folder)

        # 将提取的文本内容格式化，设置一二级标题等等
        new_md = format_md(old_md, new_md)

        # 分割每年的日记，每月一个文件夹，每天的日记单独一个md文件
        separate_notes_folder = os.path.join(new_md_folder, note_name)
        create_folder(separate_notes_folder)
        split_md(new_md, separate_notes_folder)
        
    print('Done!') # 显示处理进度