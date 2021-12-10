
# Information Extraccion: Aviation accidents
Laboratory Assignment II: Trainable Information Extraction. From AIW 2021.

This repository contains the application web that uses a pre-trained model based on fine-tunned BERT to extract information from aviation accidents texts. We we run our model inside a Flask server using torch.

The developed application has been designed to be easy to use, with a clear and lossless interface.

![Front page of our application](/static/img/front2.png)


The application also contains a few preloaded HTML samples that do not require starting the server with the model. To do so, simply open the [index.html](https://github.com/Pedroos46/Aviation-accidents-IE/blob/main/templates/index.html) page (inside the *templates* folder), as if it were any other web page.

### Model

Our model has been build using a pre-trained version of BERT specific for Token Classifications sourced by HuggIngFace. (HugginFace, 2020). This  model is posteriorly fine-tuned. The fine-tuning procedure allows adjusting a pre-trained model, using transfer learning, to specialize the network towards a specific content or format.

In our case, we adjust the model so that it is capable of detecting information related to aircraft accidents. We do it using the [Conscius](http://www.taln.upf.edu/pages/concisus/index.html)  Corpus (Saggion & Szasz, 2012) dataset, which contains .

Our model and the data associated to it can be found in the *model* folder.


## Environment configuration
### Package installation

In order to run the model, as well as the server, we need to have some Python libraries and packages installed.

**Remember!** If you manage different versions of Python on your machine, or use Python3. Maybe you should use  `pip3` instead of `pip`.

The packages required to run our application are:

    pip install torch

Which runs our model.

    pip install flask
    pip install flask_cors
    pip install json

Which is used to start the server and send requests to the model.

    pip install numpy
    pip install nltk
    pip install transformers

Additional software required to use the model correctly.

## Running the server.
Once all the packages has been installed successfully we can simple run the server and the web application bye typing in the root folder of the project:

    flask run

**BUT:** Due to differences in machines or operating system configurations, or future versions of Flask or Python. As well as to avoid problems with HTTP request or CORS. **We strongly recommend to run it using:**

    flask run --host=127.0.0.1 --port=5000

App.py contains all the settings to avoid problems with the server host, as well as other CORS problems. If you want to modify any aspect of the server you must modify the settings in that file, or setting up different Flask variables.

The server may take a while to start at the first time, and may update some of its packages. The **model is loaded when the server starts**, depending on your machine it may take more or less time, but it should not take more than 30 seconds.

We also recommend shutting down the server, either from a browser or from Postman, using:

    http://127.0.0.1:5000/shutdown

If you used the previous launch parameters. Ctrl + C can also be used, but we recommend to use the previous statement.

##### Detected problems:
At certain points in the development we have detected strange behaviors by server-browser.

If at some point you encounter unauthorized access to the server (403) or the server does not respond correctly, terminate the process (if not possible consider the task manager) and startup it again. Also, completely close your browser and launch it again.

Another problem detected while development is the dev and production launch. Due to some Flask configurations, the server may not start if it detects that it is in production. For this we recommend reviewing the [Flask Environment configuration](https://flask.palletsprojects.com/en/2.0.x/config/) in order to set `FLASK_ENV`.

    FLASK_APP = app.py
    FLASK_ENV = development
    FLASK_DEBUG = 0

## Launching the web app.

**Application startup should be automatic at server startup.** The server may take a while to start the first time, and may update some of its packages. The model is loaded when the server starts, depending on your machine it may take more or less time, but it should not take more than 30 seconds.

One way to access the page if it does not happen automatically, is going manually to this address:

- [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

If the Flask server has started without problems it should be able to access without problems.


#### Detected problems:
In case the browser is not able to find the page, you can access it by launching index.html page **downloaded** in your computer, inside the *templates* folder. At this point it is possible that the web will not be able to make the requests correctly to the server. If it's a server problem, you can still check the HTML examples on the page.

In case it is a problem with the Flask server, apart from checking the Index.html page, you can also try to run the CLI application.

## Terminal version

The terminal application pretends to be a more distilled version of our application, returning the extracted information directly simplified.

Can be started with:

    python application.py

or

    python3 application.py  

inside the folder *terminal-application*.

## Authors
Roger Pedrós Villorbina.

Wenjie Jin. 

Rodrigo Caero.