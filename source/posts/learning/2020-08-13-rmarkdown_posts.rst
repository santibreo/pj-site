:draft: false
:date: 13-08-2020

======================
Rmarkdown (nice) posts
======================

In this post I am going to explain how I have prepared my Rmarkdown posts to
look exactly as the standard Markdown posts. It is not as straightforward as
you could suppose because Rmarkdown is becoming a framework fast, you need to
look the documentation for `blogdown <https://bookdown.org/yihui/blogdown/>`_,
`html sites <https://bookdown.org/yihui/rmarkdown/rmarkdown-site.html>`_ and
`bookdown <https://www.bookdown.org/>`_, and then find the logic that is hidden
behind.

Same TOC
--------

I love my nice-looking Table Of Contents which I have found in the Internet.
I had to make minimal changes in the javascript (I know no javascript) to make
that worm behave exactly as I want. Of course I have read the way of `dealing
with this suggested by Yihui <https://bookdown.org/yihui/blogdown/templates.html#how-to>`_,
and then, when I was thinking it was time to start writing, I watched that uggly
TOC that was added to my Rmarkdown posts, and I could not hold it. So I start
thinking about possible solutions:

1. [**FAIL**] - In Rmarkdown files the TOC is in an html tag with
   `id='toc'`. In the Markdown files I have absolute control of where it is
   going to appear, so I can just give in my css the same properties to both,
   the `.toc` class and the `#toc` id, and that was my first approach, but it
   did not work. The TOC created for Markdown files was inside a `nav` and the
   Rmarkdown one was not. Furthermore, the javascript worm is getting the
   `.toc` class, and I am not confortable making more and more changes in the
   javascript. So I leave this way back where I started.
2. [**FAIL**] - I was reading a lot of issues asking Yihui for the `toc_float` parameter
   support in blogdown, so I started feeling that a decent workaround should be
   somewhere. I found `this post <https://www.garrickadenbuie.com/blog/add-a-generated-table-of-contents-anywhere-in-rmarkdown/>`_
   talking about how to create the TOC anywhere inside your Rmarkdown file
   using and R function. I thought, *okey, I just have to edit the function,
   so it creates the html code instead of markdown*. I have some experience
   doing this kind of *hacking* (look [here](#toc_Nice-alerts)) so I accepted
   the challenge, but this attempt implies a high dependence on regular
   expressions, for which I have great appreciation, but I did not feel that I
   would have sufficient control over the input text to adopt this solution.
3. [**SUCCESS**] - The last solution gave me the idea of just getting the `h1`,
   `h2`, `h3`, `h4`, `h5` and `h6` tags of my html and create the TOC using
   javascript. I found it done somewhere so I have just taken it and used it.
   In a near future I should improve it because I have found it a bit
   intricate, but by this moment I was desperate so I just wanted a working
   solution.

   So, how does it work: I just use a different parameter
   (`with_toc`) to indicate if I want TOC or not. Then the mechanism is the
   same as it was when using the Hugo `.TableOfContents` approach (suggested
   for Markdown files) but calling a javascript function that creates the TOC
   list inside the corresponding `nav` tag. The `svg` tag that will become the
   worm is underneath so that's all, it works perfectly.


Nice alerts
-----------

One of the things that I missed the most in the standard markdown and makes
me document my code (when using `Sphinx <https://www.sphinx-doc.org/en/master/>`_)
with ReStructuredText is the nice alerts, notes and errors that you can put all
around. I find them really useful, and I can't understand how markdown is not
supporting this. As when I decided to build up this blog I was already a
regular Rmarkdown user, I solved this to have that alerts in the notes that I
am writting about everything I learn. So the solution is pure Rmarkdown.

The idea is pretty simple, create a R function that returns the text given as
input as html, inside the `divs` with the corresponding `alert` class. As
R has already a `message`, `warning`, and `stop` function, I will just adapt
them for my purpose. Here is the code that I have used:

.. code-block:: r
   :linenos:

    # Nice warnings, errors and messages
    knitr::knit_hooks$set(
        # To watch error use error=T and stop function
        error = function(x, options) {
            paste('\n\n<div class="alert alert-danger" style=>',
                  gsub('##', ' ',
                    gsub('^##\ Error in eval\\(expr, envir, enclos\\):',
                         '<i class="fas fa-skull"></i> **ERROR**: ', x)),
                  '</div>', sep = '\n')
        },
        # To watch warning use warning function
        warning = function(x, options) {
            paste('\n\n<div class="alert alert-warning">',
                  gsub('##', ' ',
                       gsub('^##\ Warning:', '<i class="fa fa-exclamation-triangle" aria-hidden="true"></i> **WARNING**: ', x)),
                  '</div>', sep = '\n')
        },
        # To watch message use message function
        message = function(x, options) {
            paste('\n\n<div class="alert alert-info">',
                  gsub('##', ' ',
                       gsub('^##\ ', '<i class="fas fa-comment-dots"></i> **INFO**: ', x)),
                  '</div>', sep = '\n')
        },
        class = function(before, options, envir) {
            if(before){
                sprintf("<div class = '%s'>", options$class)
            }else{
                "</div>"
            }
        }
    )

Of course, I am using the `font-awesome icons <https://fontawesome.com/icons?d=gallery>`_
only here, in my blogdown posts. For the standalone html created when you `knit`
your document I use Unicode symbos. You need to set the `stop` parameter of the
code chunk as `TRUE` to see the errors, and that's all. The final alerts look
like:

.. admonition:: Cannot show up
   :class: error

   This is what I am using now

Pictures
--------

The last function `class` in the code chunk is there because I use to add
pictures using R code, and when I do it, I want to be able to choose the html
`div` inside which they will be placed. So using the following code chunk:

.. code-block:: r

    include_graphics("/path/to/your/image.png")


With parameters `out.width = "70%", class = "center-pic"`, and having the
following class defined at my css:

.. code-block:: css

    .center-pic img {
        display: block;
        margin-left: auto;
        margin-right: auto;
        margin-bottom: 1.5rem;
    }

I can have nice looking and centered standalone images. Now I can set the
images exactly as I want, using css code, which gives you a lot a freedom.

And that's all, it could sound like not a big effort but for me, a beginner
with all this technologies, it was a bit challenging.
