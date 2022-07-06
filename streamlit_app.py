import streamlit
import pandas
import requests

streamlit.title("My Mom's new healthy Diner")

streamlit.header('Breakfast Favorites')

streamlit.text('🥣Omega 3 & blueberry Oatmeal')
streamlit.text('🥗Kale,Spinach & Rocekt Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruits_list = pandas.read_csv(
    "https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# set the index
my_fruits_list = my_fruits_list.set_index("Fruit")

# pick list
fruits_selected = streamlit.multiselect("Pick some fruits", list(
    my_fruits_list.index), ['Avocado', 'Strawberries'])

fruit_to_show = my_fruits_list.loc[fruits_selected]
# display the table
streamlit.dataframe(fruit_to_show)


streamlit.header("Fruityvice Fruit Advice!")

fruityvice_response = requests.get(
    "https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())


# write your own comment -what does the next line do?
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)
