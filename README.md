# transfer-notes-onenote2md

一直在Onenote里面记日记，现在想要迁移到其他Markdown笔记管理软件。

## 步骤

1. 每年的日记为一个Onenote分区，可以分别导出为docx文件，存放在docx_notes文件夹下。

2. Onenote导出的docx文件里面不包含标题样式，运行脚本完成以下格式转换，新的md文件会存放在new_md_notes文件夹下。

   - 匹配“X月”“X.X”等文本分别设置为一二级标题

   - 去掉Onenote页面创建日期和时间戳

   - 优化空行换行等格式

     ![IMG_202211192232053](https://img-1313032483.cos.ap-beijing.myqcloud.com/202211192232053.webp)

3. 转换后每年的日记为一个md文件，月份为一级标题，日期为二级标题。为了方便管理，继续分割每年的日记md文件，将每天的日记单独保存为一个md文件，按照月份存在对应的文件夹中。

## 主要函数

- word2tmp_md：提取docx文件中的文本并储存为md文件
- tmp_md2new_md：将提取的文本内容格式化，设置一二级标题等等
- split_md：分割每年的日记，每月一个文件夹，每天的日记单独一个md文件
