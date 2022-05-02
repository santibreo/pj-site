Latex tutorial
==============

Just a summit of `this latex tutorial <https://riptutorial.com/es/latex>`_, with the main ideas I do not want to forget.

Bibliography
------------

Latex make the bibliography management really simple. You should have a `.bib` file full of entries like this one:

.. code:: latex
   @inproceedings{citation_name,
     title={Paper Title},
     author={List Authors},
     pages={45--48},
     year={2013},
     organization={organization name}
   }

And then make your document look something like this:

.. code:: latex
   \usepackage[style=ieetr, backend=biber]{biblatex}

   \begin{document}
   Here I need to cite my favourite article \cite{citation_name}. And that's all.
   \printbibliography
   \end{document}


Then you have to compile your document one first time. Run the command ``biber your_document_name_with_no_extension`` and then re-compile it. That's all.

Presentations
-------------

**Latex** is well suited to make presentations but I won't cover how here. If you want to use it for this purpose you can follow `this tutorial <https://www.overleaf.com/learn/latex/Beamer>`_.

Bucles
------

.. warning::
  If we use commands with an `@` in its name we have to use it between ``\makeatletter` - `\makeatother``. The right way: ``\makeatletter\def\is#1#2{\@ifstar{#1}{#2}}\makeatother``

**Latex** allow us to create loops, but not as sophisticated as other programming languages.

@for
****

.. code:: latex
   \makeatletter
   \@for\sun:={rising,setting}\do{The sun is \sun.}
   \makeatother


It creates the following text: *The sun is rising.The sun is setting*.

@whilenum
*********

.. code:: latex
   \makeatletter
   \newcounter{int}
   \@whilenum\value{int}<10\do
   {\stepcounter{int}\ifthenelse{\isodd{\value{int}}}{\theint}{}}
   \makeatother

You need to add ``\usepackage{ifthen}`` in the header to make this work. It creates the following text: *1 3 5 7 9*.


