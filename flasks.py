from flask import Flask, send_from_directory, render_template_string

app = Flask(__name__, static_folder="static")


@app.route("/")
def serve_html():
    with open("Page-2.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return render_template_string(html_content)

@app.route("/static/<path:filename>")
def serve_static_files(filename):
    return send_from_directory("static", filename)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
