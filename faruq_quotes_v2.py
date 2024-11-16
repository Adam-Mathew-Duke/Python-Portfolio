'''
Faruq Quotes

To do:
Re-write with no HTML
Add a picture for each quote of the battlebots or Faruq
'''

import streamlit as st
import random

from faruq_quotes_data_v2 import faruq_quotes_list
quote = random.randint(0,len(faruq_quotes_list)-1)

background_colors = [
'#000000','#00008B','#006400','#8B0000','#2F4F4F',
'#556B2F','#8B008B','#008B8B','#FF8C00','#9400D3']

string = ""

for word in faruq_quotes_list[quote].split():

    # random number is used for random word background highlights
    rand = random.randrange(100)

    # upper case words get a color background and larger font
    if word.isupper() and len(word) >= 2:
        string += ' <font style=color:'+'white'+';background:'+background_colors[random.randint(0,len(background_colors)-1)]+';font-size:25px;line-height: normal;>'+word+'</font>'
    
    # random words get a color background and a larger font
    elif rand >= 0 and rand <= 10 and len(word) >= 5:
        string += ' <font style=color:white;background:'+background_colors[random.randint(0,len(background_colors)-1)]+';font-size:25px;line-height: normal;>'+word+'</font>'
    
    # other words are printed out as normal
    else:
        string += ' <font style=font-size:20px;line-height: normal;>'+word+'</font>'

st.header("Faruq BattleBots Quotes")
st.html(string)
st.write('')
st.write('')
st.button("New Faruq Quote")
st.divider()
st.page_link("https://battlebots.fandom.com/wiki/Faruq_Tauheed", label="Learn about the Faruq on the Battle Bots Wiki!", icon="🌐")
st.page_link("https://buymeacoffee.com/adamd", label="Buy me a coffee!", icon="☕")

# end of code
