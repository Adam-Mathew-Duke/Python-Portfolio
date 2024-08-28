## Portfolio

### Card Suits - Volume 2 ([View Code](https://github.com/Adam-Mathew-Duke/Python-portfolio/blob/main/Card%20Suits%20-%20Version%202))
`DESCRIPTION` An Aphasia memory exercise using card suits
`GOALS` Aid in memory improvement and confidence
`IMPROVEMENTS` Add better choice validation and positive user feedback
`TAKEAWAY` My first program using Tkinter

Function to display a new card (ASCII Symbol) on the screen:
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

Image from the app showing the card suit and the solution:

<img align="center" width="413" alt="image of card suites program" src="https://github.com/user-attachments/assets/e5b657f0-ec74-497d-9361-48ff5de3212e">

### MTG Card Price - Volume 2 ([View Code](https://github.com/Adam-Mathew-Duke/Python-portfolio/blob/main/MTG%20Card%20Price))
`DESCRIPTION` Terminal based MTG card price lookup tool
`GOALS` A simple way to lookup current MTG card prices and save them to a text file
`IMPROVEMENTS` Refine the code do further testing
`TAKEAWAY` My first program that calls an API

Screenshot of the MTG Card Price program in action:

<img width="388" alt="image" src="https://github.com/user-attachments/assets/ecb2ac89-d556-447e-ac21-e6894230e4a6">



