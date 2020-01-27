"""Create form logic."""
from wtforms import (Form,
                     StringField,
                     SelectField,
                     PasswordField,
                     SubmitField)
from wtforms.validators import (DataRequired,
                                Email,
                                EqualTo,
                                Length,
                                Optional)


class SignupForm(Form):
    """User Signup Form."""

    name = StringField('Name',
                       validators=[DataRequired(message=('Enter a fake name or something.'))])
    email = StringField('Email',
                        validators=[Length(min=6, message=('Please enter a valid email address.')),
                                    Email(message=('Please enter a valid email address.')),
                                    DataRequired(message=('Please enter a valid email address.'))])
    password = PasswordField('Password',
                             validators=[DataRequired(message='Please enter a password.'),
                                         Length(min=6, message=('Please select a stronger password.')),
                                         EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Confirm Your Password', )
    website = StringField('Website',
                          validators=[Optional()])
    submit = SubmitField('Register')


class LoginForm(Form):
    """User Login Form."""

    email = StringField('Email', validators=[DataRequired('Please enter a valid email address.'),
                                             Email('Please enter a valid email address.')])
    password = PasswordField('Password', validators=[DataRequired('Uhh, your password tho?')])
    submit = SubmitField('Log In')


class MushroomForm(Form):
    cap_shape = SelectField(u'Enter cap shape', choices=[('b', 'bell'), ('c', 'conical')
        , ('x', 'convex'), ('f', 'flat')
        , ('k', 'knobbed'), ('s', 'sunken')
                                                         ])

    cap_surface = SelectField(u'Enter cap surface', choices=[('f', 'fibrous'), ('g', 'grooves')
        , ('scaly', 'y'), ('s', 'smooth')
                                                             ])

    cap_color = SelectField(u'Enter cap color', choices=[('n', 'brown'), ('b', 'buff')
        , ('c', 'cinnamon'), ('g', 'gray')
        , ('p', 'pink'), ('u', 'purple')
        , ('e', 'red'), ('w', 'white')
        , ('y', 'yellow'), ('r', 'green')
                                                         ])

    bruises = SelectField(u'Enter bruises', choices=[('t', 'bruises'), ('f', 'no')])
    odor = SelectField(u'Enter odor', choices=[('a', 'almond'), ('l', 'anise')
        , ('c', 'creosote'), ('y', 'fishy')
        , ('f', 'foul'), ('m', 'musty')
        , ('n', 'none'), ('p', 'pungent')
        , ('s', 'spicy')
                                               ])

    gill_attachment = SelectField(u'Enter gill attachment', choices=[('a', 'attached'), ('d', 'descending')
        , ('f', 'free'), ('n', 'notched')
                                                                     ])

    gill_spacing = SelectField(u'Enter gill spacing', choices=[('c', 'close'), ('w', 'crowded')
        , ('d', 'distant')
                                                               ])

    gill_size = SelectField(u'Enter gill size', choices=[('b', 'broad'), ('n', 'narrow')
                                                         ])

    gill_color = SelectField(u'Enter gill color', choices=[('n', 'brown'), ('k', 'black')
        , ('h', 'chocolate'), ('g', 'gray')
        , ('r', 'green'), ('o', 'orange')
        , ('p', 'pink'), ('u', 'purple')
        , ('e', 'red'), ('w', 'white')
        , ('y', 'yellow')
                                                           ])

    stalk_shape = SelectField(u'Enter stalk shape', choices=[('e', 'enlarging'), ('t', 'tapering')])

    stalk_root = SelectField(u'Enter stalk root', choices=[('b', 'bulbous'), ('c', 'club')
        , ('u', 'cup'), ('e', 'equal')
        , ('r', 'green'), ('o', 'orange')
        , ('z', 'rhizomorphs'), ('r', 'rooted')
        , ('?', 'missing')
                                                           ])

    stalk_surface_above_ring = SelectField(u'Enter stalk surface above ring', choices=[('f', 'fibrous'), ('y', 'scaly')
        , ('k', 'zilky'), ('s', 'smooth')
                                                                                  ])

    stalk_surface_below_ring = SelectField(u'Enter stalk surface below ring', choices=[('f', 'fibrous'), ('y', 'scaly')
        , ('k', 'zilky'), ('s', 'smooth')
                                                                                  ])

    stalk_color_above_ring = SelectField(u'Enter stalk color above ring', choices=[('n', 'brown'), ('b', 'buff')
        , ('c', 'cinnamon'), ('g', 'gray')
        , ('p', 'pink'), ('u', 'purple')
        , ('e', 'red'), ('w', 'white')
        , ('y', 'yellow')
                                                                              ])

    stalk_color_below_ring = SelectField(u'Enter stalk color below ring', choices=[('n', 'brown'), ('b', 'buff')
        , ('c', 'cinnamon'), ('g', 'gray')
        , ('p', 'pink'), ('u', 'purple')
        , ('e', 'red'), ('w', 'white')
        , ('y', 'yellow')
                                                                              ])

    veil_type = SelectField(u'Enter veil type', choices=[('p', 'partial'), ('u', 'universal')])

    veil_color = SelectField(u'Enter veil color', choices=[('n', 'brown'), ('o', 'orange')
        , ('w', 'white'), ('y', 'yellow')])

    ring_number = SelectField(u'Enter ring number', choices=[('n', 'none'), ('o', 'one')
        , ('t', 'two')])

    ring_type = SelectField(u'Enter ring type', choices=[('n', 'none'), ('o', 'one')
        , ('e', 'evanescent'), ('c', 'cobwebby')
        , ('f', 'flaring'), ('l', 'large')
        , ('n', 'none'), ('p', 'pendant')
        , ('s', 'sheating'), ('z', 'zone')
                                                                              ])

    spore_print_color = SelectField(u'Enter spore print color', choices=[('n', 'brown'), ('k', 'black')
        , ('h', 'chocolate'), ('b', 'buff')
        , ('r', 'green'), ('o', 'orange')
        ,('w', 'white'), ('y', 'yellow')
                                                                         ])

    population = SelectField(u'Enter population', choices=[('a', 'abundant'), ('c', 'clustered')
        , ('n', 'numerous'), ('s', 'scattered')
        , ('v', 'several'), ('y', 'solitary')
                                                                        ])

    habitat = SelectField(u'Enter habitat', choices=[('g', 'grasses'), ('l', 'leaves')
        , ('m', 'meadows'), ('p', 'paths')
        , ('u', 'urban'), ('w', 'waste')
        , ('d', 'woods')
                                                                        ])

    submit = SubmitField('Submit')
