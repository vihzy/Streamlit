import streamlit as st
import numpy as np
import pandas as pd
import sqlalchemy
from st_aggrid import AgGrid

#读取数据库中的数据
conn = sqlalchemy.create_engine('mysql+pymysql://root:123654@localhost:3306/gzlib')
sql = 'SELECT * FROM 金融'
df = pd.read_sql(sql,conn)

#页面设置
st.set_page_config(
    page_title="Streamlit demo",layout="wide",)

#分标签页
tab1, tab2 = st.tabs(["广州图书馆金融类书籍", "charts"])

#标签页1
with tab1:
    st.title('广州图书馆金融类书籍')
    
    #筛选条件
    option1 = st.selectbox('请选择出版社', pd.concat([pd.Series('所有'),df['出版社']]))
    option2 = st.selectbox('请选择作者', pd.concat([pd.Series('所有'),df['作者']]))
        
    #筛选
    if option1 == '所有' and option2 == '所有':
        AgGrid(df,fit_columns_on_grid_load=True)   #AgGrid可以使dataframe完全展开
    elif option1 != '所有' and option2 == '所有':
        AgGrid(df[df['出版社']==option1],fit_columns_on_grid_load=True)
    elif option1 == '所有' and option2 != '所有':
        AgGrid(df[df['作者']==option2],fit_columns_on_grid_load=True)
    else:
        AgGrid(df[(df['出版社']==option1) & (df['作者']==option2)],fit_columns_on_grid_load=True)

#标签页2
with tab2:
    #地图数据可视化（来自于google api项目）
    df1 = pd.read_excel(r'C:\Users\64501\Desktop\Projects\Google API geolocation\output.xlsx')
    df1 = df1[df1['distance']!=0][['lat','lng']]
    df1.columns = ['lat', 'lon']
    st.map(df1)
    
    #空两行，不然挨得太紧
    st.markdown('&nbsp;')
    st.markdown('&nbsp;')

    
    #生成2列，列之间有一定空隙
    col1, col2, col3= st.columns([10, 1, 10])
    
    #画各类chart
    with col1:
        #line chart
        chart_data1 = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c'])
        st.line_chart(chart_data1) 
    with col2:
        st.empty() #本质是一个可插入一个组件的容器
    with col3:
        #bar chart
        chart_data2 = pd.DataFrame(np.random.randn(26, 1),index=[chr(i) for i in range(65,91)])
        st.bar_chart(chart_data2)

    
    

    




