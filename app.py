import flask from flask

@app.route('/'), methods = ('GET')
def test():
    return render_templates(index.html)

