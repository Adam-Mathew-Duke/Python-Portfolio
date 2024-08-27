## Python Portfolio

### Card Suits - Volume 2
+ An Aphasia memory exercise using playing card suits
+ Adds GUI support witih tkinter

Lets look at the card_display() function and see what it does:
+ Clear the answer text so it's hidden from the user - the name of the suit is a secret for now eg. Harts
+ Set the answer text to a new random card suit. eg Harts
+ Compare the answer text to the list of card suits. eg. "Harts" is a match to "♥"
+ Once we know it's harts we set the card suit and choose the appropiate color in this case it's red.

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


