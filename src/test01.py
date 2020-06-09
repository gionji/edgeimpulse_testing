# Install requests via: `pip3 install requests`

# got from Project dashboard
API_KEY = 'ei_5d60c246c831b7939ba2dd768ebd3996d22601587bd576ec08de9890ad8c0fd4'

with open('somefile.cbor', 'r') as file:
    res = requests.post(url='https://ingestion.edgeimpulse.com/api/training/data',
                        data=file,
                        headers={
                            'Content-Type': 'application/cbor',
                            'x-file-name': 'idle.01',
                            'x-label': 'idle',
                            'x-api-key': API_KEY
                        })

    if (res.status_code == 200):
        print('Uploaded file to Edge Impulse', res.status_code, res.content)
    else:
        print('Failed to upload file to Edge Impulse', res.status_code, res.content)
