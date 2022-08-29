import os
import requests
import base64

def generate(prompt): # using craiyon ia private api
    req = requests.post('https://backend.craiyon.com/generate', json={"prompt": str(prompt)})
    with open("result.png", "wb") as fh:
        fh.write(base64.b64decode(req.json()['images'][0]))

def main(): # main system
    p = input('What you want to draw? ')
    print('\n[AI] Drawing Your Image...')
    generate(p)
    print('\n[AI] Your image has been drawed!')
    print('\n[AI] Opening result file...')
    os.system('start result.png')
    print('\n[AI] File opened !')
    print('[SYS] This tool was made by yux#9751, using craiyon.com AI')
    input('')
    os.system('cls')
    main()

main() # starting program
