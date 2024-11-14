import streamlit as st 
from pygwalker.api.streamlit import StreamlitRenderer

def main():
    #Set up stream lit interface
    st.set_page_config(
        page_title = "2_📊_interactive_visualization_tool", page_icon = "📊", layout = "wide"
    )
    st.header("📊 Interactive Visualization Tool")
    st.write("Welcome to Interactive Visualization Tool. Pls Enjoy!")
    # Render pygwalker
    if st.session_state.get("df") is not None:
        pyg_app = StreamlitRenderer(st.session_state.df)
        pyg_app.explorer()
    else:
        st.info("Please upload a dataset to begin using the interactive visualization tool")
    
if __name__ == "__main__":
    main()