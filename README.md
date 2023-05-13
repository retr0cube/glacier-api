<p align=center>
  <img src="https://github.com/retr0cube/glacier-api/assets/61835816/ab1f1765-ceb4-443e-92bf-fa509c931c4f">
</p>
<h1 align="center">Glacier API</h1>
<p align=center>A REST API for the 👾 Monolith project</p>

<p align=center>
<img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/retr0cube/glacier-api?color=darkblue&style=for-the-badge"><img alt="GitHub" src="https://img.shields.io/github/license/retr0cube/glacier-api?color=blue&style=for-the-badge"><img alt="GitHub Workflow Status" src="https://img.shields.io/github/actions/workflow/status/retr0cube/glacier-api/python-app.yml?logo=GitHub&style=for-the-badge"></p>


## ℹ️ What is this?
- As mentioned in my [proof of concept](https://www.notion.so/monolith-retcy/feca0c394c4146429d7f7e0deee57e06?v=823fd92169e14adcbab697f69c98e32b&pvs=4), this is a REST API designed to house a database full of addons, and make it accessible via GET requests which return a JSON object, it’s the main addon repository for the 👾 Monolith project hosted on glacier-api.onrender.com.

_**Example:**_
- HTTP request:
```
GET https://glacier-api.onrender.com/package/mnl
```
- JSON response:
```json
{
	"name": "Monolith",
	"author": ["Retcy"]
	// other stuff here ;)
}

```

**NOTE: You can use this repository as a template for your own custom repo to use on the CLI.**

