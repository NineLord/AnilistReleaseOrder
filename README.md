# AnilistReleaseOrder
A short script to query Anilist's database about specific shows,
which returns a list of each entry, in release order.
Based on Anilist API:
- https://anilist.gitbook.io/anilist-apiv2-docs/
- https://anilist.github.io/ApiV2-GraphQL-Docs/

## Requirements / Installation:
- Uses Python 3 (tested on 3.9.9).
- Needs lib "requests", to install it run:
  > python3 -m pip install requests

## How to use the script:
1. Go to a specific show page on anilist, for example:
   > https://anilist.co/anime/9260/Kizumonogatari-Part-1-Tekketsu/
2. From the URL get the show's ID, in our example its:
   > 9260
3. In the "script_input.py" file change the "initialID" variable to the ID you found.
4. And then run the script, like so:
   > python3 main.py

## Other useful information about the script:
- Any other parameter in "script_input.py" can be changed to refine the script output.
  Each of them has a comment that explains what it does.
  It is best to leave the filter as they are, to avoid getting "crossover" shows into the output.

## Unresolved TODOs:
- Take as input a username, and change the checklist according to his watch list.