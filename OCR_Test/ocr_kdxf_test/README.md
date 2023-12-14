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

## 科大讯飞 OCR 测试结果
### 官方文档
https://www.xfyun.cn/doc/words/wordRecg/API.html#%E6%8E%A5%E5%8F%A3%E8%AF%B4%E6%98%8E

### 主要问题：
1. 汉语没有正确返回，并且和英文混合在了一起。
2. 返回内容无法识别，哪部分是人写的，哪部分是印刷体。

### 次要问题：
3. 存在某些单词没有识别出来，例如："books"
4. 某些单词被拆解为了两个，例如："twelve" -> "twe" + "lve"
5. 有些用户写的很小的字，会识别丢失。例如："the" -> "th"
6. 某些单词部分，学生用橡皮擦掉了，但也被识别了出来。例如："do" -> "does"