import flask

import data_manager

app = flask.Flask(__name__)


@app.route("/")
def hello_to_flask():
    return flask.make_response("Hello", 200)


@app.route("/html", methods=["GET"])
def html_page():
    html = "<h1>Title of HTML</h1>"
    return html


# Please create a web application that connects to your AskMate database.
# Create endpoints with the following functionalities:
# listing all questions (optional: taking parameter for ordering)
@app.route("/questions/<string:orderby>", methods=["GET"])
def get_all_questions(orderby):
    result = data_manager.get_all_questions(orderby)
    return result


# listing all answers (optional: taking parameter for ordering)
@app.route("/answers/<string:orderby>", methods=["GET"])
def get_all_answers(orderby):
    result = data_manager.get_all_answers(orderby)
    return result


# listing all users
@app.route("/users", methods=["GET"])
def get_all_users():
    result = data_manager.get_all_users()
    return result


# get question by id
@app.route("/questions/<int:question_id>", methods=["GET"])
def get_question_by_id(question_id):
    result = data_manager.get_question_by_id(question_id)
    return result


# listing answers of a specific question
@app.route("/questions/<int:question_id>/answers", methods=["GET"])
def get_question_with_answers(question_id):
    result = data_manager.get_question_with_answers(question_id)
    return result

# listing questions that have more than x answers
# listing answers that are longer than x characters
# listing users with username, list of questions, list of answers


if __name__ == "__main__":
    app.run(debug=True)