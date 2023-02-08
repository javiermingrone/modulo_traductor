from translate import Translator 
#modulo de traductor al ingles para utilizar en cualquier proyecto

traductor = Translator(from_lang='es', to_lang='en')

text = traductor.translate(input('Escriba el texto a traducir: '))

print(text)

