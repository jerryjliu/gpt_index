# Installation and Setup

### Installation from Pip

You can simply do
```
pip install gpt-index
```

### Installation from Source
Git clone this repository: `git clone git@github.com:jerryjliu/gpt_index.git`. Then do:

- `pip install -e .` if you want to do an editable install (you can modify source files) of just the package itself.
- `pip install -r requirements.txt` if you want to install optional dependencies + dependencies used for development (e.g. unit testing).


### Setup Environment

By default, we use the OpenAI GPT-3 "text-davinci-002" model. In order to use, you must have an OPENAI_API_KEY setup.
You can register an API key by logging into [OpenAI's page and creating a new API token](https://beta.openai.com/account/api-keys)