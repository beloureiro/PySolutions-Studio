import streamlit as st

def run_bcframework():
    st.title("Comprehensive Problem Solving: From Analysis to Action")
    st.markdown("""
    This web app presents a framework that integrates various methodologies and technologies, including Python, fullstack development, machine learning, problem-solving with the PDCA method, process design using BPMN methodology and the Mermaid library, as well as interactive dashboards for data analysis. It also incorporates data treatment (ETL), goal setting, and a wide range of visualizations.

    The framework is structured in four stages. It begins with mapping the patient lifecycle within the process and identifying critical touchpoints to understand the patient journey. 
    Two custom-built Python-based NLP algorithms were developed: the first prepares the data and captures sentiment from user feedback, while the second organizes the cleaned data, correlating sentiment data with specific processes (touchpoints) to generate a sentiment score for each process based on individual reviews.

    These sentiment scores help uncover key pain points within the processes. A root cause analysis is then conducted to prioritize the most significant causes, followed by the definition of preliminary goals based on internal benchmarks. These goals inform the development of a strategic action plan aimed at improving patient care, while identifying internal improvement opportunities and potential revenue enhancements.
    """, unsafe_allow_html=True)


    st.write("""
    Below, you will find more detailed information on each of the four stages of the web app.
    """)
    st.image("logo/bc_framework.png")  # Caminho da imagem
    st.write("""
    The process design was prioritized as the fundamental first step for effective data categorization and analysis. Understanding the operation before categorizing ensures a clear relationship between the data and the process.
    By modeling the patient lifecycle and identifying critical touchpoints, data categorization is aligned with operational reality. This structured approach directly connects data to the process's opportunity gaps.
    This integrated view links data analysis with process management, leading to more effective and targeted categorization.
    """)


    st.write("___")  # Linha de separação

    st.markdown("""
    <span style='color: #1b9e4b;'><strong>Use the navigation menu on the left (⬅️) to explore each stage of the web app in detail.</strong></span>
    """, unsafe_allow_html=True)



if __name__ == "__main__":
    run_bcframework()
