from pandas.io.parsers import read_csv
import streamlit as st 
import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt 

@st.cache
def load_data():
    df =pd.read_csv('dropout-ratio-2012-2015.csv')
    df.replace(to_replace='NR',value=0,inplace=True)
    df['Upper Primary_Boys'].replace('Uppe_r_Primary',0,inplace=True)

    df.Primary_Boys = df.Primary_Boys.astype(float)
    df.Primary_Girls = df.Primary_Girls.astype(float)
    df['Secondary _Girls']=df['Secondary _Girls'].astype(float)
    df['Secondary _Boys']=df['Secondary _Boys'].astype(float)
    return df

df = load_data()

st.title('INDIAN SCHOOLS STATISTICS ANALYSIS')
st.sidebar.header('PROJECT OPTIONS')
options =[
    'ABOUT THE PROJECT',
    'Primary  Dropout Students ',
    'Upper Primary Dropout Students',
    'Secondary Dropout Students',
    'Higher Secondary Students'
    ]
choice_in = st.sidebar.selectbox('Select an option',options)


if choice_in ==options[0]:
    st.header=('Introduction')
    st.image('images.png')
    st.info('Education is a  basic need of every person. Some people dro this basic need due some problems.India is one the countries who are having higher dropout student ratio,the main reasons for being bale to complete their education are : Poverty,accessbility and availability. Dropout can also be said as one of the  major issues. ')

elif choice_in == options[1]:
    st.info(' 1. desciption about')
    fig,ax=plt.subplots()
    df.groupby('year').mean().plot(kind='line',figsize=(10,5),ax=ax)
    plt.xlabel('Year')
    plt.ylabel('Frequency')
    plt.title('Primary boys frequency from 2012-15')
    st.pyplot(fig)
  


    st.info(' 2. Description about')
    fig,ax=plt.subplots()
    df.groupby('State_UT').mean().head(10).plot(kind='line',figsize=(20,4),ax=ax)
    plt.xlabel('States')
    plt.ylabel('Reach of Droupout Students- BOYS')
    st.pyplot(fig)

    st.info('3. Description')
    fig,ax=plt.subplots()
    df.groupby('Primary_Total').mean().head(10).plot(kind='line',figsize=(15,10),ax=ax)
    plt.title('Total Primary Students VS Primary Boys and Primary Girls')
    plt.xlabel('Primary Total Frequency')
    plt.ylabel('Frequency')
    st.pyplot(fig)


    st.info('description')
    fig,ax=plt.subplots()
    df.groupby('State_UT').mean().plot(kind='line',figsize=(20,5),ax=ax)
    plt.xlabel('States')
    plt.ylabel('Dropout Students Frequency')
    plt.title( 'Ratio of Dropout Primary Students in States')
    st.pyplot(fig)

elif choice_in==options[2]:
    st.info('Description about')
    fig,ax=plt.subplots()
    df['Upper Primary_Boys'].value_counts().head(10).plot(ax=ax)
    df['Upper Primary_Girls'].value_counts().head(10).plot(ax=ax)
    df['Upper Primary_Total'].value_counts().head(10).plot(ax=ax)
    plt.xlabel('Upper Primary Students Data')
    plt.ylabel('Upper Primary Total')
    plt.title('Upper Primary Students VS Upper Primary Total')
    plt.legend()
    st.pyplot(fig)


    st.info('Description about')
    b = df['Upper Primary_Boys'].astype(float)
    c = df['Upper Primary_Girls'].astype(float)
    fig,ax=plt.subplots(1,1,figsize=(15,5))
    b.plot(kind='line',ax=ax)
    c.plot(kind='line',ax=ax)
    plt.title('Data of Higher Secondary Students')
    plt.xlabel('States')
    plt.ylabel('Boys and Girls Status')
    plt.legend()
    st.pyplot(fig)

elif choice_in==options[3]:
    st.info('description')
    k=df['Secondary _Boys']
    q=df['Secondary _Girls']
    fig,ax = plt.subplots(1,1,figsize=(15,5))
    k.plot(kind='line',ax=ax)
    q.plot(kind='line',ax=ax)
    plt.title('Data of Secondary Students')
    plt.xlabel('Years')
    plt.ylabel('Boys and Girls Status')
    plt.legend()
    st.pyplot(fig)
