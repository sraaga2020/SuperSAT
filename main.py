from datasets import load_dataset
import streamlit as st

ds = load_dataset("betterMateusz/SAT_Writting_Reading_Assessment_Question_Bank")
df = ds["train"].to_pandas()
print(df.head())

def focus_skill():
  focus = st.text_input("Select the skill you would like to focus on: ")

focus_skill()
