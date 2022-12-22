# transfer-notes-onenote2md

一直在Onenote里面记日记和笔记，现在想要迁移到其他Markdown笔记管理软件如Obsidian。

## 使用方法

1. 将Onenote分区导出为docx文件，存放在`old_docx_notes`文件夹中。
2. 运行`transfer_notes_docx2md.py`，会先利用`docx2txt`库将docx文件转换为临时md文件，然后完成临时md文件的格式化，新的md文件会存放在`new_md_notes`文件夹中。
3. 但实践发现步骤2，利用`docx2txt`库会丢失docx文件中的超链接信息。手动复制docx内容到md文件可以保留超链接信息，将手动复制得到的md文件存放在`old_md_notes`文件夹，然后运行`transfer_notes_md2md.py`，新的md文件会存放在`new_md_notes`文件夹中。
4. 可以选择继续分割得到的新md文件，会按照一级标题创建文件夹，每个二级标题及其内容会以单独md文件保存在对应的一级标题文件夹中。

## 格式化md文件

Onenote导出的docx文件里面不包含标题样式，运行脚本会利用`format_md`函数完成格式化，转换后每年的日记为一个md文件，月份为一级标题，日期为二级标题。

- 匹配“1月”，“1.1”等日期文本，格式化为md一二级标题

- 删除Onenote页面创建日期和时间戳

- 优化空行和换行等格式

  ![IMG_202211192232053](https://img-1313032483.cos.ap-beijing.myqcloud.com/202211192232053.webp)

## 主要函数

- docx2md：提取docx文件中的文本并储存为md文件
- format_md：将提取的文本内容按照一定要求格式化，如设置一二级标题等等
- split_md：分割每年的日记，每月一个文件夹，每天的日记单独一个md文件
