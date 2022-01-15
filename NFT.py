import requests

first = 1
traits = {}

for i in range(5001):
	if i == 0:
		first = 1
	else:
		URL = "https://soundmint-public.s3.amazonaws.com/KLOUD_REVEALED/meta/"+str(i)

		RESP = requests.get(URL)
		resp_readable = RESP.json()
		
		for trait in resp_readable['attributes']:


			try:
				traits[trait['trait_type']][trait['value']] = traits[trait['trait_type']][trait['value']]+1
			except:
				try:
					traits[trait['trait_type']].update({trait['value']:1})
				except:
					traits[trait['trait_type']] = {trait['value']:1}

print(traits)