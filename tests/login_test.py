#from app import auth
#from app.auth import login
#from app.db import db
#from app.db.models import User
#from app.auth.forms import login_form

#def test_login(application):
    #with application.app_context():


        #assert db.session.query(User).count() == 0
        #user = User('keith@webizly.com', 'testtest', is_admin=1)
        #db.session.add(user)

        #assert user.email == 'keith@webizly.com'
        #db.session.commit()
        #assert db.session.query(User).count() == 1

        #form = login_form()
        #user = User.query.filter_by(email=form.email.data).first()
        #assert current_user.is_authenticated