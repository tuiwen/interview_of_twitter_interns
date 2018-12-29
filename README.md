# 推文实习生面试题

### 说明：

- <span style="color:red">以下题目都是编程题，上网查资料完成以下题目；程序和运行**结果截图**，发到  **hr@babelchain.org** 或者微信发给HR小姐姐。</span>

- **<span style="color:red">题目不需要全部都做，只做你擅长的编程语言对应的题目。</span>**



### JAVA

1. 写一个程序，统计一下 JDK 下面有多少个 .java 文件，多少个.xml 文件
2. Groovy是很流行的一种基于JVM的脚本语言。请在你的开发环境中安装Groovy，并启动一个 HTTPServer，我们可以用浏览器访问 http://localhost:8000/ 访问，能够返回 helloworld。

   http://groovy-lang.org/documentation.html

3. Spring IOC基础测试，从github上下载以下代码，然后按照说明一步一步完成 IOC 的测试

   https://github.com/liguobao/spring-ioc-sample


### Python

从 github 下载这个地址的代码，另存为 gen_data.py

https://gitee.com/yangbigrm/codes/ni1s50gpj2zoylvm76hcu42

安装 python 的包 XlsxWriter

运行程序

```
python gen_data.py 10
```

你可以看到输出的结果，是10条日期数据，注意日期的格式

好，现在生成10万条数据，并保存到 `data10.txt`中

```
python gen_data.py 100000 > data10.txt
```

- 问题1：

1.1 读取这个文件，按时间顺序排序

1.2 把属于 2005-2015 年的数据，存到一个excel 表格中

1.3 对于生成的表格中，**闰年闰月**的数据，高亮显示

- 问题2：

2.1 生成500万条数据，存到文件`data500.txt`，取出时间最近的1000条，存到Excel文件中，

2.2 程序运行得很慢，有没有优化的方法？



### 算法

写一个程序，计算第n个斐波那契数列。当 n 很大的时候，程序运行很慢，请仔细看下面的程序优化过程，并总结一下都做了哪些优化。是否还能在这个文章的基础上，继续优化。（查资料，总结技巧，不用编程）

https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/