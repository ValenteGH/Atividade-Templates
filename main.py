from flask import Flask, render_template
app = Flask('app')

@app.route('/')
def meutemplate():
  return render_template('meutemplate.html')
@app.route('/unifran')
def unifran():
  return render_template('unifran.html')
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)