import requests, json, sys, operator
from typing import Tuple, Set

import script_input, global_parameters
from classes import FuzzyDate, ShowData

def getInputFromCMD():
	argvLen = len(sys.argv)
	if argvLen != 2:
		print("Expecting only 1 argument from command line, instead got", argvLen - 1, "arguments")
		exit()
	else:
		try:
			return int(sys.argv[1], base=10)
		except ValueError:
			print("Argument isn't a number, it needs to be the id of the show")

# Make the HTTP Api request with our query,
# if fails prints error and exit the program.
def doQuery(id: int):
	response = requests.post(global_parameters.url, json={'query': global_parameters.query, 'variables': {'id': id}}, timeout=script_input.http_timeout)
	if response.ok:
		return response.json()
	else:
		print("Error at doQuery(", id, ")", sep="")
		print("Status code:", response.status_code)
		print("Message:", response.json()["errors"][0]["message"])
		# print("JSON:", json.dumps(response.json(), indent=4), sep="\n")
		exit()

def jsonToClass(queryJson) -> Tuple[ShowData, Set[int]]:
	innerJson = queryJson["data"]["Media"]

	fuzzyDate = FuzzyDate(innerJson["startDate"]["year"], innerJson["startDate"]["month"], innerJson["startDate"]["day"])
	title = innerJson["title"]["romaji"] if innerJson["title"]["english"] == None else innerJson["title"]["english"]
	format = "?" if innerJson["format"] == None else innerJson["format"]
	
	relations = set()
	for node in innerJson["relations"]["nodes"]:
		if node["type"] == "ANIME":
			if (node["format"] == None and not script_input.filterUnknownFormat) or (node["format"] == "TV" and not script_input.filterTV) or (node["format"] == "TV_SHORT" and not script_input.filterTVShort) or (node["format"] == "MOVIE" and not script_input.filterMovie) or (node["format"] == "SPECIAL" and not script_input.filterSpecial) or (node["format"] == "OVA" and not script_input.filterOVA) or (node["format"] == "ONA" and not script_input.filterONA) or (node["format"] == "MUSIC" and not script_input.filterMusic):
				if (node["duration"] == None and not script_input.filterUnknownDuration) or (not node["duration"] == None and node["duration"] >= script_input.minimumDuration):
					relations.add(node["id"])
	
	return (ShowData(innerJson["id"], title, format, fuzzyDate, innerJson["siteUrl"]), relations)

def printTableOfData(datas, isOnlyLinks: bool):
	if isOnlyLinks:
		for data in datas:
			print(data.siteUrl)
	else:
		print(global_parameters.template.format("Check", "Index", "ID", "Format", "Date", "URL", "Title"))
		index = 0
		for data in datas:
			print(data.formatOutput(global_parameters.template, index))
			index += 1

def debug():
	jsonObj = doQuery(102976)
	print(json.dumps(jsonObj, indent=4))
	dataObj, _ = jsonToClass(jsonObj)
	print(str(dataObj))
	printTableOfData([dataObj])

if __name__ == "__main__":
	if global_parameters.runDebug:
		debug()
	else:
		initialData, unprocessed = jsonToClass(doQuery(script_input.initialID))
		processed = {initialData}

		while len(unprocessed) != 0:
			id = unprocessed.pop()
			newData, newUnprocessed = jsonToClass(doQuery(id))

			processed.add(newData)

			for newID in newUnprocessed:
				if not any(data.id == newID for data in processed):
					unprocessed.add(newID)

		sorted_processed = sorted(processed, key=operator.attrgetter("date"))
		printTableOfData(sorted_processed, False)

		if script_input.toPrintOnlyLinks:
			print()
			printTableOfData(sorted_processed, True)