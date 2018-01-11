# Generate a certain amount of random http codes for test data
import random, json

httpDictionary = {'100':'Continue','101':'SwitchingProtocols','102':'Processing','200':'OK','201':'Created','202':'Accepted','203':'Non-AuthoritativeInformation','204':'NoContent','205':'ResetContent','206':'PartialContent','207':'Multi-Status','208':'AlreadyReported','226':'IMUsed','300':'MultipleChoices','301':'MovedPermanently','302':'Found','303':'SeeOther','304':'NotModified','305':'UseProxy','307':'TemporaryRedirect','308':'PermanentRedirect','400':'BadRequest','401':'Unauthorized','402':'PaymentRequired','403':'Forbidden','404':'NotFound','405':'MethodNotAllowed','406':'NotAcceptable','407':'ProxyAuthenticationRequired','408':'RequestTimeout','409':'Conflict','410':'Gone','411':'LengthRequired','412':'PreconditionFailed','413':'RequestEntityTooLarge','414':'Request-URITooLong','415':'UnsupportedMediaType','416':'RequestedRangeNotSatisfiable','417':'ExpectationFailed','422':'UnprocessableEntity','423':'Locked','424':'FailedDependency','426':'UpgradeRequired','428':'PreconditionRequired','429':'TooManyRequests','431':'RequestHeaderFieldsTooLarge','500':'InternalServerError','501':'NotImplemented','502':'BadGateway','503':'ServiceUnavailable','504':'GatewayTimeout','505':'HTTPVersionNotSupported','506':'VariantAlsoNegotiates','507':'InsufficientStorage','508':'LoopDetected','510':'NotExtended','511':'NetworkAuthenticationRequired'}

def http_output(responsesExpected, argsCodes):
	global http_responseCode
	responseCodes = []
	# Generate the list of http keys
	httpKeys = list(httpDictionary.keys())
	# generate x amount of response codes
	try:
		# if no codes in the arguements array exist we'll just
		# print n amount of random response codes
		if not argsCodes:
			for _ in range(responsesExpected):
				# get n amount of random keys from the list
				randomKey = random.choice(httpKeys)
				# get the value of the random key
				value = httpDictionary[randomKey]
				# responseCodes[randomKey] = value
				newObj = {randomKey:value}
				responseCodes.append(newObj)
			# Return the results
			return json.dumps(responseCodes)
		elif argsCodes:
			for _ in range(responsesExpected):
				# get n amount of random keys from the list
				for code in argsCodes:
					value = httpDictionary[code]
					responseCodes[code] = value
			return responseCodes
	except Exception as e:
		raise e
print(http_output(500,['200']))