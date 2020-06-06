import flask
import frss_utils as utils
import time

app = flask.Flask(__name__, template_folder='./rss_templates')

@app.route('/robots.txt', methods=["GET"])
def robots():
    return "User-agent: *\nDisallow: /fileserver"

@app.route('/fileserver', methods=["GET"])
def fs_info():
    return "File server is not avaliable to the public yet. (Staff please access :8000 after logging in).", 404

@app.route('/', methods=["GET"])
def index():
    return flask.render_template('index.html')

@app.route('/get_feed', methods=["POST"])
def get_feed():
    data = flask.request.json
    url    = data['url']
    method = data['method']
    body   = data['data']

    if not utils.validate_url(url):
        return flask.jsonify({'url': url, 'content': f'Invalid URL {flask.escape(url)}, valid domains are: {utils.validate_get_urls()}'}), 400

    content = utils.get_xml(method, url, body)
    if content is None:
        return flask.jsonify({'url': url, 'content': f'Failed to get URL {flask.escape(url)}'}), 500

    parsed = utils.parse_feed(content)
    if parsed is None:
        return flask.jsonify({'url': url, 'content': f'Failed to parse feed:' + flask.escape(content.decode()[:512])}), 500

    for item in parsed[2]:
        item['content'] = flask.Markup(item['content']).unescape()

    return flask.jsonify({
        'url': url,
        'content': flask.render_template('items.html', title=parsed[0], updated=parsed[1], items=parsed[2])
    })

if __name__ == '__main__':
    app.run(port=8001, host="0.0.0.0")
