from flask import Flask, request, render_template
from bean.Paper import *
from urllib.parse import quote
import builtins
from flask_bootstrap import Bootstrap
import read_database as r


# p1 = PaperBean(number=1, title="paper1", authors='Wentao1', published_in='Sustech1', url='localhost:5000',
#                abstract='this is the abstract of paper 1. this is the abstract of paper 1. this is the abstract of paper '
#                         '1. this is the abstract of paper 1. this is the abstract of paper 1.',
#                citations=[1,2], references=[3,4], citation_number=0)
# p2 = PaperBean(number=2, title="paper2", authors='Wentao2', published_in='Sustech2', url='localhost:5000',
#                abstract='this is the abstract of paper 2. this is the abstract of paper 2. this is the abstract of paper '
#                         '2. this is the abstract of paper 2. this is the abstract of paper 2. this is the abstract of paper'
#                         ' 2. this is the abstract of paper 2. this is the abstract of paper 2.',
#                citations=[1, 2], references=[3, 4],citation_number=0)
# p3 = PaperBean(number=3, title="paper3", authors='Wentao3', published_in='Sustech3', url='localhost:5000',
#                abstract='this is the abstract of paper 3. this is the abstract of paper 3. this is the abstract of paper '
#                         '3. this is the abstract of paper 3. this is the abstract of paper 3.',
#                citations=[1, 2], references=[3, 4],citation_number=0)
# p4 = PaperBean(number=4, title="paper4", authors='Wentao4', published_in='Sustech4', url='localhost:5000',
#                abstract='this is the abstract of paper 4. this is the abstract of paper 4. this is the abstract of paper '
#                         '4. this is the abstract of paper 4. this is the abstract of paper 4. this is the abstract of paper '
#                         '4. this is the abstract of paper 4. this is the abstract of paper 4.',
#                citations=[1, 2], references=[3, 4],citation_number=0)

end_result = dict()

app = Flask(__name__)

@app.route('/test')
def test():
    return render_template('base.html')

@app.route('/paper?title=<title>/<int:rank>')
def success(title, rank):

    paperBean = end_result[rank]
    # print(paperBean)
    # print(request.args)
    # print(request.get_json())
    title = quote(paperBean.title)
    # print(paperBean.citations)
    return render_template('temp.html',
                           title=paperBean.title,
                           authors=paperBean.authors,
                           abstract=paperBean.abstract,
                           published_in=paperBean.published_in,
                           url=paperBean.url,
                           references=paperBean.citations,
                           citations=paperBean.references,
                           rank=rank
                           )


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['POST', 'GET'])
def search():
    global end_result
    if request.method == 'POST':
        keyword = request.form['keyword']
        rank = int(request.form['ranking'])
        end_result = r.get_infomation(keyword=keyword, alpha=rank)
        # print(end_result)
        return render_template('results.html', name=keyword, ranking=rank, papers=end_result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)
