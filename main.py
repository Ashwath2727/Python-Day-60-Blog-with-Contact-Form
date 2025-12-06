from flask import Flask, render_template, request
import requests
from mail import Mail

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/00b23b65247a891e7d9e").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        form_data = request.form

        # print(form_data.get("name"))
        # print(form_data.get("email"))
        # print(form_data.get("phone"))
        # print(form_data.get("message"))

        final_msg = (f"Name: {form_data.get("name")}\n"
                     f"Email: {form_data.get("email")}\n"
                     f"Phone: {form_data.get("phone")}\n"
                     f"Message: {form_data.get("message")}")

        mail = Mail(form_data.get("email"), final_msg)
        mail.send_mail()

        return render_template("contact.html", msg_sent=True)

    return render_template("contact.html", msg_sent=False)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

# @app.route("/form-entry", methods=["POST"])
# def receive_data():
#     form_data = request.form
#
#     print(form_data.get("name"))
#     print(form_data.get("email"))
#     print(form_data.get("phone"))
#     print(form_data.get("message"))
#
#     return "<h1>Successfully sent your message</h1>"

if __name__ == "__main__":
    app.run(debug=True, port=5001)
