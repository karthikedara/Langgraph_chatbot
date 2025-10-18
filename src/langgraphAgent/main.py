import streamlit as st
from src.langgraphAgent.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphAgent.LLMs.GroqLLM import GroqLLM
from src.langgraphAgent.graphbuilder.graphbuilder import GraphBuilder
from src.langgraphAgent.ui.streamlitui.displayresult import DisplayResultStreamlit





def load_langgraph_agentic_app():
    """
    Loads and runs the LangGraph AgenticAI application with Streamlit UI.
    This function initializes the UI, handles user input, configures the LLM model,
    sets up the graph based on the selected use case, and displays the output while 
    implementing exception handling for robustness.

    """
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load the input from UI")
        return
    
    user_message = st.chat_input("Enter your message")
    if user_message:
        try:
            obj_llm_config = GroqLLM(user_control_input=user_input)
            model = obj_llm_config.get_llm()
            if not model:
                st.error("ERROR: Failed to load LLM model")
                return
            usecase = user_input.get("selected_usecase")
            if not usecase:
                st.error("ERROR: Failed to get usecase")
                return
            graph_builder = GraphBuilder(model)
            try:
                graph = graph_builder.setup_graph(usecase)
                print(user_message)
                DisplayResultStreamlit(usecase,graph,user_message).disply_result_on_ui()
            except Exception as e:
                st.error(f"Error:Graph setup failed{e}")
                return
        except Exception as e:
            st.error(f"Error:Graph setup failed{e}")
            return
            