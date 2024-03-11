# Web Applications in Python with Flask

This guide will show you how to create and structure a basic Flask application, including HTML rendering, CSS linking, and data processing with Jinja.

## Introduction to Flask

Flask a is "framework" for creating web applications by writing Python code.

In software development, a framework is generally an idea about how to best write some kind of program and a set of tools (e.g. scripts, functions, server, IDE) that help turn this idea into well-organized code.

A web application is a website with more flexibility, interactivity, or continuity. Specifically, while we can think of a website as a set of predefined HTML files, a web application can use control structures (e.g. "if" statements, "for" loops, etc.) to produce "made to order" HTML files which may vary between users. Generating HTML files in this way gives users numerous benefits, including the ability to "log in to" a web application and interact with previously saved or personalized content.

## Set Up and Basic Routing

Let's make a basic web application.

First, make sure you are familiar with virtual environments in Python. Follow [this guide](https://canvas.uw.edu/courses/1699981/pages/managing-external-modules-in-your-python-projects?wrap=1) if you need a refresher. Make sure you pass the "Make sure that it worked" step before proceeding.

if you create a new project in PyCharm and set "Location" of both the project and its virtual environment to be the same filepath, your starting file structure should resemble the figure below.

```
├── bin
├── lib
├── pyvenv.cfg
```

> NOTE: **Your virtual environment folder and Flask code do not _need to_ be in the same directory!** Don't worry too much if your folder does not match the one above. Remember, a virtual environment is a "mode" that tells Python where to look for certain files, like modules. This information can "follow you around" as you move through your file system. Hence you can "turn on" a virtual environment in one folder, navigate to another folder, and, so long as the virtual environment is still "on," still access modules and run installed commands from the new location.

> NOTE: If you create your virtual environment through the `venv` command or through VS Code, your starting directory structure will look different. Running `python3 -m venv <name-of-env>` will make a directory called `<name-of-env>` at the filepath where you ran the command. Creating a virtual environment through VS Code, on the other hand, will create a "hidden" directory for your virtual environment called `.venv`. (Directories that begin with `.` do not appear when you run the `ls` command unless you supply the `-a` flag, but your text editor may display these folders.)

> NOTE: You may notice other folders, such as `__pycache__`, which may appear in your project as you add and execute code. It's safe to ignore such folders, and you can tell git to exclude them from a commit by running, for example, `git rm -r --cached <name_of_folder_to_untrack>`. If you want to avoid manually excluding pesky "behind-the-scenes" folders, like `__pycache__`, from your project altogether, create a file called `.gitignore` and add the following line to this file BEFORE you run your code for the first time: `__pycache__/`.
>
> If you decide to add a .gitignore to your project, your initial directory will resemble the following structure:
>
> ```
> ├── .gitignore
> ├── bin
> ├── lib
> ├── pyvenv.cfg
> ```
>
> You can learn more about using `.gitignore` in [this guide](https://canvas.uw.edu/courses/1699981/pages/working-with-api-keys-and-other-secrets-in-your-projects?wrap=1).

Moving forward, this guide will not include virtual environment files in folder tree graphics.

Now let's create our Flask app's "point of entry," a python file at the root of our project folder called `app.py`. Once you create this file, your entire project folder should match this structure.

```
├── .gitignore      # optional
├── app.py          # entry point of app
```

To create our application, we first need to import `Flask` in `app.py` by writing the following line of code.

`app.py`

```python
from flask import Flask
```

`flask` is a module (i.e. classes, functions, and scripts) that helps us create web applications by writing Python code. Remember, though, Flask is a _framework_, which means you must know _more than_ how to run Flask functions in order to build a Flask web application; you must additionally memorize several Flask conventions or "best practices." Creating a file called (exactly) `app.py` at the root of your project is the first Flask convention you should memorize.

We will create a Flask web application by creating an instance of a Flask class. To make a new instance, the Flask constructor expects a string that represents a "reference" to the Python module (i.e. file) which will execute the application's "start-up" code (i.e. run `app.py`). This reference will also help Flask locate all the files the application will need. Using `__name__`, the built-in Python variable, as this string supplies the information Flask needs and tells the Flask system to use `app.py`'s location as the application's root filepath.

Let's extend `app.py` to create our Flask application. We will create an instance of the Flask class as described above and then define our first route.

`app.py`

```python
from flask import Flask

my_flask_app = Flask(__name__)

@my_flask_app.route('/')
def render_html_for_default_page():
    return 'hello world'
```

We just created an instance of a Flask application called `my_flask_app`, and then defined the application's first route, "/". In other words, we wrote code that defines what will happen when the user visits `my-app/`. Let's break down this code further.

`my_flask_app`, our Flask object, has a special "decorator" method called `route()` which we can use to connect URLs and HTML files in our application. We use decorators by prefixing them with the `@` character. Hence, if we wanted to define a route for `/home`, we could do so by writing `@my_flask_app.route('/home')` and placing this code right above a render function.

Render functions in Flask must directly follow route decorators, and they must return some content. By default, returning a string from a render function will produce an HTML file that contains that string.

To run our application, navigate to the folder the contains `app.py` and run the following command:

```
flask --debug run
```

If your code and configuration are correct thus far, you should see the message below.

```
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 702-978-384
```

This message tells us that our computer is listening for HTTP requests (e.g. a visit from a web browser) at `http://127.0.0.1:5000`. The routes we define will always follow this URL. For example, if we create a route called `/home`, we must visit `http://127.0.0.1:5000/home` to run this route's render function.

> NOTE: Flask, like many frameworks, provide tooling to modify its system's default behavior. For example, you can run a Flask app from a file called `my-app.py` by running the following command:
>
> ```
> flask --app my-app.py run
> ```

## Rendering HTML Templates

Web pages are a key building block of web applications, and it can be handy to define a separate HTML file for each page of our application. This section will show you how to render an entire HTML file instead for a given route.

Let's say we are making a news application that will contain pages about sports and tech. We have decided that this application needs a home page, a page for sports news, and a page for tech news. One approach to designing this application would be to create a route and HTML file for each of these pages. To do so, we will need to follow the following steps.

1. Create a folder at the root of our project called `templates`
2. Create an HTML file for our page inside of `templates`
3. Define a route using a decorator for each page
4. User `render_template` to map each route and corresponding HTML file

When we're done, our complete project folder should resemble the form below.

```
- my-app
  ├── .gitignore
  ├── app.py
  ├── templates         # must match name exactly
  │   ├── home.html
  │   ├── sports.html
  │   ├── tech.html
```

Here is a simple template to use for our HTML pages.

`home.html`

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
  </head>
  <body>
    <h1>Home</h1>
  </body>
</html>
```

To map these whole HTML files to our desired routes, we first need to create a folder named `templates` in our project root as described above. This name and location are both Flask conventions-- though you can configure this filepath through the Flask constructor if you would like.

Anyways, we you create these items, extend `app.py` as follows.

`app.py`

```python
from flask import Flask, render_template

my_flask_app = Flask(__name__)

@my_flask_app.route("/")
def render_html_for_home_page():
    return render_template('home.html')

@my_flask_app.route("/sports")
def render_html_for_sports_page():
    return render_template('sports.html')

@my_flask_app.route("/tech")
def render_html_for_tech_page():
    return render_template('tech.html')
```

Notice that we are now importing a new function from `flask` called `render_template`. The purpose of `render_template` is to render HTML files by name and pass data to these files-- more on that later. To render an entire HTML file, we return the output of calling `render_template(<name_of_html_file_in_templates_folder_as_string>)`

## Processing Data in HTML with Jinja

Web applications tend to retrieve data and then transform it into HTML so that the user can see it in a web browser. Let's make some fake data that represents news articles for our application. Assuming we will fetch this data through an API, we will want to organize our code so that data-fetching functions are separate from our rendering functions. An easy way to organize your code is to make a file called `functions.py` to keep all of your code to fetch data. For this project, `functions.py` could look like this file.

`functions.py`

```python

def get_sports_news_data():
    return [
        {
            'title': 'Basketball News',
            'content': 'Blah blah about Basketball'
        },
        {
            'title': 'Football News',
            'content': 'Blah blah about Football'
        }
    ]

def get_tech_news_data():
    return [
        {
            'title': 'Apple News',
            'content': 'Blah blah about Apple'
        },
        {
            'title': 'Google News',
            'content': 'Blah blah about Google'
        }
    ]
```

All that the functions `get_sports_news_data()` and `get_tech_news_data()` do is return a list of dictionaries with fake information that represents a news article. Namely, both functions return a list of two dictionaries, where each dictionary contains a field for `title` and `content`.

Now let's import these functions into `app.py` by updating our import statement.

`app.py`

```python
from flask import Flask, render_template
from functions import get_sports_news_data, get_tech_news_data
```

Later in the file, we can then load and pass this data into our `sports` and `tech` HTML files using `render_template()` as shown below.

`app.py`

```python
@my_flask_app.route("/sports")
def render_html_for_sports_page():
    sport_news_data = get_sports_news_data()
    return render_template('sports.html', sports_articles=sport_news_data)

@my_flask_app.route("/tech")
def render_html_for_tech_page():
    tech_news_data = get_tech_news_data()
    return render_template('tech.html', tech_articles=tech_news_data)
```

Notice how we have added a second argument to our `render_template()` call. `render_template()` actually accepts any number of arguments beyond the first, and the caller of this function can name these additional parameters whatever they would like. However, your naming choice is significant because you will use this chosen variable name to reference its data from HTML.

Specifically, when you call `render_template('sports.html', sports_articles=sport_news_data)`, you are 'injecting' a list of dictionaries called `sports_articles` into an html file called `sports.html`. We can then use a technology called Jinja to process `sports_articles` from within `sports.html` by writing Python-like code in this HTML file.

**Rendering data with Jinja**

It's important to keep in mind that Jinja is not Python; it has its own rules and syntax. For example, let's say we want to print the value of a string called `sample_name` that we passed into `sports.html` as follows: `render_template('sports.html', sample_name='Adrian')`. We would do so by placing the name of the variable between double curly braces in our html. Take a look at how we could update `sports.html` to render "Adrian".

`sports.html`

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
  </head>
  <body>
    <h1>Sports News</h1>
    <p>{{ sample_name }}</p>
  </body>
</html>
```

To appreciate the difference between Jinja and Python, let's now update `sports.html` to render the number (i.e. length) of fake sports articles we created before. Here are some code snippets to jog your memory.

`functions.py`

```python
# We defined a list with two dictionaries here.
def get_sports_news_data():
    return [
        {
            'title': 'Basketball News',
            'content': 'Blah blah about Basketball'
        },
        {
            'title': 'Football News',
            'content': 'Blah blah about Football'
        }
    ]
```

```python
# We created and passed this list into sports.html
@my_flask_app.route("/sports")
def render_html_for_sports_page():
    sports_news_data = get_sports_news_data()
    return render_template('sports.html', sports_articles=sports_news_data)
```

```html
<body>
  <h1>Sports News</h1>
  <!-- Now we print the number of dictionaries  -->
  <p>{{ sports_articles | length }}</p>
</body>
```

To render the number of fake sports articles we created (i.e. the length of list of dictionaries we created in `functions.py`), we called `{{ sports_articles | length }}` in `sports.html` where `| length` applies a Jinja "filter" to `sports_articles`. Filtering for length is routine in Jinja, but it is odd in Python programming, where we have the built-in `len()` function.

**If Statements in HTML Files with Jinja**

If statements in Jinja look a bit different as well. Let's say we want to update `sports.html` to display a "no articles" message when the length of `sports_articles` is less than `1`.

`sports.html`

```html
<body>
  <h1>Sports News</h1>
  {% if sports_articles | length < 1 %}
  <p>There are no sports articles</p>
  {% endif %}
</body>
```

Notice that, instead of typing double curly braces `{{ }}`, we put if-statement code inside of curly braces and percentage signs `{% %}`. Unlike Python, where indentation and the colon demarcate if statements, Jinja if statements require two parts. The first is `{% if <!-- condition --> %}`, and the second part is `{% endif %}`.

**For Loops in HTML with Jinja**

Jinja also allows you to iterate over data. You can use this ability to, for example, generate HTML for every item of a given list of data. Let's use a Jinja for loop to do so for each sports_article dictionary we defined in `functions.py` and passed into `sports.html` as `sports_articles`.

```html
<body>
  <h1>Sports News</h1>
  <ul>
    {% for article in sports_articles %}
    <li>
      <h3>{{ article.title }}</h3>
      <p>{{ article.content }}</p>
    </li>
    {% endfor %}
  </ul>
</body>
```

For loops in Jinja do indeed resemble for loops in Python. Just like if statements, we place for-loop code inside of curly braces and percentage signs `{% %}`. You can iterate through `list` and create a variable named `item` for each element by creating a for loop with `{% for item in list %}` and closing it with `{% endfor %}`.

## Styling Flask Applications

Just like how Flask's HTML files must live in a folder called `templates`, Flask's CSS files must live in a folder called `static`.

Suppose we want to style our home page by making the page's title large and blue. We can do so with CSS by, for example, creating a file called `home.css` inside of a folder called `static` and then adding the following code to `home.css`:

`home.css`

```css
h1 {
  font-size: 8rem;
  color: blue;
}
```

These changes should make our app's folder look like like this.

```
- my-app
  ├── .gitignore
  ├── app.py
  ├── functions.py
  ├── templates
  │   ├── home.html
  │   ├── sports.html
  │   ├── tech.html
  └── static
      ├── home.css
```

Now that we have created our styling code and put it inside of `static`, we can link it to `home.html` by using a flask function called `url_for()`. `url_for()` is a function from the `flask` module that has the following parameters: `url_for(<name_of_render_function_in_app_py, <extra_var_name_1>=<extra_var_1>,)`. This function returns a URL that will always execute the render function one specifies as `url_for()`'s first argument. However, when we call the function with `static` as the first argument and `filename='home.css'` as the second argument, we can create a URL that will link any CSS file in `static` to any HTML file in `templates`. Let's update `home.html` to include `home.css`.

`home.html`

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link
      rel="stylesheet"
      href="{{ url_for('static', filename='home.css') }}"
    />
  </head>
  <body>
    <h1>Home</h1>
  </body>
</html>
```

Recall that, in general, we use the `<link>` HTML tag to connect CSS files to HTML files. Here we create a URL to `home.css` by calling `url_for('static', filename='home.css')`. Then we assign that URL to the `<link>` tag's `href` attribute, making the connection.
