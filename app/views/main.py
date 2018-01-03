from flask import Blueprint, render_template

mod = Blueprint('main', __name__)

@mod.route('/', methods=['GET'])
def index():
  return "New Data"

@mod.route('/test', methods=['GET'])
def test():
  return render_template('main/test.html', 
    a_variable="This is my variable"
  )
