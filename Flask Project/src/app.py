import os,mpld3,pandas as pd
from flask import Flask, render_template, request


app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


def func(file):
    df = pd.read_excel(file)
    df.groupby('CWL Name').count()['Employee Code'].plot.bar()
    mpld3.show()

# def analysis(filename):
#     x = pd.DataFrame(filename)
#     return render_template("analysis.html", name='May', data=x.to_html())

@app.route("/")
def index():
    return render_template("upload.html")


@app.route("/upload", methods=['POST'])
def upload():
    # target = os.path.join(APP_ROOT, 'excelFiles\\')
    # print(target)
    #
    # if not os.path.isdir(target):
    #     os.mkdir(target)

    for file in request.files.getlist("file"):
        return func(file)
        # print(file)
        # filename = file.filename
        # destination = "\\".join([target, filename])
        # print(destination)
        # file.save(destination)

    # return render_template("output.html")

if __name__ == "__main__":
    app.run(port=4555, debug=True)