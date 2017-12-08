# query
This is a simple, yet powerful command line translator with baidu translate
命令行下翻译工具，翻译服务基于百度翻译

## install 安装
pip install query

## Usage 用法

### English To Chinese（英文翻译中文）
```
query apple
 ***************************** 
 *apple:苹果
 ***************************** 

```

### Chinese To English（中文翻译英文）

```
 query -t en 苹果
 ***************************** 
 *苹果:Apple
 ***************************** 
```

> 目标翻译语言支持英语、日语、德语等几十种语言，用 -t 指定翻译目标语言即可

### Chinese To Japan（中文翻译日文）
```
query -t jp 我是谁
 ***************************** 
 *我是谁:私は誰ですか
 ***************************** 

```

## query 作为一个模块导入
>默认翻译为中文,第二个参数为翻译目标语言

```
>>> from query import Query
>>> q = Query('apple')
>>> q.translate()
apple:苹果
{'src_result': 'apple', 'trans_result': '苹果'}
>>> q = Query('english', 'wyw')
>>> q.translate()
english:英吉利语
{'src_result': 'english', 'trans_result': '英吉利语'}
```