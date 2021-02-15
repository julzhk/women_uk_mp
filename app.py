import pandas as pd
import numpy as np
import streamlit as st

# run with
# streamlit run <SCRIPT.py>

def load_data():
    CSV_DATA_PATH = 'most-votes-for-women.tsv'
    data = pd.read_csv(CSV_DATA_PATH,delimiter='\t').fillna(value=0)
    return data

def main():
    st.title('Votes for women - UK')
    df = load_data().transpose()
    df['total'] = df.sum(axis=1)

    if st.checkbox('Show raw data'):
        st.subheader('Raw data')
        st.write(df)


if __name__ == '__main__':
    main()
