class Story:
	stories = []

	def __init__(self, title):
		self.title = title
		Story.stories.append(self)



class StoryManager:
	def __init__(self):
		self.stories = []

	def add(self, story):
		self.stories.append(story)

	def search_title(self, title):
		for story in self.stories:
			if story.title == title:
				return story

if __name__ == "__main__":
	manager = StoryManager()
	manager.add(Story("How to code"))
	manager.add(Story("Python is Good!"))
	story = manager.search_title("How to code")
	print(story.title)