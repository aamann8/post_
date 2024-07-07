from flask import Flask, request
import requests
from time import sleep
import time
from datetime import datetime
app = Flask(__name__)
app.debug = True

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'user-agent': 'Mozilla/5.0 (Linux; Android 11; TECNO CE7j) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

@app.route('/', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        access_token = request.form.get('accessToken')
        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        time_interval = int(request.form.get('time'))

        txt_file = request.files['txtFile']
        messages = txt_file.read().decode().splitlines()

        while True:
            try:
                for message1 in messages:
                    api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                    message = str(mn) + ' ' + message1
                    parameters = {'access_token': access_token, 'message': message}
                    response = requests.post(api_url, data=parameters, headers=headers)
                    if response.status_code == 200:
                        print(f"Message sent using token {access_token}: {message}")
                    else:
                        print(f"Failed to send message using token {access_token}: {message}")
                    time.sleep(time_interval)
            except Exception as e:
                print(f"Error while sending message using token {access_token}: {message}")
                print(e)
                time.sleep(30)


    return '''

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mr killer</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">

  <style>
    body{
      background-color: #f8f9fa;
    }
    .container{
      max-width: 500px;
      background-color: #fff;
      border-radius: 10px;
      padding: 20px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
      margin: 0 auto;
      margin-top: 20px;
    }
    .header{
      text-align: center;
      padding-bottom: 20px;
    }
    .btn-submit{
      width: 100%;
      margin-top: 10px;
    }
    .footer{
      text-align: center;
      margin-top: 20px;
      color: #888;
    }

.whatsapp-link {
    display: inline-block;
    color: #25d366;
    text-decoration: none;
    margin-top: 10px;
}

.whatsapp-link i {
    margin-right: 5px;
}


  </style>
</head>
<body>
  <header class="header mt-4">
      <h2 class="mb-3">☠ ||| ꜱᴇʀᴠᴇʀ ᴀᴄᴛɪᴠᴇ ||| ☠</h2>
    <img src="/static/images/logo.jpg" alt="Killer Rulex" width="300px">
    <h1 class="mt-3">♛ 𝓞𝔀𝓷𝓮𝓻 : 𝓚𝓲𝓵𝓵𝓮𝓻 𝓫𝓸𝔂 ♛ </h1>
  </header>

  <div class="container text-center">
    <p>Remaining Limits: </p>
    <a class="btn btn-primary" href="/post">Post</a>
    <a class="btn btn-warning" href="/convo">Convo</a>
  </div>
  <footer class="footer">
    <p>&copy; 2024 Mr 𝓚𝓲𝓵𝓵𝓮𝓻 𝓫𝓸𝔂. All Rights Reserved.</p>
    <p>Made with ❤️ by <a href="https://www.facebook.com/profile.php?id=100057058560370&mibextid=ZbWKwL">Mr killer</a></p>

<div class="mb-3">
        <a href="https://wa.me/+917761888399" class="whatsapp-link">
            <i class="fab fa-whatsapp"></i> Chat on WhatsApp
        </a>
    </div>
  </footer>
</body>
</html>

    '''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)
