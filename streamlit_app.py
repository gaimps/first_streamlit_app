from ast import Try
import re
import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

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


def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get(
        "https://fruityvice.com/api/fruit/" + fruit_choice)

    fruityvice_normalized = pandas.json_normalize(
        fruityvice_response.json())
    return fruityvice_normalized


streamlit.header("Fruityvice Fruit Advice!")
try:
    fruit_choice = streamlit.text_input(
        'What fruit would you like information about?')
    if not fruit_choice:
        streamlit.error('Please select a fruit to get information')
    else:
        back_from_function = get_fruityvice_data(fruit_choice)
        streamlit.dataframe(back_from_function)
except URLError as e:
    streamlit.error()


# streamlit.text(fruityvice_response.json())


# write your own comment -what does the next line do?

# write your own comment - what does this do?

# streamlit.stop()

streamlit.header("The fruit load list contains:")


def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("select * from fruit_load_list")
        return my_cur.fetchall()


if streamlit.button('Get fruit load list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    my_cnx.close()
    streamlit.dataframe(my_data_rows)


def insert_row_snowflakes(new_fruit):
    with my_cnx.cursor() as my_cur:
        my_cur.execute(
            "insert into fruit_load_list values ('" + new_fruit + "')")
        return "Thanks for adding " + new_fruit


add_my_fruit = streamlit.text_input(
    "what fruit would you like to add? ")

if streamlit.button('Add a Fruit to the list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_function = insert_row_snowflakes(add_my_fruit)
    my_cnx.close()
    streamlit.text(back_from_function)
