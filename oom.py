from transformers import pipeline
import gradio as gr
import logging
import numpy as np


def hello(i):
     # 尝试创建一个巨大的numpy数组
    huge_array = np.zeros(10**9, dtype=np.int64)  # 分配约10GB内存
    logging.warning(i)

    return "这是test2分支测试更新"



iface = gr.Interface(fn=hello, inputs="text", outputs="text")
iface.launch()
