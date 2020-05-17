class Food():
	def __init__(self):
		self.x = screen_width / 2
		self.y = screen_height / 4
		self.color = red
		self.width = 10
		self.height = 10

	def draw_food(self,surface):
		self.food = pg.Rect(self.x,self.y,self.width,self.height)
		pg.draw.rect(surface,self.color,self.food)

	def is_eaten(self,head):
		return self.food.colliderect(head)

	def new_pos(self):
		self.x = random.randint(0,screen_width-self.width)
		self.y = random.randint(0,screen_height-self.height)