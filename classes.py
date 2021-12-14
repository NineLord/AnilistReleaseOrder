import traceback
from typing import Union

class FuzzyDate(object):
	def __init__(self, year: Union[None, int], month: Union[None, int], day: Union[None, int]) -> None:
		self.year = year
		self.month = month
		self.day = day
	
	# self >  other return positive int
	# self == other return 0
	# self <  other return negativ int
	def _compare(self, other) -> int:
		if not isinstance(other, type(self)):
			print("FuzzyDate::_compare : incorrect types:", type(other))
			exit()
		if self.year == None or other.year == None:
			if self.year == None and other.year == None:
				return 0
			elif self.year == None:
				return 1
			else:
				return -1
		else:
			year = self.year - other.year
			if year != 0:
				return year
			else:
				if self.month == None or other.month == None:
					if self.month == None and other.month == None:
						return 0
					elif self.month == None:
						return 1
					else:
						return -1
				else:
					month = self.month - other.month
					if month != 0:
						return month
					else:
						if self.day == None or other.day == None:
							if self.day == None and other.day == None:
								return 0
							elif self.day == None:
								return 1
							else:
								return -1
						else:
							return self.day - other.day

	def __lt__(self, other) -> bool:
		return self._compare(other) < 0

	def __le__(self, other) -> bool:
		return self._compare(other) <= 0

	def __eq__(self, other) -> bool:
		return self._compare(other) == 0

	def __ge__(self, other) -> bool:
		return self._compare(other) >= 0

	def __gt__(self, other) -> bool:
		return self._compare(other) > 0

	def __ne__(self, other) -> bool:
		return self._compare(other) != 0

	def __str__(self) -> str:
		try:
			return '/'.join(["?" if self.day == None else str(self.day), "?" if self.month == None else str(self.month), "?" if self.year == None else str(self.year)])
		except TypeError:
			print("FuzzyDate::__str__")
			exit()

class ShowData(object):
	def __init__(self, id: int, title: str, format: str, date: FuzzyDate, siteUrl: str) -> None:
		self.id = id
		self.title = title
		self.format = format
		self.date = date
		self.siteUrl = siteUrl
	
	def __hash__(self) -> int:
		return hash(self.id)

	def __eq__(self, other) -> bool:
		if not isinstance(other, type(self)):
			return False
		else:
			return self.id == other.id
	
	def formatOutput(self, template: str, index: int) -> str:
		return template.format("[?]", str(index), str(self.id), self.format, str(self.date), self.siteUrl, self.title) # TODO: change [?] to check the user's watch list, and mark V if he watched.
	
	def __str__(self) -> str:
		try:
			return ''.join(["{id=", str(self.id), ", title=\"", self.title, "\", format=\"", self.format, "\", date=", str(self.date), ", siteUrl=\"", self.siteUrl, "\"}"])
		except TypeError:
			print("ShowData::__str__ : type error at", str(self.id))
			print(traceback.format_exc())
			exit()
