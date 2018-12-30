from urllib.parse import quote

from flask import Flask, request, render_template
# import builtins
from flask_bootstrap import Bootstrap
from flask_bootstrap import WebCDN

from util import read_database as r

app = Flask(__name__)

bootstrap = Bootstrap(app)
app.extensions['bootstrap']['cdns']['jquery'] = WebCDN(
    '//cdnjs.cloudflare.com/ajax/libs/jquery/4.6.0/'
)
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

end_result = []

app = Flask(__name__)
bootstrap = Bootstrap(app)
@app.route('/test')
def test():
    return render_template('SJR.html')

@app.route('/algo')
def algo():
    return render_template('algo.html')


@app.route('/paper?title=<title>/<int:rank>')
def success(title, rank=99):

    paperBean = end_result[rank]
    # print(paperBean)
    # print(request.args)
    # print(request.get_json())
    # print(end_result)
    title = quote(paperBean.title)
    print(type(paperBean.citations_name))

    refs = list(zip(paperBean.references_name,paperBean.references_url))
    cites = list(zip(paperBean.citations_name, paperBean.citations_url))

    print(refs)
    # print(refs[0][0])
    return render_template('details.html',
                           title=paperBean.title,
                           authors=paperBean.authors,
                           abstract=paperBean.abstract,
                           published_in=paperBean.published_in,
                           url=paperBean.url,
                           references=refs,
                           citations=cites,
                           citations_number=paperBean.citations_number,
                           rank=rank
                           )


@app.route('/')
def index():
    return render_template('SJR.html')


@app.route('/search', methods=['POST', 'GET'])
def search():
    global end_result
    if request.method == 'POST':
        keyword = request.form['keyword']
        rank = int(request.form['ranking'])
        print('keyword is:',keyword,rank)
        end_result = r.get_infomation(keyword=keyword, alpha=rank)
        # print(end_result[0].citations_number)
        return render_template('results.html', name=keyword, ranking=rank, papers=end_result)
    if request.method == 'GET':
        print(request.args.get('keyword'))
        keyword = request.args.get('keyword')
        rank = request.args.get('ranking')
        end_result = r.get_infomation(keyword=keyword, alpha=int(rank))
        return render_template('results.html', name=keyword, ranking=int(rank), papers=end_result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)
