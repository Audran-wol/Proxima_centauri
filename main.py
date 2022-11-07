from flask import Flask, render_template, request
import requests
import smtplib
app = Flask(__name__)

my_email = "gimanboom@gmail.com"
my_password = "653116180"
url = "https://api.npoint.io/dccb57eb82214ce1b1ca"
response = requests.get(url)
post = response.json()


@app.route("/")
def get_all_post():
    return render_template("index.html", all_post=post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == 'POST':
        data = request.form
        send_email(data["username"], data["email"], data["phone_number"], data["message"])
        return render_template("contact.html", msg_send=True)
    return render_template("contact.html", msg_send=False)


def send_email(username, email, phone_number, message):
    email_message = f"Subject:New Message\n\nName: {username}\nEmail: {email}\nPhone: {phone_number}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs="audranwolfhards@gmail.com", msg=email_message)


@app.route("/post/<int:index>")
def show_post(index):
    request_post = None
    for blog_post in post:
        if post["id"] == index:
            request_post = blog_post
    return render_template("post.html", post=request_post)


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port="5000")

