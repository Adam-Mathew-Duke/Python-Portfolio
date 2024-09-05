'''
Name:           clean_currency_string.py
Version:        1
Description:    Remove whitespace, comma and dollar sign
                from a string of text for example: $13,305.60 
'''

import streamlit as st

input_string = st.text_input("Input currency string:","")

# remove comma and dollar sign
output_string = input_string.replace(',', '')
output_string = output_string.replace('$', '')

# remove the whitespace
output_string = output_string.strip()

# display the result
st.write(output_string)

# end of code
