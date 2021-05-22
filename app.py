from flask import Flask

app=Flask(__name__)
ans=str('')
@app.route('/')
def hello():
    return 'Hello world'

@app.route('/<string:s>',methods=['GET'])
def concat(s):
    global ans
    ans=ans+s
    return s +'\nsubmitted view it at <a href="/result">clickme</a>'
@app.route('/result')
def result():
    return str(ans)


if __name__=='__main__':
    app.run()