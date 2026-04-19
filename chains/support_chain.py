from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder

class SupportAgent:
    def __init__(self, llm, tools, memory):
        self.llm = llm
        self.tools = tools
        self.memory = memory
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a helpful customer support assistant.
            
Your responsibilities:
- Answer questions about products and their prices
- Help customers find the right product
- Escalate complex issues to admin via email if needed

Always be polite, professional, and helpful."""),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad")
        ])
        
        agent = create_openai_functions_agent(
            llm=self.llm,
            tools=self.tools,
            prompt=prompt
        )
        
        self.agent_executor = AgentExecutor(
            agent=agent,
            tools=self.tools,
            memory=self.memory,
            verbose=True,
            handle_parsing_errors=True
        )
    
    def chat(self, user_input: str) -> str:
        response = self.agent_executor.invoke({"input": user_input})
        return response["output"]
