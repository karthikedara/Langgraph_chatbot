from langgraph.graph import StateGraph
from src.langgraphAgent.state.state import State
from src.langgraphAgent.node.basicchatbot import BasicChatBotNode
from langgraph.graph import START,END


class GraphBuilder:
    def __init__(self,model):
        self.llm = model
        self.graph_builder = StateGraph(State)
    def basic_chatbot_graph(self):
        """
        Builds a basic chat bot using graph
        This method initialized a chat bot node using the graph.
        The chatbot node is set as both start and end point of graph
        
        """
        self.basic_chatbot=BasicChatBotNode(self.llm)
        self.graph_builder.add_node("chatbot",self.basic_chatbot.process)
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_edge("chatbot",END)

    def setup_graph(self,usecase:str):
        """setup the graph for the selected usecase"""
        if usecase =="Basic Chatbot":
            self.basic_chatbot_graph()
        return self.graph_builder.compile()
        
        