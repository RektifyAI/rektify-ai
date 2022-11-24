from src.utils import GenCode, Config

code_gen_class = GenCode(Config.code_gen_idt, gen_kwargs={})

def test_gen_code():
    code_snippet = "def dataset_name():\n    return 'test'"
    generated_code = code_gen_class(code_snippet)
    print(generated_code)


if __name__ == "__main__":
    test_gen_code()