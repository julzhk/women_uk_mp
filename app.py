import altair as alt
import pandas as pd
import streamlit as st


# run with
# streamlit run <SCRIPT.py>

def load_data():
    CSV_DATA_PATH = 'most-votes-for-women.tsv'
    data = pd.read_csv(CSV_DATA_PATH, delimiter='\t').fillna(value=0)
    st.write(data.head())
    return data


def main():
    st.title('Votes for women - UK')
    df = load_data().transpose()
    df = set_column_labels_cut_metadata(df)
    st.write(df.head())
    df['total'] = df.sum(axis=1)

    if st.checkbox('Show raw data'):
        st.subheader('Raw data')
        st.write(df)
    df["total"] = pd.to_numeric(df["total"])
    df.sort_values(by='total', inplace=True, ascending=False)
    df['name'] = df.index
    st.write(df.total)
    st.write(alt.Chart(df).mark_bar().encode(
        y='name',
        x=alt.Y('total', sort=['name']),
    ))


def set_column_labels_cut_metadata(df):
    # columns are Election year
    df.columns = df.iloc[0]
    # remove party row
    party = df[0][3:]
    st.write(party)
    df = df.drop([0], axis=1)
    df = df[3:]
    # first column (party affiliation is string, so casts df as a string. This makes it numbers
    df = df.apply(pd.to_numeric)
    return df


if __name__ == '__main__':
    main()
