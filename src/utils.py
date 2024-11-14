import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

def execute_plt_code(code: str, df: pd.DataFrame):
    try:
        local_vars = {"plt":plt, "df":df}
        compliled_code = compile(code, "<string>", "exec")
        exec(compliled_code, globals(), local_vars)
        return plt.gcf()
    except Exception as e:
        st.error(f"Error executing plt code: {e}")
        return None
        