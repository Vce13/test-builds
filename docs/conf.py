# Default settings
project = 'Test Builds'
extensions = [
    'sphinx_autorun',
    'notfound.extension',
    'hoverxref.extension',
    'sphinx_js',
    'sphinx_tabs.tabs',
    'sphinx_jinja2',
]

latex_engine = 'xelatex'  # allow us to build Unicode chars

autosectionlabel_prefix_document = True
hoverxref_auto_ref = True
hoverxref_roles = [
    'term',
]

# Include all your settings here
html_theme = 'insipid'

js_source_path = '../src/'
html_extra_path = ['static']
html_context = {
    "comment": "This comment is injected manually as a test.",
}

jinja2_env_kwargs = {
    "extensions": ["jinja2.ext.loopcontrols"],
}
