Python :
from flask import Flask, render_template, request
import os
import time
from nltk.corpus import wordnet

class Emp:
				
	def getdata(self,word):
		syns = wordnet.synsets(word)
		try:
			return " , ".join([syns[0].definition()])
		except IndexError:
			return []
	
	def get_synonyms(self,word):
		synonyms = []
		for syn in wordnet.synsets(word):
			for l in syn.lemmas():
				synonyms.append(l.name())
		set1=set(synonyms)
		str1= " , ".join(set1)
		if len(str1)>0:
			return str1
		else:
			return "There are no sysnonyms for this word"
		
	def get_antonym(self,word):
		antonyms = []
		for syn in wordnet.synsets(word):
			for l in syn.lemmas():
				if l.antonyms():
					antonyms.append(l.antonyms()[0].name())
		set2 = set(antonyms)
		str2 = " , ".join(set2)
		if len(str2)>0:
			return str2
		else:
			return "There are no antonyms for this word"
	
		
app = Flask(__name__,static_url_path='/static',static_folder = "static")

@app.route('/',methods=['GET','POST'])
def index():
	return  render_template('wordhome.html')
	
@app.route('/process', methods=['GET','POST'])
def process():
	f1=Emp()
	str4=request.form['user_input']
	list1 = str4.split()
	if len(list1)==1:
		word = str4.replace(" ","")
		if request.form['button1']=="Definition":
			bot=f1.getdata(word)
		elif request.form['button1']=="Synonyms":
			bot=f1.get_synonyms(word)
		elif request.form['button1']=="Antonyms":
			bot=f1.get_antonym(word)
	else:
		bot = 'Please enter a single word'
	return render_template('wordhome.html', user_input=request.form['user_input'],bot_response=bot)
	
if __name__ =='__main__':
	app.run(debug=True,port=5000)


