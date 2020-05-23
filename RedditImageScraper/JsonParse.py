##########################################
# These two classes process JSON data from
# reddit. Reddit uses an infinite-scrolling
# interface. The initial page load returns
# different JSON than the subsequent reloads.
# One class deals with the first load, while
# the other deals with the reloads.
###########################################

class JsonParser:
	def __init__(self, json_data):
		self.json_data = json_data
		self.post_id_dictionary = {}
	
	def getPosts(self):
		"""Grabs reddit 'posts' from Json, removes non-image
		posts and returns them.
		"""
		
		post_container = self.json_data['posts']
		
		posts = [p for p in post_container.values()
					if len(p['id']) <= 9					# Remove Ads,
					and p['media'] != None
					and p['media']['type'] == 'image'		# and non-image posts
					and p['id'] not in id_dict]				# no duplicates
		
		return posts

class JsonParserFirst(JsonParser):
	def __init__(self, json_data):
		super().__init__(self)
		self.json_data = json_data
		self.post_id_dictionary = {}
	
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
	
	def returnIDs(self):
		return post_id_dictionary
	
	def getPostData(self, json_post):
		
		post_info = json_post['data']
		
		upvotes = post_info['score']
		title = post_info['title']
		total_awards_received = post_info['total_awards_received']
		num_comments = post_info['num_comments']
	
	