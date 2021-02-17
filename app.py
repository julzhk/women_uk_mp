import pandas as pd
import streamlit as st
import altair as alt

# run with
# streamlit run <SCRIPT.py>

def load_data():
    CSV_DATA_PATH = 'most-votes-for-women.tsv'
    data = pd.read_csv(CSV_DATA_PATH, delimiter='\t').fillna(value=0)
    return data


def main():
    st.title('Votes for women - UK')
    df = load_data().transpose()
    df = df[3:]
    df['total'] = df.sum(axis=1)

    if st.checkbox('Show raw data'):
        st.subheader('Raw data')
        st.write(df)
    df["total"] = pd.to_numeric(df["total"])
    df.sort_values(by='total', inplace=True)
    df['name'] = df.index
    st.write(alt.Chart(df).mark_bar().encode(
        y='name',
        x=alt.Y('total', sort=['name']),
    ))

if __name__ == '__main__':
    main()
