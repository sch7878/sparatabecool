import flask from flask

@app.route('/'), methods = ('GET')
def test():
    return render_templates(index.html)

@app.route('/'), methods = ('POST')
def test_post():
    test_receive = list(db.test.find({'value':value},{'_id':False}))
    return render_templates(index.html)

