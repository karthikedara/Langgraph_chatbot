from src.langgraphAgent.state.state import State

class BasicChatBotNode:
    """
    basic chatbot logic implementation
    
    """
    def __init__(self,model):
        self.llm = model
    def process(self,state:State)->dict:
        """Process the input state and generates response"""
        return {'messages':self.llm.invoke(state['messages'])}
        