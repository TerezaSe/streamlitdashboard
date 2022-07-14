import streamlit as st
from sqlalchemy import create_engine
import pandas as pd
import pymysql
import plotly.graph_objects as go
import plotly.express as px



##################
#data
##################
engine = create_engine("mysql+pymysql://data-student:u9AB6hWGsNkNcRDm@data.engeto.com:3306/data_academy_04_2022")
query = """SELECT
            start_station_latitude as lat,
            start_station_longitude as lon
        FROM edinburgh_bikes
        LIMIT 20000

"""

df_bikes = pd.read_sql(sql=query, con=engine)


##################
#vizualizace
##################


st.title('Moje prvni appka')

st.write('Toto je moje prvni aplikace, kterou delam')

page = st.sidebar.radio('Select page',['Mapa','Thompson'])
if page == 'Mapa':
    st.write('Mapa používání sdílených dat v Edinbourgu')
    st.map(df_bikes)
    

if page == 'Thompson':
    st.write('Thompson sampling')
