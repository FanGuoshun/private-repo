from transformers import pipeline
import gradio as gr
import logging

def hello(i):
    classifier = pipeline("sentiment-analysis")
    a = classifier(i)
    logging.warning('文本分类结束')
    asdadsasadsa
    return a


iface = gr.Interface(fn=hello, inputs="text", outputs="text")
iface.launch()
