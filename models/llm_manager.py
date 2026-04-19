from langchain_openai import ChatOpenAI
from config.settings import Settings


class LLMManager:
    def __init__(self):
        self.llm = ChatOpenAI(
            model=Settings.MODEL_NAME,
            temperature=Settings.TEMPERATURE,
            api_key=Settings.OPENAI_API_KEY
        )


    def get_llm(self):
        return self.llm
