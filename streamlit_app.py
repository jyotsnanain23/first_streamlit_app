import streamlit
import pandas
streamlit.title('My Mom\'s New Healthy diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣Omega3 & Blueberry Oatmeal')
streamlit.text('🥗Kale,spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free Range Egg')
streamlit.text('🥑🍞Avacado Toast')
                
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt"
streamlit.dataframe(my_fruit_list)
