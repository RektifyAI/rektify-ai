import ast
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from dataclasses import dataclass

# Configs
class Config:
    code_gen_idt : str = "lvwerra/codeparrot-small"
    code_gen_config : dict = {
        "max_length" : 256
    }

class GenCode:
    def __init__(self,model_idt:str,gen_kwargs:dict) -> None:
        self.generation_pipe = pipeline("text-generation", model=model_idt)
        self.gen_kwargs = gen_kwargs
    def __call__(self, input : str):
        return self.generation_pipe(input, **self.gen_kwargs)[0]["generated_text"]
        


def return_lexer_map(code_snippet:str):
    return None


def return_parse_tree(code_snippet:str):
    return ast.dump(ast.parse(code_snippet))