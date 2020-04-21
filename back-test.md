# 推文实习生面试题

### 说明：

- <span style="color:red">以下题目都是编程题，答题时间为 24 小时，你可以上网、看书、问任何你能问的人；</span>
- <span style="color:red">完成后请将程序源码 + 运行**结果截图**+ PDF 格式简历文件通过电子邮件发到 **hr@funstory.ai** 或者微信发给 HR 小姐姐。</span>

- **<span style="color:red">邮件里只有代码文件和截图，不要发生成的数据文件，excel，word，pdf 等。</span>**

- **<span style="color:red">题目不需要全部都做，使用你擅长的编程语言做你会做的题目。</span>**

### 编程问题

1.  写一个程序，统计一下 C 盘下面有多少个 .dll 文件；如果你是 Mac 或者 Linux 系统，统计一下 /usr 目录下有多少个 .so 文件.
    **注意不能使用 walkFileTree, os.walk 这类直接遍历所有目录的方法，而是要你自己实现它。**

2)  mkdate 是一个用不同语言写的（Java，C++，Bash，Python，JavaScript），生成随机日期的程序，下载 mkdate，完成下面的任务。mkdate 下载链接
    https://gitee.com/yangbigrm/interview_of_twitter_interns/tree/master/mkdate

- 2.1 编译并运行 mkdate 程序，生成 10 万条数据 `./mkdate 10 > date10.txt`（5 种语言里选你会的，注意 Java 应编译为 jar）
- 2.2 文件的每一行是一个日期，但是这些日期并不都是正确的，你需要修复这些日期。修复采取就近修复的原则；例如：`2010-2-30 6:5:13`，没有 2 月 30 日，就近修复到 `2010-3-1 6:5:13`
- 2.3 把文件中所有恰好是星期日的数据（例如 2010-1-31 是星期日），存到一个 excel 文件中。注意日期要排序。
- 2.4 生成 500 万条数据，存到文件 `./mkdate 500 > date500.txt`，取出时间离今天时间最近的 1000 条，存到 Excel 文件中。
- 2.5 5000 万条数据，程序运行得很慢，有没有优化的方法？

### 项目实战题

#### JWT 加密解析

要求如下：

- JWT（Json web token）是一种常见的应用在分布式微服务、SSO 中的鉴权机制，请使用你熟悉的编程语言完成 JWT 的生成和解析

- 需要自行实现 JWT 的生成和解析，不允许借助其他的第三方库

- 需要自行实现 JWT 的生成和解析，不允许借助其他的第三方库

- 需要自行实现 JWT 的生成和解析，不允许借助其他的第三方库

JWT 样例

```log
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```

#### OAuth 登录实践

OAuth 是常见的一种第三方授权系统，

现在我们需要基于框架自行完成搭建一套自己的 OAuth 登录系统

要求如下：

- OAuth Server 不需要自行实现，直接 [hydra server](https://www.ory.sh/hydra/docs/index)即可

- OAuth 中的用户系统需要自行实现，可以简单验证账号密码为 test/test

- 需要完成第三方 APP/Web 接入 OAuth2.0 登录，获取到对应的授权码和用户信息

AC 要求：

- 简短描述一下整个操作流程，同时提供必要相关命令信息和配置信息
- 提供用户系统源码
- 提供第三方 APP/Web 接入此 OAuth2.0 的源码

#### 安居客租房数据抓取

租房站点 [https://m.anjuke.com/sh/zf/?from=anjuke_home](https://m.anjuke.com/sh/zf/?from=anjuke_home)

- 自行完成房源数据抓取，存储到本地 json 文件

- 房源价格信息已加密，需要自行完成解密

### 算法

第 1 题 已知一个**完全二叉树**的每个节点为 Node {leftChild, rightChild, data}

```
先序遍历的结果为: A D E F G H K L B I M C
```

请写代码重建这个二叉树

<br>

第 2 题 写一个程序，计算下面数列的结果；在屏幕上打印出的要求是精确结果

$f(n) = f(n-1)+f(n-2)+f(n-3)+1$

$f(0)=f(1)=f(2)=0$

a. f(100)<br>
b. f(100,000)<br>
c. f(20,000,000)<br>
<br>
