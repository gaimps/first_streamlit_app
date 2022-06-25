import streamlit
import pandas

streamlit.title("My Mom's new healthy Diner")

streamlit.header('Breakfast Favorites')

streamlit.text('🥣Omega 3 & blueberry Oatmeal')
streamlit.text('🥗Kale,Spinach & Rocekt Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruits_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruits_list)
