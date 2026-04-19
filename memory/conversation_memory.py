from langchain.memory import ConversationBufferMemory

class ConversationManager:
    def __init__(self):
        self.memory = ConversationBufferMemory(
            memory_key= "chat_history",
            return_message=True
        )


    def get_memory(self):
        return self.memory
    

    def get_history(self):
        return self.memory.load_memory_variables({})