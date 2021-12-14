# Input for the program (change those)
initialID = 1575 # the show's id.
toPrintOnlyLinks = False # If True, will ALSO print the output list as only links.
http_timeout = 60 # If the Anilist does not respond after http_timeout seconds the script will fail.

# filters below does not apply to the initial id!
filterUnknownFormat = True # If True, the output will not contain entries with unannounced format (TV, TV Short, Movie, etc).
filterTV = False # If True, the output will not contain entries of TV format.
filterTVShort = True # If True, the output will not contain entries of TV Short format.
filterMovie = False # If True, the output will not contain entries of Movie format.
filterSpecial = False # If True, the output will not contain entries of Special format.
filterOVA = False # If True, the output will not contain entries of OVA format.
filterONA = False # If True, the output will not contain entries of ONA format.
filterMusic = True # If True, the output will not contain entries of Music format.
filterUnknownDuration = True # If True, the output will not contain entries with unannounced length of episode.
minimumDuration = 14 # How many minutes does a episode has to have in order to be included in the output.
