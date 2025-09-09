from flask import render_template, flash, redirect, url_for
from app import app
from app.form import ContactForm

@app.route("/", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        flash(f"Message sent successfully from {form.name.data}!", "success")
        return redirect(url_for("contact"))
    return render_template("contact.html", form=form)
