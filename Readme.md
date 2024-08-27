## Python Portfolio

### Card Suits - Volume 2
+ An Aphasia memory exercise using playing card suits
+ Adds GUI support witih tkinter

Here is the card_display() function that resets the answer and displays a
new random card suit on the screen.

+ Choose a new random card suit - card_text eg. "Harts"
+ Next we compare the card_text to the card_suit and display the appropiate ASCII character on screen eg. "♥"
+ We also set the color of the card_suit eg. "♥" to the appropate color eg. red in this case.

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


