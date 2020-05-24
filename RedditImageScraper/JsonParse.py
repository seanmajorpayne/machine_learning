##########################################
# These two classes process JSON data from
# reddit. Reddit uses an infinite-scrolling
# interface. The initial page load returns
# different JSON than the subsequent reloads.
# One class deals with the first load, while
# the other deals with the reloads.
###########################################

class JsonParser:
	def __init__(self, json_data, id_dict={}):
		self.json_data = json_data
		self.post_id_dictionary = {}
		self.id_dict = id_dict
	
	def getPosts(self):
		"""Grabs reddit 'posts' from Json, removes non-image
		posts and returns them.
		"""
		
		post_container = self.json_data['posts']
		
		posts = [p for p in post_container.values()
					if len(p['id']) <= 9					# Remove Ads,
					and p['media'] != None
					and p['media']['type'] == 'image'		# and non-image posts
					and p['id'] not in self.id_dict]		# no duplicates
		
		return posts
	
	def getUpvotes(self, json_post):
		"""Returns the upvote count for a given post"""
		return json_post['score']
	
	def getURL(self, json_post):
		"""Returns the URL for a given post"""
		return json_post['media']['content']
	
	def getId(self, json_post):
		"""Returns an ID for a given post"""
		return json_post['id']
		


class JsonParserFirst(JsonParser):
	def __init__(self, json_data, id_dict={}):
		super().__init__(self)
		self.json_data = json_data
		self.id_dict = id_dict
	
	def getPosts(self):
		"""
		Grabs reddit 'posts' from Json, removes non-image
		posts and returns them.
		"""
		
		post_container = self.json_data['data']['children']
		
		posts = [p for p in post_container
			if len(p['data']['name']) <= 9					# Remove Ads,
			and p['data']['post_hint'] == 'image']			# and non-image posts
		
		return posts
	
	def getUpvotes(self, json_post):
		upvotes = json_post['data']['score']
		return upvotes
	
	def getURL(self, json_post):
		url = json_post['data']['url']
		return url
	
	def getId(self, json_post):
		id = json_post['data']['name']
		return id
	
	