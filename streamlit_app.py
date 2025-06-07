import streamlit as st
import numpy as np
import pandas as pd

# Set the title of the Streamlit app
st.title('Interactive Linear Function Plot')

# Add sliders to the sidebar for user input
st.sidebar.header('Adjust the Linear Function')
a = st.sidebar.slider('Slope (a)', -10.0, 10.0, 1.0, 0.1)
b = st.sidebar.slider('Y-intercept (b)', -10.0, 10.0, 0.0, 0.1)

# Create a range of x values
x = np.linspace(-10, 10, 400)

# Calculate the corresponding y values
y = a * x + b

# Create a Pandas DataFrame to hold the data
df = pd.DataFrame({
    'x': x,
    'y': y
})

# Display the equation of the line
st.write(f"Displaying the plot for: y = {a:.2f}x + {b:.2f}")

# Plot the linear function using st.line_chart
st.line_chart(df.rename(columns={'x':'index'}).set_index('index'))
