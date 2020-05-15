from ibm_watson import SpeechToTextV1
from ibm_watson import LanguageTranslatorV3

import json

from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from pandas.io.json import json_normalize




""" First get the required text from an audio file in mp3 format. 

"""
def get_sentence(filename):
	iam_apikey_s2t="API Key Credentials of Sound to text service of IBM watson"

	url_s2t="url credentials of IBM watson Sound to Text service"

	authenticator=IAMAuthenticator(iam_apikey_s2t)

	s2t=SpeechToTextV1(authenticator=authenticator)
	s2t.set_service_url(url_s2t)

	with open(filename,mode="rb") as wav:
		response=s2t.recognize(audio=wav,content_type='audio/mp3')
	
#response contains data about audio file in dictionary format
#print(response.result)

	json_normalize(response.result['results'],"alternatives")

	recognized_text=response.result['results'][0]["alternatives"][0]["transcript"]


	return(recognized_text)
	
	
	
#Now Translate the text into spanish
def translate_sentence(recognized_sentence):
	
	apikey_lt="API key credentials of IBM watson Language Translator Service"

	url_lt="url credentials of IBM watson Language Translator Service"

	version_lt="2018-05-01"

	authenticator=IAMAuthenticator(apikey_lt)

	language_translator=LanguageTranslatorV3(version=version_lt , authenticator=authenticator)

	language_translator.set_service_url(url_lt)

	json_normalize(language_translator.list_identifiable_languages().get_result(),"languages")

	translation_response=language_translator.translate(text=recognized_text,model_id="en-es")

#print(translation_response)

	translation=translation_response.get_result()

#print(translation)
	spanish_translation=translation["translations"][0]["translation"]

	return(spanish_translation)
	
	
	
	
filename="English.mp3"
recognized_text=get_sentence(filename)
print("The English Text: "+ recognized_text)

translated_text=translate_sentence(recognized_text)
print("The Spanish Translation: "+ translated_text)
