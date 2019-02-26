# WordBot
I have a developed a simple dictionary Bot in Python using nltk and Flask python packages.
This Bot will take a word from the user and gives definition, synonyms and antonyms for the word given by the user.
For this i have written UI in html,logic in python,style sheets in CSS.
Below are the important points need to be considered while building the bot:
    1.HTML templates need to maintained in templates folder.
      Ex: C:\Python27\Bot\templates\wordhome.html
    2.Static objects like images., need to maintain in static folder.
      Ex: C:\Python27\Bot\static\scrabble.jpg
    3.Python code would be present in main folder.
      Ex: C:\Python27\Bot\wordcode.py
Working :
1.	First we need to excecute python code using python wordcode.py in command prompt.There we will get the URL where the Bot is running.
2.  Ex:Type the URL : http://127.0.0.1:5000/ in browser(We need to give 5000 – port number in python code as app.run(debug=True,port=5000).
3.	The browser will show the below response,like
            user :
            bot  :
              Friends chatbot:
                Definition  Synonym  Antonym   --- > options for response-user choice
                
4. Then if User enters any word and clicking appropriate word bot will give response according to user choice.
       Ex: User : Program and if we click on Definition then we will get the response like program definition. 
       
5. If your enters morethan a single word then the bot will send response like “Please enter a single word”.

            


