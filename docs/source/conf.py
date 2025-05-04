# Configuration file for the Sphinx documentation builder.
# Using Certora Documentation Infrastructure.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


# -- docsinfra imports -------------------------------------------------------
# NOTE: requires docsinfra installed
from docsinfra.sphinx_utils import TAGS, CVL2Lexer

# -- Dev build ---------------------------------------------------------------
# The following sets this as a "dev build", which will include TODO and othe comments.
# See:
# https://certora-docs-infrastructure.readthedocs-hosted.com/en/latest/showcase/comments_todos.html
# tags.add(TAGS.is_dev_build)  # noqa: F821


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Certora Coinbase training"
copyright = "2025, Certora, Inc"
author = "Certora, Inc"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
extensions = [
    "sphinx.ext.graphviz",
    "sphinx.ext.todo",
    "sphinxcontrib.video",
    "sphinxcontrib.youtube",
    "sphinx_design",
    "sphinxarg.ext",
    "sphinxcontrib.spelling",
    # docsinfra extenstions
    "docsinfra.sphinx_utils.codelink_extension",
    "docsinfra.sphinx_utils.includecvl",
]

templates_path = ["_templates"]
exclude_patterns = []

language = "en"


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_theme = "furo"
html_static_path = ["_static"]

# A shorter “title” for the HTML docs.
# This is used for links in the header and in the HTML Help docs.
# Defaults to the value of html_title.
# html_short_title = project

# The html_title also appears in the side-bar, different title to indicate dev-build.
html_title = (
    f"{project} - Development" if tags.has(TAGS.is_dev_build) else project  # noqa: F821
)


# -- themes customizations -----------------------------------------------------
if html_theme == "furo":
    html_theme_options = {
        "light_logo": "Certora_Logo_Black.svg",
        "dark_logo": "Certora_Logo_White.svg",
        # Disable the edit button, see:
        # https://pradyunsg.me/furo/customisation/top-of-page-buttons/#disabling-on-read-the-docs
        "top_of_page_buttons": [],
    }
else:
    html_logo = "_static/Certora_Logo_Black.svg"


# -- prologue ----------------------------------------------------------------
# A string of reStructuredText that will be included at the beginning of every source
# file that is read.
# Here we use the prologue to add inline cvl code and solidity code.
rst_prolog = """
.. role:: cvl(code)
   :language: cvl

.. role:: solidity(code)
   :language: solidity
"""


# -- codelink_extension configuration ----------------------------------------
link_to_github = True
path_remappings = {
    "@lesson1": "../../training-examples/lesson1",
    "@lesson2": "../../training-examples/lesson2",
    "@lesson3": "../../training-examples/lesson3",
    "@lesson5": "../../training-examples/lesson5",
    "@lesson6": "../../training-examples/lesson6",
    "@ERC20": "../../training-examples/ERC20",
    "@evc": "../../training-examples/ethereum-vault-connector/src",
    "@set": "../../training-examples/set/",
}


# -- Options for todo extension ----------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/todo.html#configuration
# Show todo only in dev-build
todo_include_todos = tags.has(TAGS.is_dev_build)  # noqa: F821


# -- spelling configuration --------------------------------------------------
# See https://sphinxcontrib-spelling.readthedocs.io/en/latest/customize.html
spelling_lang = "en_US"
spelling_word_list_filename = "spelling_wordlist.txt"

# In sphinxcontrib.spelling 8.0.0 when spelling_ignore_contributor_names is True it
# DOES scan git log for contributor names to add them to list of correct spelling.
# This results in a warning when not working over a git repository.
spelling_ignore_contributor_names = False


# -- graphviz configuration --------------------------------------------------
# See https://www.sphinx-doc.org/en/master/usage/extensions/graphviz.html
graphviz_output_format = "svg"  # Supports hover and links
# For links, add ``target``, e.g. ``target="_blank"``.
# See https://www.w3.org/TR/html401/types.html#type-frame-target for ``target`` options


# -- add CVL syntax highlighting ---------------------------------------------
def setup(sphinx):
    sphinx.add_lexer("cvl", CVL2Lexer)
