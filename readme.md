# Comprehensive Problem Solving: From Analysis to Action

This project presents a framework that integrates various methodologies and technologies, such as Python, full-stack development, **machine learning**, and problem-solving techniques. The solution employs the PDCA (Plan-Do-Check-Act) method, process design using BPMN (Business Process Model and Notation) methodology, Mermaid library for diagramming, and interactive dashboards for data analysis. Additionally, it incorporates ETL (Extract, Transform, Load) for data treatment, goal setting, and various visualization techniques.

### Key Features:

1. **Patient Lifecycle Mapping**: 
   - The framework begins by mapping the patient's lifecycle within a given process and identifying critical touchpoints to understand the patient journey.
   
2. **Custom NLP and Machine Learning Algorithms**: 
   - Two custom-built Python-based NLP and **Machine Learning** algorithms are used: one for preparing data and capturing sentiment from user feedback, and another for organizing this data, correlating sentiment with specific processes to generate sentiment scores for each touchpoint.
   
   - **Text Processing and Sentiment Analysis**: The first algorithm leverages NLTK (Natural Language Toolkit) and VADER for sentiment analysis, focusing on efficiently processing large amounts of unstructured feedback. It provides a granular, sentence-level sentiment evaluation, ensuring accurate identification of user concerns.
   
   - **Text Categorization and Touchpoint Extraction with Machine Learning**: The second algorithm uses spaCy and **BERT (a machine learning model)** for natural language processing, allowing for precise categorization of feedback and extraction of key touchpoints, enhancing the analysis of critical interactions.

3. **Sentiment-Based Process Analysis**:
   - The generated sentiment scores help identify pain points in the processes, allowing for targeted improvement efforts.

4. **Root Cause Analysis**: 
   - A root cause analysis is performed to prioritize the most significant pain points, leading to the definition of goals based on internal benchmarks.

5. **Action Plan Development**:
   - Based on the analysis, a strategic action plan is developed aimed at improving patient care and identifying internal improvement opportunities and potential revenue enhancements.

### Structured Approach:

The web app is designed in four stages, beginning with process mapping and continuing through sentiment analysis, root cause identification, and action planning. The process design step ensures effective data categorization, connecting data analysis directly to operational gaps.

An interactive dashboard is provided for exploring the results and gaining insights, with detailed information available in each stage of the app.

___

If you would like to see the app in action, visit: [https://pysolutions.streamlit.app/](https://pysolutions.streamlit.app/)
