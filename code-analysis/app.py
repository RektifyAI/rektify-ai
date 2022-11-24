import gradio as gr
from src.utils import return_parse_tree, GenCode, Config
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



logger.info("Loading classes into the memory....")
code_gen_class = GenCode(Config.code_gen_idt, gen_kwargs=Config.code_gen_config)
logger.info("Sucessfully loaded classes into the memory")

def code_gen(code_snippet:str) -> str:
    logger.info("Starting to generate code...")
    generated_code = code_gen_class(code_snippet)
    logger.info("Sucessfully generated code")
    
    return generated_code

def code_edit(code_snippet:str = "def dataset_name():\n    return 'test'"):
    return code_snippet + "\n" + return_parse_tree(code_snippet)

demo = gr.Blocks(analytics_enabled=True)
with demo:
    gr.Markdown("""# Code Analysis \n ## Code Editor""")
    with gr.Row():
        input_editor = gr.Textbox(label="Code Editor",lines=10,interactive=True,placeholder="Use this as the main code editor ")
        button_gen = gr.Button(value="Complete Code")

    button_gen.click(code_gen,input_editor,input_editor)
    # iface = gr.Interface(title="Code Editor",fn=code_edit, inputs="text", outputs="text",examples=["def dataset_name():\n    return 'test'"])
    # iface.launch()

demo.launch(debug=True)