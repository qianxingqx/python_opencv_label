### 功能
* 使用 opencv 对图像进行矩形框标注
* 因为在使用 labelmg 的过程中感觉不太方便，主要是我所使用的图像长宽比差别大，所以在 labelImg 中标记起来很费劲，而 opencv 可以自由缩放图像，更加方便一些

### 使用方法
#### 标记
* 在命令行中运行`label_main.py`程序后，用选框拖动一个矩形框
![在这里插入图片描述](https://img-blog.csdnimg.cn/929c0d6cfcf6435eb8893799f118ebea.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAcWlhbnhpbmdxeA==,size_20,color_FFFFFF,t_70,g_se,x_16)
* 会出现一个确认框，如果标注正确，点击`正确`，那么该标记框就会加入到列表中保存；如果点击`错误`，那么该标记框不会保存；如果该图片标记完成，点击`结束`，进行下一张图片的标记（请不要直接关闭图像，而是应该点击结束进行下一张图片的标记）
* 点击`正确`后，之前的蓝色矩形框会变成红色
![在这里插入图片描述](https://img-blog.csdnimg.cn/9bb69ecc866d48de90f110db29789f73.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAcWlhbnhpbmdxeA==,size_20,color_FFFFFF,t_70,g_se,x_16)
* 可以自由缩放图像比例进行标记
![在这里插入图片描述](https://img-blog.csdnimg.cn/23d88e4d6ce44e1e94cb415c8cdef7b0.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAcWlhbnhpbmdxeA==,size_18,color_FFFFFF,t_70,g_se,x_16)
* 标记完毕后，每张图片的标记都会生成一个 csv 文件
* 运行日志
```shell
C:\Users>python label_main.py
--当前标记的图片: 0
已经增加一处标记，请继续框选，标记框数量: 1
已经增加一处标记，请继续框选，标记框数量: 2
已经增加一处标记，请继续框选，标记框数量: 3
已经增加一处标记，请继续框选，标记框数量: 4
已经增加一处标记，请继续框选，标记框数量: 5
--结束当前图片标记--

--当前标记的图片: 1
已经增加一处标记，请继续框选，标记框数量: 1
--结束当前图片标记--
```
#### 读取标记框并可视化
* 运行`read_label.py`文件，可视化如图所示
![在这里插入图片描述](https://img-blog.csdnimg.cn/e30b616dfc2e4736b9aac9fb71bfe59a.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAcWlhbnhpbmdxeA==,size_20,color_FFFFFF,t_70,g_se,x_16)
#### 注意
*  该程序需最好在命令行运行，在 spyder 和 ipython 中可能会出错
* 注意结束当前标记图片在弹出的确认框中点击结束，而不是直接关掉图片
