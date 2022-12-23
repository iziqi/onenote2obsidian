# transfer-notes-onenote2obsidian

一直在Onenote里面记笔记，现在想要迁移到[Obsidian](https://obsidian.md/)，一个md笔记管理软件。

## 使用方法

1. 将Onenote分区导出为docx文件，存放在`old_notes`文件夹中。

2. 运行`transfer_notes_main.py`，会先利用`docx2txt`库将docx文件转换为md文件，然后利用`format_md`函格式化md文件，最终新的md文件会存放在`new_notes`文件夹中。

3. 但实践发现步骤2，利用`docx2txt`库会丢失docx文件中的超链接信息。手动复制docx内容到md文件可以保留超链接信息，将手动复制得到的md文件存放在`old_notes`文件夹，然后运行`transfer_notes_main.py`，新的md文件会存放在`new_notes`文件夹中。

4. 可以使用`links_on2ob`函数将文件中的Onenote内链替换为Obsidian内链：

   Onenote内链格式: 今天看了\[一部电影](onenote:笔记.one#千钧一发&.........)

   Obsidian内链格式: 今天看了一部电影（[[千钧一发]]）

5. 可以使用`split_md`函数分割md文件，会先按照一级标题创建文件夹，每个二级标题及其内容会以单独md文件保存在对应的一级标题文件夹中。

## 格式化md文件

Onenote导出的docx文件里面不包含标题样式，运行脚本会利用`format_md`函数完成格式化，转换后月份为一级标题，日期为二级标题。

- 匹配“1月”，“1.1”等日期文本，格式化为md一二级标题

- 删除Onenote页面的创建日期和创建时间戳

- 优化空行和换行等

  ![IMG_202211192232053](https://img-1313032483.cos.ap-beijing.myqcloud.com/202211192232053.webp)
