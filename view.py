from flask import Flask, request, render_template
from bean.Paper import Paper
app = Flask(__name__)
p1 = Paper(title= "paper1", authors='Wentao1', public_in='Sustech1', data='aaaaaaaa', url='localhost:5000',
                 abstract='this is the abstract of paper 1. this is the abstract of paper 1. this is the abstract of paper 1. this is the abstract of paper 1. this is the abstract of paper 1.', citations=[Paper(),Paper(),Paper()], references=[Paper(),Paper()])
p2 = Paper(title= "paper2", authors='Wentao2', public_in='Sustech2', data='aaaaaaaa', url='localhost:5000',
                 abstract='this is the abstract of paper 2. this is the abstract of paper 2. this is the abstract of paper 2. this is the abstract of paper 2. this is the abstract of paper 2. this is the abstract of paper 2. this is the abstract of paper 2. this is the abstract of paper 2.', citations=[Paper(),Paper(),Paper(), Paper()], references=[Paper(),Paper()])
p3 = Paper(title= "paper3", authors='Wentao3', public_in='Sustech3', data='aaaaaaaa', url='localhost:5000',
                 abstract='this is the abstract of paper 3. this is the abstract of paper 3. this is the abstract of paper 3. this is the abstract of paper 3. this is the abstract of paper 3.', citations=[Paper(),Paper(),Paper()], references=[Paper(),Paper()])
p4 = Paper(title= "paper4", authors='Wentao4', public_in='Sustech4', data='aaaaaaaa', url='localhost:5000',
                 abstract='this is the abstract of paper 4. this is the abstract of paper 4. this is the abstract of paper 4. this is the abstract of paper 4. this is the abstract of paper 4. this is the abstract of paper 4. this is the abstract of paper 4. this is the abstract of paper 4.', citations=[Paper(),Paper(),Paper(), Paper()], references=[Paper(),Paper()])
end_result = {1: p1, 2: p2, 3: p3, 4: p4}

@app.route('/paper/<name>')
def success(paperBean):
    paperBean.
    return 'welcome %s' % name


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/search',methods = ['POST', 'GET'])
def search():
    if request.method == 'POST':
        keyword = request.form['keyword']
        rank = request.form['ranking']
        return render_template('results.html', name = keyword, ranking= rank, papers = end_result)


if __name__ == '__main__':
    app.run(debug = True)