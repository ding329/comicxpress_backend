from django.core.exceptions import ValidationError

def removeJavascriptKeyword(value):
    if "javascript:" in value:
        raise ValidationError('string contains javascript')

def validateInterger(value):
   if 0 > value:
	raise ValidationError("Int value is negative")
