# ProcTHOR

Create a virtual environment and install the requirements listed in requirements.txt install of using their installation functions in the notebook (i have commented them out). The version of moviepy they install gives errors on SCC so I have downgraded to moviepy 1.0.3

Make sure when defining the controller, you use the `platform` parameter and set it to CloudRendering. Otherwise it gives issues on SCC due to lack of display. 