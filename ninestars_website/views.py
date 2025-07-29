from flask import render_template, request, flash, redirect, url_for
from flask_mail import Message
from ninestars_website import app, db, mail
from ninestars_website.models import ContactMessage
from datetime import datetime
from flask_babel import _

# Homepage
@app.route('/')
def index():
    return render_template(
        'home.html',  # Use your Bootstrap-based home.html
        title='Home',
        year=datetime.now().year
    )

# About Us Page
@app.route('/about')
def about():
    return render_template(
        'about.html',
        title='About Us',
        year=datetime.now().year
    )

# Contact Page
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Save to database
        new_msg = ContactMessage(name=name, email=email, message=message)
        db.session.add(new_msg)
        db.session.commit()

        # Send email
        msg = Message(
            subject=f"New Contact from {name}",
            sender=email,
            recipients=["your_email@gmail.com"],  # Replace with your email
            body=message
        )
        mail.send(msg)

        flash("Thank you! Your message has been sent.", "success")
        return redirect(url_for('contact'))

    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year
    )
