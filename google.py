
from googletrans import Translator
sen = str(input("Enter the sentance: "))
k=Translator()
lang=str(input("your language : "))
convert =str(input("which language : "))
output= k.translate(sen,src=lang,dest=convert)
print(output.text)
'''

# To Print all the languages that google
# translator supports
import googletrans
 
 
print(googletrans.LANGUAGES)'''