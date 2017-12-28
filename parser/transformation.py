# Script to transform json objects into newline json objects
import json

json_file = '' # Add readfile here
json_transformed = '' # Add write file here

with open(json_file,'r') as orgFile, open(json_transformed, 'w') as newFile:
	data = json.load(orgFile)
	for item in data["features"]:
			json.dump(item, newFile)
			if data["features"].index(item) == len(data["features"])-1:
				continue
			else:
				newFile.write('\n')