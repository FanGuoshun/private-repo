from transformers import pipeline
import gradio as gr
import logging
import numpy as np
import array

huge_array = array.array('i', [0] * (10**9))  # 分配约10GB内存

def hello(i):
    print(huge_array)
    logging.warning(i)

    return "这是test2分支测试更新"



iface = gr.Interface(fn=hello, inputs="text", outputs="text")
iface.launch()
