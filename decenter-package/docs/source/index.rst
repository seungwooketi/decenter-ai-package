.. decenter_package_v1 documentation master file, created by
   sphinx-quickstart on Mon Apr 22 16:19:19 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to decenter's documentation!
===============================================


This project provides package (decenter) which can be used to build a Containerized AI Application (CAA) based on DECENTER platform. You can find more about DECENTER platform on the web site: http://www.decenter-project.eu

The purpose of this package is to provide base container to build a CAA. There exist various base containers to build an AI applicaiton on the container, but basically their purposes are limited to the containerization of ML platforms such as Tensorflow or Keras. With those containers, developers can build their own models and scoring functions with easy, since platforms and all the development tools, libraries are included in those base containers. However, to build an AI application as a microservice, developers needs to design the microservice architecture, and implement functionalities on their own. This will make it complex to containerize AI application for a developer. The DECENTER project (http://www.decenter-project.eu) will provide the base container and python package make it easy to containerize an AI application, and also to build a microservice with it.

* :doc:`Structure of DECENTER python package <overview>`


* :doc:`How it works <install>`


* :doc:`How to implement your AI logic with DECENTER BaseClass <howtobuild>`

Package Information
===================
.. toctree::
   :maxdepth: 2

   decenter

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
