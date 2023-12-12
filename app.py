from datetime import datetime
from flask import Flask, render_template, flash, redirect, session, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_babel import Babel, _

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu_clave_secreta'
babel = Babel()

# Configuración de Babel
# app.config['BABEL_DEFAULT_LOCALE'] = 'es'
app.config['LANGUAGES'] = ['en', 'es']

def get_locale():
    print(request.accept_languages.best_match(app.config['LANGUAGES']))
    return session.get('language', request.accept_languages.best_match(app.config['LANGUAGES']))


babel.init_app(app, locale_selector=get_locale)

class MyForm(FlaskForm):
    name = StringField(_('Name'), validators=[DataRequired()])
    submit = SubmitField(_('Submit'))

# Rutas
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = MyForm()
    if form.validate_on_submit():
        flash(_('Form submitted successfully!'), 'success')
        return redirect(url_for('home'))
    return render_template('form.html', form=form)

@app.route('/set_language/<language>')
def set_language(language):
    # Validar que el idioma sea uno de los idiomas admitidos
    if language in app.config['LANGUAGES']:
        # Guardar el idioma en la sesión
        session['language'] = language
        print(language)
    return redirect(request.referrer or url_for('home'))

@app.route('/date')
def date():
    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render_template('date.html', current_date=current_date)

@app.route('/error')
def error():
    return render_template('error.html')

@app.route('/items')
def items():
    num_items = 5  # Puedes obtener este valor de tu base de datos o de cualquier fuente de datos
    return render_template('items.html', num_items=num_items)

@app.route('/number')
def number():
    formatted_number = 12345.6789  # Puedes obtener este número de tu base de datos o de cualquier fuente de datos
    return render_template('number.html', formatted_number=formatted_number)


if __name__ == '__main__':
    app.run(debug=True)
