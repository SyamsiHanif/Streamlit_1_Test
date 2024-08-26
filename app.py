import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title('My First Streamlit App')

# Add a header
st.header('Welcome to Streamlit!')

# Add some text
st.write('This is a simple Streamlit app for beginners.')

# Display an image
st.image('https://via.placeholder.com/300', caption='Sample Image')

# Create some random data
data = np.random.randn(100, 3)
df = pd.DataFrame(data, columns=['A', 'B', 'C'])

# Display a chart
st.line_chart(df)

# Add an interactive widget
number = st.slider('Pick a number', 0, 100, 50)
st.write(f'You selected: {number}')
