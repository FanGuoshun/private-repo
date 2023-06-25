import gradio as gr
import logging
import requests
import os


def hello(i):
    logging.warning('这是test3分支')
    url = "https://huggingface.co"
    response = requests.get(url)
    print(str(os.environ.get("http_proxy")))
    print(str(os.environ.get("https_proxy")))
    print(str(os.environ.get("no_proxy")))
    print(str(os.environ.get("PATH")))
    print("Request:")
    print(response.request.headers)
    print("\nResponse:")
    print(response.status_code)
    print(response.headers)
    return "这是test3分支测试更新11111111111"


iface = gr.Interface(fn=hello, inputs="text", outputs="text")
iface.launch()
