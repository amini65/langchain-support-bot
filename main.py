from models.llm_manager import LLMManager
from memory.conversation_memory import ConversationManager
from chains.support_chain import SupportAgent

def main():
    print("🤖 Customer Support Bot - Powered by LangChain")
    print("=" * 50)
    print("Type 'exit' to quit\n")
    
    llm_manager = LLMManager()
    conversation_manager = ConversationManager()
    
    agent = SupportAgent(
        llm=llm_manager.get_llm(),
        memory=conversation_manager.get_memory()
    )
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "exit":
            print("\n👋 Thank you for using our support bot!")


            history = conversation_manager.get_history()
            if history['chat_history']:
                summary = "User ended the conversation. Please review the chat history."
                agent.chat(f"Send this summary to admin: {summary}")
            print("خداحافظ!")
            break
        
        response = agent.chat(user_input)
        print(f"\nBot: {response}\n")

if __name__ == "__main__":
    main()
