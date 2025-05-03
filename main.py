import streamlit as st 


master_tabs = st.tabs(["Fine Tuning","Communication Primitives"])


st.set_page_config(layout="wide")


with master_tabs[0]:
    st.markdown("""

   #### Model Abstractions 
   - Fine Tuning 
   - Knowledge Distillation 
        """)
    
with master_tabs[1]:

    st.markdown("""

    1.	One to One Communication 
2.	One to Many Communication
a.	Scatter – Send a tensor to different parts of tensor 
b.	Gather – Gather data 
c.	Reduce – Similar to Gather, But averaging/Summing 
d.	Broadcast – Send Identical copies to all other workers 
3.	Many to Many Communication 
a.	All Reduce – Reduce on 0, 
b.	All Gather – Perform gather on all Workers 

        """)