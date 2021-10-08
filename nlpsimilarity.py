from nltk.corpus import wordnet
import tkinter as tk
window = tk.Tk()
window.geometry("150x150")

def work():
	w1 = f"{ent_input1.get()}.n.01"
	w2 = f"{ent_input2.get()}.n.01"
	ww1 = wordnet.synset(w1)
	ww2 = wordnet.synset(w2)
	value = ww1.wup_similarity(ww2)

	if value < .5:
		lbl_value["text"] = "These words aren't very much alike"
	if value > .5 and value < .8:
		lbl_value["text"] = "These words are pretty similar"
	if value > .8 and value < 1:
		lbl_value["text"] = "These words are super duper alike"
	if value == 1:
		lbl_value["text"] = "This is the same word or a direct synonym"

ent_input1 = tk.Entry(master=window, relief=tk.SUNKEN)
ent_input1.pack(side=tk.TOP)

ent_input2 = tk.Entry(master=window, relief=tk.SUNKEN)
ent_input2.pack(side=tk.TOP)

btn_go = tk.Button(master=window, relief=tk.RAISED, text="Go", command=work)
btn_go.pack(side=tk.TOP)

lbl_value = tk.Label(master=window, height=100, width=100, wraplength=150, text="Enter two words and I'll tell you whether or not I think they're similar!")
lbl_value.pack(side=tk.BOTTOM)

window.mainloop()