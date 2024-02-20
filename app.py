from transformers import pipeline
import gradio as gr
import logging

def hello(i):
    logging.warning('这是test2分支1')
    logging.warning('这是test2分支2')
    logging.warning('这是test2分支3')
    logging.warning('这是test2分支4')
    logging.warning('这是test2分支5')
    logging.warning('这是test2分支6')
    logging.warning('这是test2分支7')
    logging.warning('这是test2分支8')
    logging.warning('这是test2分支9')
    logging.warning('这是test2分支10')
    logging.warning('这是test2分支11')
    logging.warning('这是test2分支12')
    logging.warning('这是test2分支13')
    logging.warning('这是test2分支14')
    logging.warning('这是test2分支15')
    logging.warning('这是test2分支16')

    return "这是test2分支测试更新"



iface = gr.Interface(fn=hello, inputs="text", outputs="text")
iface.launch()
