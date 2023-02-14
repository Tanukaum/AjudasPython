from flask import Flask, render_template 

text_to_tile = 'Texto para o título'

#Cria aplicação flask
app = Flask(__name__)

@app.route('/')
def show_template():
    #title é o texto substituido no html
	return  render_template('index.html', title=text_to_tile)

#inicia a aplicação
if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=False)