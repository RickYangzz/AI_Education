## Gemini 开放平台
文档
https://ai.google.dev/tutorials/python_quickstart

studio平台
https://makersuite.google.com/app/prompts/1RvrdqMK-blmUWuRoqhqkFENTTz81Dl7s

api_key地址
https://console.cloud.google.com/apis/credentials?cloudshell=false&project=gen-lang-client-0756748615

Bard地址
https://bard.google.com/chat/077a321528eb0546

vpn能力视频：
https://www.youtube.com/watch?v=Ofkh9D3xI6o 

## tips
顺利调用Gemini的api，其中需要注意的是，需要一个好的VPN，以及地址需要选在美国。
503的问题：可以通过添加一个参数搞定。

## 创建虚拟环境
- python3 -m venv .venv
- source .venv/bin/activate 
- pip install -U pip
- pip install -q -U google-generativeai
- pip install python-dotenv

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


