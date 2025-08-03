from flask import Flask

app = Flask(__name__)

@app.route("/nana")
def home():
    return "🌸 Hai cayang! Website ini aktif 24 jam."

@app.route("/surat")
def surat():
    return """
    <html>
        <head><title>Surat nana</title></head>
        <body style='font-family: sans-serif; text-align: center; padding: 40px;'>
            <h1>💌 Untuk rere hahan</h1>
            <p>maaf yaa buat semuanya.</p>
            <p><strong> jangam lupa mam🥺</strong></p>
            <img src="https://i.pinimg.com/originals/0e/3f/65/0e3f652cd4d8f3b9ae7aa60a23c460d6.gif" width="300"/>
            <p>Dari: Raihan</p>
        </body>
    </html>
    """ 

    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=5000)
