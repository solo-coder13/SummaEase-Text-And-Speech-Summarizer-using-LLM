from flask import Flask, request, render_template

app=Flask(__name__)

# routes
@app.route('/')

def index():
    return render_template('index.html')

@app.route('/summarize_text', methods=['POST','GET'])
def summ_text():
    pass

@app.route('/summarize_file', methods=['POST','GET'])
def summ_file():
    pass

@app.route('/summarize_audio_file', methods=['POST','GET'])
def summ_audio():
    pass


if __name__ == '__main__':
    app.run(debug=True)