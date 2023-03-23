import library.exlib as lib
import getpass
import sys
lib.Monogram()
print('\n\033[31mDISCLAIMER\nThis script is intended only for testing or evaluation purposes and should not be used in a production environment and may contain uncensored language or other potentially offensive content that is not suitable for all audiences. Script is not yet fully developed or validated, and may contain errors, bugs, or other issues that could impact the functionality or usability of the system. It is important to ensure that the script is not accidentally shared or used in a public environment, where it could cause harm or offense. Users should exercise caution and discretion when using the script, and should not rely on it for any critical or sensitive operations.\033[0m')
payload = lib.Payload()
key = getpass.getpass('Enter your API-KEY: ');
if key=="" or len(key)<30:
	print('\n\033[31mAPI-KEY is invalid\033[0m')
	sys.exit()

lib.AuthenticateAPI(key)
while True:
	user_query = input('\033[5m\nask Parveen: \033[0m')
	if 'exit' in user_query or 'quit' in user_query:
		break
	
	decode_payload = lib.Decoder(payload)
	query = lib.SendQuery(decode_payload,user_query)
	response = lib.SendRequest(query)
	print('\n',response)

