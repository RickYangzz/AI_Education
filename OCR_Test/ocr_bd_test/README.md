## 创建虚拟环境
- python3 -m venv .venv
- source .venv/bin/activate 
- pip install requests
- pip install python-dotenv
- pip install -U pip
- pip freeze > requirements.txt

## 从git下载下来，启动虚拟环境
- pip install -U pip
- pip install -r requirements.txt
- source .venv/bin/activate

## 关闭虚拟环境
- deactivate

## .env文件内容
- 需要根据api的调用方提供的秘钥进行创建
- 或者询问原作者

## 百度AI测试结果
### 官方文档
https://ai.baidu.com/ai-doc/OCR/hk3h7y2qq

### 主要问题：
1. 返回内容无法识别，哪部分是人写的，哪部分是印刷体。
2. 用户写在一行的内容，有时候会被拆分到两行。因为行与行是使用高度标记的。

### 次要问题：
2. 有些用户写的很小的字，会识别丢失。例如："the" -> "th"
3. 某些单词部分，学生用橡皮擦掉了，但也被识别了出来。例如："do" -> "does"