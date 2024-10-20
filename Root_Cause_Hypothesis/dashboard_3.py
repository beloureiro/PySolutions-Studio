import streamlit as st
from Root_Cause_Hypothesis.rootdash import root_cause_analysis_panel
# from Root_Cause_Hypothesis.root_cause import run_root_cause_analysis

def run_root_cause_hypothesis():
    
    st.title("Root Cause Hypothesis Panel")
    # Chama a função do painel de análise de causas raízes
    root_cause_analysis_panel()
    

if __name__ == "__main__":
    run_root_cause_hypothesis()

