Overview
========

Consider building an AI application based on the Tensorflow base container. The figure below depicts the configuration of app on TF container. TF container provides various tools for AI model and application development. Notebook, libraries as well as TF itself is included in the TF container. To build an AI application based on that, developer can implement everything on his/her own. Build a model, develop scoring functions, and if it is going to be a microservice, an interface can be built with any server implementation.

.. image:: http://182.252.132.43/decenter/appontfcon.png
  :width: 500px

However, these configuration can vary from every implementation. This will eventually bring degradation on design and development phase. If you want to build another AI application with different model or different function, you might need to implement another application from the scratch. Different network model means that it requires different preprocessing of input data, and also different translation of results.
The purpose of this project, is to provide a package which can be used to build an AI application on a container, with more systematic and intuitive way.

Package configuration
=====================

.. image:: http://182.252.132.43/decenter/appondecenter.png
  :width: 700px


The figure below depicts AI application built with this decenter package. Being compared to the first figure, you can find that number of orange boxes has been decreased, which means that roles of developer has been decreased. In our package, we're going to provide frameworks to enable packaging of existing AI application into a microserivce-compatible container, and those functionalities are depicted as green boxes in the figure.

You can find 3 major modules in DECENTER package in the above figure - which are, :class:`decenter.ai.appconfig.AppConfig`, :class:`decenter.ai.flask.DecenterFlask`, and :class:`decenter.ai.baseclass.BaseClass`.

The first one includes methods to the configuration messages for an AI application - from where retrieve input to be processed, where to will the AI result be delivered. Also methods to control of AI computation - start AI computation, and terminate AI computation are included in that module. :class:`decenter.ai.flask.DecenterFlask` will provide RESTful interfaces for the communication between this DECENTER-based service and other microservices. This moduel works as a message handler between RESTful interface and other modules. :class:`decenter.ai.baseclass.BaseClass` provides the root class for AI logic implementation.
