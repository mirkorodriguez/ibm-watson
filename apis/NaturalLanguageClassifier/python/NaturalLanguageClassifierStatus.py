import sys
import operator
import requests
import json
import twitter

from watson_developer_cloud import NaturalLanguageClassifierV1 as NaturalLanguageClassifier

#The IBM Bluemix credentials
nlc_username = '569206c1-3641-4e54-9438-7fbda0f146a0'
nlc_password = 'rPYrOqVdpfBi'

natural_language_classifier = NaturalLanguageClassifier(
  username=nlc_username, password=nlc_password)

classifierId = 'e4be4cx148-nlc-16';
status = natural_language_classifier.status(classifierId)

print (json.dumps(status, indent=2))