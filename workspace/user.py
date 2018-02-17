
class User:

	instance = None

	def __init__(self, login, senha):
		self.login = login
		self.senha = senha

	def get_instance(login=None, senha=None):
		if not instance:
			if login and senha:
				instance = User(login=login, senha=senha)

		return instance

	def __str__(self):
		json = {"login":self.login,"senha":self.senha}
		return json