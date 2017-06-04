import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS('#336699', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)

chart.title = 'Python Projects'
chart.x_labels = ['awesome-python', 'httpie', 'thefuck', 'flask', 'youtube-dl', 'django', 'requests', 'ansible', 'awesome-machine-learning', 'big-list-of-naughty-strings', 'scrapy', 'scikit-learn', 'certbot', 'shadowsocks', 'system-design-primer', 'keras', 'models', 'XX-Net', 'superset', 'YouCompleteMe', 'CppCoreGuidelines', 'tornado', 'reddit', 'you-get', 'sentry', 'Deep-Learning-Papers-Reading-Roadmap', 'ipython', 'python-patterns', 'macOS-Security-and-Privacy-Guide', 'source-code-pro']

plot_dicts = [
	{'value': 34601, 'label': 'A curated list of awesome Python frameworks, libraries, software and resources'}, 
	{'value': 29896, 'label': 'Modern command line HTTP client – user-friendly curl alternative with intuitive UI, JSON support, syntax highlighting, wget-like downloads, extensions, etc.  https://httpie.org'},
	 {'value': 28249, 'label': 'Magnificent app which corrects your previous console command.'}, 
	{'value': 27410, 'label': 'A microframework based on Werkzeug, Jinja2 and good intentions'},
	 {'value': 26421, 'label': 'Command-line program to download videos from YouTube.com and other video sites'}, 
	 {'value': 26044, 'label': 'The Web framework for perfectionists with deadlines.'},
	 {'value': 25301, 'label': 'Python HTTP Requests for Humans™'},
	  {'value': 23505, 'label': 'Ansible is a radically simple IT automation platform that makes your applications and systems easier to deploy. Avoid writing scripts or custom code to deploy and update your applications— automate in a language that approaches plain English, using SSH, with no agents to install on remote systems.'}, 
	{'value': 23113, 'label': 'A curated list of awesome Machine Learning frameworks, libraries and software.'},
	{'value': 21095, 'label': 'The Big List of Naughty Strings is a list of strings which have a high probability of causing issues when used as user-input data.'},
	 {'value': 20856, 'label': 'Scrapy, a fast high-level web crawling & scraping framework for Python.'}, 
	 {'value': 18937, 'label': 'scikit-learn: machine learning in Python'}, 
	 {'value': 18650, 'label': "Certbot, previously the Let's Encrypt Client, is EFF's tool to obtain certs from Let's Encrypt, and (optionally) auto-enable HTTPS on your server.  It can also act as a client for any other CA that uses the ACME protocol."}, 
	 {'value': 17925, 'label': 'Nonee'}, 
	 {'value': 17163, 'label': 'Learn how to design large-scale systems. Prep for the system design interview.  Includes Anki flashcards.'}, 
	 {'value': 16149, 'label': 'Deep Learning library for Python. Convnets, recurrent neural networks, and more. Runs on TensorFlow or Theano.'}, 
	 {'value': 15403, 'label': 'Models built with TensorFlow'}, 
	 {'value': 14554, 'label': 'a web proxy tool'},
	  {'value': 14255, 'label': 'Superset is a modern, enterprise-ready business intelligence web application'}, 
	  {'value': 13966, 'label': 'A code-completion engine for Vim'}, 
	  {'value': 13856, 'label': 'The C++ Core Guidelines are a set of tried-and-true guidelines, rules, and best practices about coding in C++'},
	   {'value': 13620, 'label': 'Tornado is a Python web framework and asynchronous networking library, originally developed at FriendFeed.'}, 
	   {'value': 13216, 'label': 'the code that powers reddit.com'}, 
	   {'value': 13190, 'label': ':arrow_double_down: Dumb downloader that scrapes the web'}, 
	   {'value': 12810, 'label': 'Sentry is a cross-platform crash reporting and aggregation platform.'},
	    {'value': 11793, 'label': 'Deep Learning papers reading roadmap for anyone who are eager to learn this amazing tech!'}, 
	    {'value': 11568, 'label': 'A collection of design patterns/idioms in Python'}, 
	    {'value': 11567, 'label': 'Official repository for IPython itself. Other repos in the IPython organization contain things like the website, documentation builds, etc.'},
	    {'value': 11381, 'label': 'A practical guide to securing macOS.'},
	     {'value': 10878, 'label': 'Monospaced font family for user interface and coding environments'}
	     ]
chart.add('', plot_dicts)
chart.render_to_file('bar_descriptions.svg')