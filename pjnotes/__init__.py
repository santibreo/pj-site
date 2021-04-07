import os

__version_info__ = (0, 0, 1)
__version__ = ".".join(map(str, __version_info__))

def get_path():
    """
    Shortcut for users whose theme is next to their conf.py.
    """
    # Theme directory is defined as our parent directory
    return os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def update_context(app, pagename, templatename, context, doctree):
    context["pjnotes_version"] = __version__


def setup(app):
    # add_html_theme is new in Sphinx 1.6+
    if hasattr(app, "add_html_theme"):
        theme_path = os.path.abspath(os.path.dirname(__file__))
        app.add_html_theme("pjnotes_theme", theme_path)
    #app.connect("html-page-context", update_context
    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True
    }
