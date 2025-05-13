from cryptography.fernet import Fernet
from Crypto.PublicKey import RSA
import os

class KeyManager:
	def __init__(self):
		self.key = None

	def symmetric_key(self):
		key = Fernet.generate_key()
		return key

	def create_asymmetric_key(self, key_size=1024):  # the default key size of one byte is being used
		base_key = RSA.generate(key_size)
		self.key = base_key

	@property
	def private_key(self):
		assert self.key, "No base key is found. Please call the create_asymmetric_key method before accessing private_key"
		return self.key.export_key()

	@property	
	def public_key(self):
		assert self.key, "No base key is found. Please call the create_asymmetric_key method before accessing public_key"
		return self.key.public_key().export_key()

	def save_private_key(self):
		private_key = self.private_key
		with open('private_key.pem', 'wb') as private_key_file:
			private_key_file.write(private_key)

	def save_public_key(self):
		public_key = self.public_key
		with open('public_key.pem', 'wb') as public_key_file:
			public_key_file.write(public_key)


