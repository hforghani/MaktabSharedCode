class Story:
	stories = []

	def __init__(self, title):
		self.title = title
		Story.stories.append(self)


	@classmethod
	def search_title(cls, title):
		for story in Story.stories:
			if story.title == title:
				return story