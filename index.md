# Information Extraccion: Aviation accidents
Laboratory Assignment II: Trainable Information Extraction. From AIW 2021.

This repository contains the application web that uses a pre-trained model based on fine-tunned BERT to extract information from aviation accidents texts. We we run our model inside a Flask server using torch.

The developed application has been designed to be easy to use, with a clear and lossless interface.

![Front page of our application](https://raw.githubusercontent.com/Pedroos46/Aviation-accidents-IE/main/static/img/front2.png)

The application also contains a few preloaded HTML samples that do not require starting the server with the model. To do so, simply open the [index.html](https://github.com/Pedroos46/Aviation-accidents-IE/blob/main/templates/index.html) page (inside the *templates* folder), as if it were any other web page.

## Model

Our model has been build using a pre-trained version of BERT specific for Token Classifications sourced by HuggIngFace. (HugginFace, 2020). This  model is posteriorly fine-tuned. The fine-tuning procedure allows adjusting a pre-trained model, using transfer learning, to specialize the network towards a specific content or format.

In our case, we adjust the model so that it is capable of detecting information related to aircraft accidents. We do it using the [Conscius](http://www.taln.upf.edu/pages/concisus/index.html)  Corpus (Saggion & Szasz, 2012) dataset, which contains .

## Authors
Roger Pedrós Villorbina.

Wenjie Jin. 

Rodrigo Caero.
