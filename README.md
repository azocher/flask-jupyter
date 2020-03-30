# ⌨️ Flask and Jupyter Notebooks

----

## ⛏ Tools

*Flask* is a lightweight web server written in and using Python. 

*Jupyter Notebooks* are a web-based computational environment that run scripts organized by individual cells, over traditional pages.

While data scientist traditionally work in Jupyter Notebooks, besides passing `.ipyndb` formated documents, there is no easy way to use or run scripts outside of Jupyter notebooks.  


## Jupyter Notebook and Flask Integration

When we talk about using *Jupyter Notebooks* and i together, we can be talking about one of two ways to use these tools:

1. Running a *Jupyter Notebook* instance from a *Flask* server we write. 
2. Importing scripts written in *Jupyter* to a *Flask* server for local use. 

**We will be exploring the second of these two options in this lesson.**

![Data and a Cat](https://media.giphy.com/media/IMdS79sQINRAY/giphy.gif)

## 👩‍💻 Project Description
You will be given a data set with counts of baby names in the United States (measured by state) from the years 2004-2014. 

As a working group you, the software developer, and a teamate, a data scientist, have each been assigned something to build. 

You, the software developer, have been tasked with developing a frontend and backend of a website where a user can input a pottential baby name, and get a "uniquness" score relative to how common that name is in their state. 

The data scientist on the team has been tasked with writing the formula for us to determine the "uniqueness" score of the user's inputed name. 

## 🏢 Steps to Achieve

### Importing Data
When we bring data into an application we have two options: 

1. Making a call to an external data source (examples: calling an API, referencing a third party DB). 
2. Importing data locally (example: reading a .CSV file). 

Because Jupyter notebooks are often hosted locally on the data scientist's computer (not remotely), we will be importing data and scripts from a Jupyter Notebook file (a `.ipynb`) file that has been given to us by a data scientist who has written some calls for us to use on a web application. 


### Data Gathering

In order to run our scripts we need the data source or file our data scientist originally refered to, and the scripts they wrote in their *Jupyter Notebook*. 

Get a local or remote link to the data file (ideally a `.csv` or `JSON` file, depending on what type of data science is being done). 

Receive the relevant *Jupyter Notebook* file, and make sure both are in your project folder. 

### Setup a Flask Server

We are going to setup a default Flask server instance to run our script from. 

This server should have a `GET` route at `/` (our home page) that displays a form to the user. This form should take in an input from the user (a baby name). 

This same route should also accept a `POST` request, and for now should just display the given user input as a return. 

### Import and Read Jupyter Script

The type of file our *Jupyter Notebook* is exported as will determine how we import the pre-written methods. For the sake of this tutorial, let's assume we have asked our Data Science to export their file as a `.py` file. 

This file format, when exported from *Jupyter Notebooks*, will export everything except was written "IN" to the program as comments. 

We want to take these written scripts and import them as a module. To do this we have to update the relative link to the imported data, and update each statement which previously returned something in *Jupyter* to a function. Otherwise, we won't have anything to return or access when we import this module.

As an example, if the following data import and `pandas` call are exported from *Jupyter* they will first appear in the following format:

```python
import pandas as pd

baby_names = pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv')

baby_names['Gender'].value_counts()
```

We want to get the relative output of the final line (`baby_names['Gender'].value_counts()`) to pass to the frontend of our project. To be able to get this script as a `return` we have to wrap this entire method in a function decleration, and then use a `return` statement to mark the data we want sent to us on module import. 

Jupyter code updated for Web use:

```python
import pandas as pd

def export(data):
    baby_names = pd.read_csv(data)
    return baby_names['Gender'].value_counts()
```

On our *Flask* server we would import this module, and pass it our local data file as a variable. 

```python
# import scripts
import module_file_name as data_script

# add url or reference to data file
data_file = "./data/names.csv"

....
# when we pass result of script to our route
	return render_template('return.html', tables=data_script.export(data_file))

```

That final line refers to how we will pass this information (via a method call on our module) to our frontend. 

### Display Result to User

When returning data in `pandas` data frame format to the fronted, we have to pass it as a variable in a `render_template` call. 

For example, if we want to pass a data to the frontend, we would create a template that would have an input holder in Jinja: 

```html
<div class="dataTable">
	{{table}}
</div>
```

On the backend, we would have our `POST` method return a `render_template` call with the result of our data call (our data frame object) being passed to the frontend as the variable name `table`:

```python
if request.method == 'POST':
	return render_template('dataDisplay.html', table=data_response_method)
```

### Conclusion

Work between Data Scientists and Software Engineers involves a very unique venn diagram of tools and languages. In this example we have assumed that a Data Scientist will be working in *Jupyter* and a Software Engineer is working primarily in Python/*Flask*, but our options for powerful cross-functional work continue to expand as tools improve. 

Talk to your teammates - work to understand the problems they run into day to day. Longterm, the better an understanding of tools and workflows you cultivate, the further you will be able to go not just working with your own team but in helping build and plan projects holistically. 
