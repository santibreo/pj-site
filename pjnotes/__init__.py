import os
from docutils.parsers.rst import Directive, directives
from pjnotes.posts import (
    Posts,
    PostsDirective,
    process_posts_nodes,
    visit_Posts_node,
    depart_Posts_node
)

__version_info__ = (1, 0, 0)
__version__ = ".".join(map(str, __version_info__))


def get_path():
    """
    Shortcut for users whose theme is next to their conf.py.
    """
    # Theme directory is defined as our parent directory
    return os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def update_context(app, pagename, templatename, context, doctree):
    """
    Includes `pjnotes_version` in the context
    """
    context["pjnotes_version"] = __version__


def setup(app):
    # add_html_theme is new in Sphinx 1.6+
    if hasattr(app, "add_html_theme"):
        theme_path = os.path.abspath(os.path.dirname(__file__))
        app.add_html_theme("pjnotes_theme", theme_path)
    app.add_node(
        Posts,
        html=(visit_Posts_node, depart_Posts_node),
    )
    app.add_directive('posts', PostsDirective, override=True)
    app.connect("html-page-context", update_context)
    app.connect("doctree-resolved", process_posts_nodes)
    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True
    }
