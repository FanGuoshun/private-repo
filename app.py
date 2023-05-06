from transformers import pipeline
import gradio as gr
import logging

def hello(i):
    logging.warning('这是test3分支')
    return "这是test3分支测试更新"



iface = gr.Interface(fn=hello, inputs="text", outputs="text")
iface.launch()
