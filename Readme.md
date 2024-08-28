## Python Portfolio

### Card Suits - Volume 2
+ An Aphasia memory exercise using playing card suits
+ Adds GUI support witih tkinter
+ Example function that displays a new random card suit on the screen
```
def card_display():

	answer_text.set('') # clear the answer
	card_text.set(card_suit[random.randint(0,3)]) # new random suit
	button_text.set('Check') # update the button

	# update the card suit
	if card_text.get() == card_suit[0]:
		card_label.config(fg=card_color[0])
	elif card_text.get() == card_suit[1]:
		card_label.config(fg=card_color[1])
	elif card_text.get() == card_suit[2]:
		card_label.config(fg=card_color[2])
	elif card_text.get() == card_suit[3]:
		card_label.config(fg=card_color[3])

# end of code
```
<img align="center" width="413" alt="image of card suites program" src="https://github.com/user-attachments/assets/e5b657f0-ec74-497d-9361-48ff5de3212e">

