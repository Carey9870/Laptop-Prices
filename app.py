import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import preprocessor, helper
import plotly.express as px

# load/read data
lap_price = pd.read_csv('laptop_data.csv')

# load preprocessor.py
lap_price = preprocessor.preprocess(lap_price)

# sidebar ui
st.sidebar.title('Laptop Prices Analysis')

# sidebar components
user_menu = st.sidebar.radio(
    'Select an Option', ('Most used Laptops', 'Inches of Laptops', 'Screen Resolution of Laptops', 
                        'CPU found in most Laptops', 'Kinds and Types of RAM', 'Memory/Hard Drives in Laptops', 'Gpu Found in Laptops',
                        'Operating Systems in Laptops', 'Weight of Laptops'))

if user_menu == 'Most used Laptops':
    st.sidebar.header('Most used Laptops')
    selected_top_5 = st.sidebar.checkbox('Top 5 most used laptops')
    
    if selected_top_5:
        st.title('Top 5 most used laptops')
        top_5_most_used_laptops = lap_price.Company.value_counts()[:5]
        st.table(top_5_most_used_laptops)
        
        # A bar graph showing top_5_most_used_laptops
        st.title('A Bar Graph Showing top 5 used laptops')
        top_5 = px.bar(lap_price.Company.value_counts()[:5])
        st.plotly_chart(top_5)
    else:
        most_used_laptops = helper.most_used_laptops(lap_price)
        st.table(most_used_laptops)
        
        #  A Bar Graph Diagram/plot
        st.title('A Bar Graph Showing most used laptops')
        plt.figure(figsize=(20,20))
        fig = px.bar(lap_price.Company.value_counts())
        plt.show()
        st.plotly_chart(fig)

if user_menu == 'Inches of Laptops':
        st.title('Showing Laptop Inches')
        laptops_inches = helper.inches_of_laptops(lap_price)
        st.table(laptops_inches)
        
        #  A Bar Graph Diagram/plot
        st.title('A Bar Graph Showing inches in laptops')
        fig =px.bar(lap_price.Inches.value_counts())
        st.plotly_chart(fig)

if user_menu == 'Screen Resolution of Laptops':
    st.title('Showing Laptop Inches')
    laptops_ScreenResolution = helper.Screen_Resolution_of_Laptops(lap_price)
    st.table(laptops_ScreenResolution)
    
    #  A Bar Graph Diagram/plot
    st.title('A Bar Graph showing Laptops of Inches')
    fig =px.bar(lap_price.ScreenResolution.value_counts())
    st.plotly_chart(fig)

if user_menu == 'CPU found in most Laptops':
    st.title('CPU Found in most Laptops')
    cpu = helper.CPU(lap_price)
    st.table(cpu)
    
    # A Bar Graph Diagram/plot
    st.title('A Bar Graph showing CPU found in most Laptops')
    fig =px.bar(lap_price.Cpu.value_counts())
    st.plotly_chart(fig)

if user_menu == 'Kinds and Types of RAM':
    st.title('Kinds and Types of RAM')
    ram = helper.Ram(lap_price)
    st.table(ram)
    
    # A Bar Graph Diagram/plot
    st.title('A Bar Graph showing Ram found in most Laptops')
    fig =px.bar(lap_price.Ram.value_counts())
    st.plotly_chart(fig)

if user_menu == 'Memory/Hard Drives in Laptops':
    st.title('Memory/Hard Drives Found in Laptops')
    memory = helper.Memory(lap_price)
    st.table(memory)
    
    # A Bar Graph Diagram/plot
    st.title('A Bar Graph showing Memory/Hard Drives found in most Laptops')
    fig = px.bar(lap_price.Memory.value_counts())
    st.plotly_chart(fig)

if user_menu == 'Gpu Found in Laptops':
    st.title('Gpu\'s Found in Laptops')
    gpu = helper.Gpu(lap_price)
    st.table(gpu)
    
    # A Bar Graph Diagram/plot
    st.title('A Bar Graph showing Gpu\'s found in most Laptops')
    fig = px.bar(lap_price.Gpu.value_counts())
    st.plotly_chart(fig)

if user_menu == 'Operating Systems in Laptops':
    st.title('Operating Systems in Laptops')
    os = helper.Os(lap_price)
    st.table(os)
    
    # A Bar Graph Diagram/plot
    st.title('A Bar Graph showing Operating Systems found in most Laptops')
    fig = px.bar(lap_price.OpSys.value_counts())
    st.plotly_chart(fig)

if user_menu == 'Weight of Laptops':
    st.title('Weight of Laptops')
    weight = helper.Weight(lap_price)
    st.table(weight)
    
    # A Bar Graph Diagram/plot
    st.title('A Bar Graph showing Weight of Laptops found in most Laptops')
    fig = px.bar(lap_price.Weight.value_counts())
    st.plotly_chart(fig)