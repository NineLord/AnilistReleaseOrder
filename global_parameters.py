url = 'https://graphql.anilist.co' # the database address.
template = "{0:6}|{1:7}|{2:9}|{3:11}|{4:32}|{5:100}" # How much padding to give between columns when printing the table
runDebug = False

# Each query to the site will be of this form
query = '''
query ($id: Int) {
	Media (id: $id, type: ANIME) {
		id
		title {
			romaji
			english
		}
		format
		startDate {
			year
			month
			day
		}
		relations {
			nodes {
				id
				type
				format
				duration
			}
		}
		siteUrl
	}
}
'''