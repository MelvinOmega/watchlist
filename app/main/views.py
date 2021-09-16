from ..request import get_news,get_articles
from flask import render_template,request,redirect,url_for, abort
from . import main
from flask_login import login_required
from ..models import Reviews, User
from .forms import ReviewForm,UpdateProfile
from .. import db
#Views
@main.route('/')
def index():
    """
    view root page function that returns the index page and its data
    """
    current_news = get_news()
    print(current_news)
    title = "Welcome to the Best News Website for latest and current news"
    return render_template('index.html', title= title, current_news = current_news )
@main.route("/news/<news_id>")
def articles(news_id):
    """
    view news page function that returns the news detail page and its data from a source
    """
    #get news based on source id
    articles = get_articles(news_id)
    print(articles)
    title = f'{news_id}'
    return render_template("articles.html", articles = articles, title = title)


@main.route('/movie/review/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_review(id):   

 @main.route('/user/<uname>')
 def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)   


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)




