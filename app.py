import pandas as pd
import streamlit as st
from streamlit_echarts import st_echarts

st.set_page_config(layout="wide")


# run with
# streamlit run <SCRIPT.py>


def load_data(full_spreadsheet=True):
    CSV_DATA_PATH = 'most-votes-for-women.tsv'
    data = pd.read_csv(CSV_DATA_PATH, delimiter='\t').fillna(value=0)
    if not full_spreadsheet:
        data = data.iloc[1:, 3:]
    return data


def main():
    st.title('Votes for women MPs - UK')
    df = load_data(full_spreadsheet=False).transpose()
    series_data = []

    for r in df:
        election_data = list(df[r])
        series_data.append(
            {'type': 'bar', 'stack': 'total', 'label': {'show': False},
             'emphasis': {'focus': 'opacity'},
             'data': election_data}
        )
    xaxis_data = list(df.index)
    options = {'grid': {'left': '3%', 'right': '4%', 'bottom': '3%', 'containLabel': True},
               'yAxis': {'type': 'value'},
               'xAxis': {'type': 'category', 'axisLabel': {
                   'show': True, 'rotate': 45
               },
                         'data': [1]},
               'dataZoom': [{'show': True, 'start': 0, 'end': 50},
                            {'type': 'inside', 'start': 0, 'end': 20}],
               'series': [{'type': 'bar', 'stack': 'total', 'label': {'show': True}, 'emphasis': {'focus': 'opacity'},
                           'data': []},
                          ]}
    options['series'] = series_data
    options['xAxis']['data'] = xaxis_data
    theme = {'color': ['#d87c7c', '#919e8b', '#d7ab82', '#6e7074', '#61a0a8', '#efa18d', '#787464', '#cc7e63', '#724e58', '#4b565b'], 'backgroundColor': 'rgba(254,248,239,1)', 'textStyle': {}, 'title': {'textStyle': {'color': '#333333'}, 'subtextStyle': {'color': '#aaaaaa'}}, 'line': {'itemStyle': {'borderWidth': 1}, 'lineStyle': {'width': 2}, 'symbolSize': 4, 'symbol': 'emptyCircle', 'smooth': False}, 'radar': {'itemStyle': {'borderWidth': 1}, 'lineStyle': {'width': 2}, 'symbolSize': 4, 'symbol': 'emptyCircle', 'smooth': False}, 'bar': {'itemStyle': {'barBorderWidth': 0, 'barBorderColor': '#ccc'}}, 'pie': {'itemStyle': {'borderWidth': 0, 'borderColor': '#ccc'}}, 'scatter': {'itemStyle': {'borderWidth': 0, 'borderColor': '#ccc'}}, 'boxplot': {'itemStyle': {'borderWidth': 0, 'borderColor': '#ccc'}}, 'parallel': {'itemStyle': {'borderWidth': 0, 'borderColor': '#ccc'}}, 'sankey': {'itemStyle': {'borderWidth': 0, 'borderColor': '#ccc'}}, 'funnel': {'itemStyle': {'borderWidth': 0, 'borderColor': '#ccc'}}, 'gauge': {'itemStyle': {'borderWidth': 0, 'borderColor': '#ccc'}}, 'candlestick': {'itemStyle': {'color': '#c23531', 'color0': '#314656', 'borderColor': '#c23531', 'borderColor0': '#314656', 'borderWidth': 1}}, 'graph': {'itemStyle': {'borderWidth': 0, 'borderColor': '#ccc'}, 'lineStyle': {'width': 1, 'color': '#aaa'}, 'symbolSize': 4, 'symbol': 'emptyCircle', 'smooth': False, 'color': ['#d87c7c', '#919e8b', '#d7ab82', '#6e7074', '#61a0a8', '#efa18d', '#787464', '#cc7e63', '#724e58', '#4b565b'], 'label': {'color': '#eee'}}, 'map': {'itemStyle': {'normal': {'areaColor': '#eeeeee', 'borderColor': '#444444', 'borderWidth': 0.5}, 'emphasis': {'areaColor': 'rgba(255,215,0,0.8)', 'borderColor': '#444444', 'borderWidth': 1}}, 'label': {'normal': {'textStyle': {'color': '#000000'}}, 'emphasis': {'textStyle': {'color': 'rgb(100,0,0)'}}}}, 'geo': {'itemStyle': {'normal': {'areaColor': '#eeeeee', 'borderColor': '#444444', 'borderWidth': 0.5}, 'emphasis': {'areaColor': 'rgba(255,215,0,0.8)', 'borderColor': '#444444', 'borderWidth': 1}}, 'label': {'normal': {'textStyle': {'color': '#000000'}}, 'emphasis': {'textStyle': {'color': 'rgb(100,0,0)'}}}}, 'categoryAxis': {'axisLine': {'show': True, 'lineStyle': {'color': '#333'}}, 'axisTick': {'show': True, 'lineStyle': {'color': '#333'}}, 'axisLabel': {'show': True, 'textStyle': {'color': '#333'}}, 'splitLine': {'show': False, 'lineStyle': {'color': ['#ccc']}}, 'splitArea': {'show': False, 'areaStyle': {'color': ['rgba(250,250,250,0.3)', 'rgba(200,200,200,0.3)']}}}, 'valueAxis': {'axisLine': {'show': True, 'lineStyle': {'color': '#333'}}, 'axisTick': {'show': True, 'lineStyle': {'color': '#333'}}, 'axisLabel': {'show': True, 'textStyle': {'color': '#333'}}, 'splitLine': {'show': True, 'lineStyle': {'color': ['#ccc']}}, 'splitArea': {'show': False, 'areaStyle': {'color': ['rgba(250,250,250,0.3)', 'rgba(200,200,200,0.3)']}}}, 'logAxis': {'axisLine': {'show': True, 'lineStyle': {'color': '#333'}}, 'axisTick': {'show': True, 'lineStyle': {'color': '#333'}}, 'axisLabel': {'show': True, 'textStyle': {'color': '#333'}}, 'splitLine': {'show': True, 'lineStyle': {'color': ['#ccc']}}, 'splitArea': {'show': False, 'areaStyle': {'color': ['rgba(250,250,250,0.3)', 'rgba(200,200,200,0.3)']}}}, 'timeAxis': {'axisLine': {'show': True, 'lineStyle': {'color': '#333'}}, 'axisTick': {'show': True, 'lineStyle': {'color': '#333'}}, 'axisLabel': {'show': True, 'textStyle': {'color': '#333'}}, 'splitLine': {'show': True, 'lineStyle': {'color': ['#ccc']}}, 'splitArea': {'show': False, 'areaStyle': {'color': ['rgba(250,250,250,0.3)', 'rgba(200,200,200,0.3)']}}}, 'toolbox': {'iconStyle': {'normal': {'borderColor': '#999999'}, 'emphasis': {'borderColor': '#666666'}}}, 'legend': {'textStyle': {'color': '#333333'}}, 'tooltip': {'axisPointer': {'lineStyle': {'color': '#cccccc', 'width': 1}, 'crossStyle': {'color': '#cccccc', 'width': 1}}}, 'timeline': {'lineStyle': {'color': '#293c55', 'width': 1}, 'itemStyle': {'normal': {'color': '#293c55', 'borderWidth': 1}, 'emphasis': {'color': '#a9334c'}}, 'controlStyle': {'normal': {'color': '#293c55', 'borderColor': '#293c55', 'borderWidth': 0.5}, 'emphasis': {'color': '#293c55', 'borderColor': '#293c55', 'borderWidth': 0.5}}, 'checkpointStyle': {'color': '#e43c59', 'borderColor': '#c23531'}, 'label': {'normal': {'textStyle': {'color': '#293c55'}}, 'emphasis': {'textStyle': {'color': '#293c55'}}}}, 'visualMap': {'color': ['#bf444c', '#d88273', '#f6efa6']}, 'dataZoom': {'backgroundColor': 'rgba(47,69,84,0)', 'dataBackgroundColor': 'rgba(47,69,84,0.3)', 'fillerColor': 'rgba(167,183,204,0.4)', 'handleColor': '#a7b7cc', 'handleSize': '100%', 'textStyle': {'color': '#333333'}}, 'markPoint': {'label': {'color': '#eee'}, 'emphasis': {'label': {'color': '#eee'}}}}

    st_echarts(options=options, height="600px",theme=theme)
    df = load_data().transpose()
    show_party(df)
    if st.checkbox('Show raw data'):
        st.subheader('Raw data')
        df = load_data(full_spreadsheet=True).transpose()
        st.write(df)
        df = load_data().transpose()
        df = set_column_labels_cut_metadata(df)
        df['total'] = df.sum(axis=1)
        df["total"] = pd.to_numeric(df["total"])
        df.sort_values(by='total', inplace=True, ascending=False)
        df['name'] = df.index
        st.write(df.total)


def show_party(df):
    party = df[0][3:]
    st.write('Party Affiliations')
    party_numbers = party.value_counts()
    data_vals = [{'value': v, 'name': i}
                 for i, v in party_numbers.items()]

    options = {'title': {'text': 'By Party',
                         'subtext': 'Count', 'left': 'center'},
               'tooltip': {'trigger': 'item'},
               'series': [
                   {'name': 'Number of MPs', 'type': 'pie', 'radius': '50%',
                    'data': [],
                    'emphasis': {'itemStyle': {'shadowBlur': 10, 'shadowOffsetX': 0, 'shadowColor': 'rgba(0, 0, 0, 0.5)'}}}]}
    options['series'][0]['data'] = data_vals
    st_echarts(options=options)


def set_column_labels_cut_metadata(df):
    # columns are Election year
    df.columns = df.iloc[0]
    # remove party row

    df = df.drop([0], axis=1)
    df = df[3:]
    # first column (party affiliation is string, so casts df as a string. This makes it numbers
    df = df.apply(pd.to_numeric)
    return df


if __name__ == '__main__':
    main()
