# Overview

This project provides package (decenter) which can be used to build a Containerized AI Application (CAA) based on DECENTER platform. You can find more about DECENTER platform on the web site: http://www.decenter-project.eu

The purpose of this package is to provide base container to build a CAA. There exist various base containers to build an AI applicaiton on the container, but basically their purposes are limited to the containerization of ML platforms such as Tensorflow or Keras. With those containers, developers can build their own models and scoring functions with easy, since platforms and all the development tools, libraries are included in those base containers. However, to build an AI application as a microservice, developers needs to design the microservice architecture, and implement functionalities on their own. This will make it complex to containerize AI application for a developer. The DECENTER project (http://www.decenter-project.eu) will provide the base container and python package make it easy to containerize an AI application, and also to build a microservice with it.

Consider building an AI application based on the Tensorflow base container. The figure below depicts the configuration of app on TF container. TF container provides various tools for AI model and application development. Notebook, libraries as well as TF itself is included in the TF container. To build an AI application based on that, developer can implement everything on his/her own. Build a model, develop scoring functions, and if it is going to be a microservice, an interface can be built with any server implementation.

![](https://bitbucket.org/teamgold19/decenter_package_v1/raw/b856a25cecdc0b95736bbdfa0b58ade08200d919/docs/img/appontfcon.png)

However, these configuration can vary from every implementation. This will eventually bring degradation on design and development phase. If you want to build another AI application with different model or different function, you might need to implement another application from the scratch. Different network model means that it requires different preprocessing of input data, and also different translation of results.
The purpose of this project, is to provide a package which can be used to build an AI application on a container, with more systematic and intuitive way.

## Package configuration

![](https://bitbucket.org/teamgold19/decenter_package_v1/raw/b856a25cecdc0b95736bbdfa0b58ade08200d919/docs/img/appondecenter.png)

The figure below depicts AI application built with this decenter package. Being compared to the first figure, you can find that number of orange boxes has been decreased, which means that roles of developer has been decreased. In our package, we're going to provide frameworks to enable packaging of existing AI application into a microserivce-compatible container, and those functionalities are depicted as green boxes in the figure.

## Installation

The decenter package is provided in the form of python package. You can install it with a simple pip command.

    # pip install decenter

## How to use decenter package to containerize an AI application

As of now, decenter package provides several facilities to enable containerization of AI method. The base class ***decenter.ai.baseclass*** package provides placeholder to host AI mothod itslef - for example, downloading AI model, loading AI model onto memory, apply input data to the AI model, etc. The configuration for the AI method inside a container - i.e. input media location or output destination - are stored in ***decenter.ai.appconfig package***. ***decenter.ai.flask*** class provides interfaces (which are built with Flask App) to the AI methods and configurations. 


### How it works

The logic implemented in this baseclass are as follows.

* When initiated, this baseclass will load AI model into memory, as designated in the variable ***model_info***.

* When model loading is complete, this baseclass will start Flaks server to open communication channel with other instances. Default Flask server implementation can be found on ***decenter.ai.flask***. Currently, two methods are provided for the configuration, each to set source url and destination url.

* Configura AI method's input and output variables. It can be done with YAML config file or RESTful API. 

* After source and destination are set, now this containerized AI application is ready to run. You can start AI application by sending a message to the Flask included in this package.


### How to configure your AI Application

There are two configuration methods available for AI application configuration. The first one is on-deployment configuration method. In this method, all the configuration values are written on the YAML deployement file, and injected into POD/ microservices by Kubernetes. The other one is runtime configuration method. In this method, the other microservice (or other software instances) configure AI microservice by accessing HTTP RESTful API. Configurable variables on AI microservices are as follows. 

* Set Input source

It designates URL where source data to be analyzed are. Examples can be an image file (file://myfile.jpg, http://server/image.jpg), a video streaming URL (rtsp://server/setreaming_address, http://server/streaming_address) or any other location which can be represented in URI.

* Set destination

It designates URL to where analysis result will be sent. It can be a HTTP server URL, MQTT topic, or anything which can receive a message.

* AI model 

It designates URL where the AI model locaes.  

#### Configuring AI method with YAML

apiVersion: v1
kind: ConfigMap
metadata:
  name: myconfig1
data:
  appconfig: |
    {
      "input": {
      "type": "http | mqtt", 
      "url": "url",
      "topic": "name of the topic, if type == mqtt"
      },
      "output": {
      "type": "http | mqtt",
      "url": "url",
      "topic": "name of the topic, if type == mqtt"
      }
      "ai_model": {
      "url": "location of AI model",
      }
}

Load configMap to the k8s, and the correpsonding values will be injected to the microservice when baseClass is initiated. 



### How to control your AI application

Currently, start and stop of AI methods are supported.

* Start AI

* Stop AI

## How to build your application based on decenter package.

Here are steps required to port your application into decenter-compatible container.

* install DECENTER, or, you can start building your application from decenter base container (will be provided later).

* refactor your application to decenter.ai.BaseClass

If you want to build your application into a docker container, please wait some more. Decenter base container will come shortly.

# test.py and running your application

You can run the test code with this command

    $ python3 test.py

* test.py

This file contains example AI application based on the decenter package. The base class for AI application will be initiated, and appconfig instance will be created. Also, to communicate with other services, a Flask (DecenterFlask) instance will be also initiated.

* customhandler.py

This file contains message handler (route) for DecenterFlask class. If you want to add any communicaiton interface based on decenter package, you can add them here in this file.

To test the test code, you can open a web browser on the same machine where test.py runs, and open these URLs. If 404 is returned, it means that something's wrong.

* http://127.0.0.1/index : a simple message will be shown on the web browser.

* http://127.0.0.1/setinput : this will call set_input_source with value "aaa". a simple message will be returned.

* http://127.0.0.1/getinput : if called after setinput, "aaa" will be shown.

* http://127.0.0.1/test : a simple message will be shown. This page is directed to the custom_handler.py
