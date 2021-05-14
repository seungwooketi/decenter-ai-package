Installation
============

The decenter package is provided in the form of python package. You can install it with a simple pip command. ::

  $ pip install decenter

As of now, decenter package has not been published yet. We'll do that when it's ready.

How to build AI application with DECENTER Package
=================================================

Basic methods for AI application are already defined in :class:`decenter.ai.baseclass.BaseClass`. To build an application, you need to create a new class inhereted from that, and override several methods to implement your application logics.

Create a class from BaseClass and override methods
--------------------------------------------------

Create a class inherited from :class:`decenter.ai.baseclass.BaseClass`::

  from decenter.ai.baseclass import BaseClass

  class MyClass ( BaseClass ):
    def __init__(self):
      pass

  ...

Override a few methods in :class:`~decenter.ai.baseclass.BaseClass`. Methods to be overridden are as follows:

* :func:`~decenter.ai.baseclass.BaseClass.load_ai_model` : this function loads AI model to host memory. You might need to define network structure you want to use, as well as restoring weights from model file.

* :func:`~decenter.ai.baseclass.BaseClass.compute_ai` : this is where your AI methods comes. Implement logics to open/read the input source, preprocess the input source, and then apply it to the AI model. The return value shall be interpreted values (not the scores from the output layer).

As of now, all the AI logics are implemented in :func:`~decenter.ai.baseclass.BaseClass.compute_ai`, but as this project goes on, this methods will be divided into several methods to make AI logics more modular.

BaseClass and :class:`~decenter.ai.appconfig.AppConfig` class
-------------------------------------------------------------

:class:`~decenter.ai.appconfig.AppConfig` is a class to hold configuration values for AI application. When you create an instance of BaseClass, associated AppConfig class will be also initiated.

You can access configuration variables by calling :func:`decenter.ai.baseclass.BaseClass.get_app_config`. This method will return the AppConfig instance. Refer to AppConfig documentation :class:`decenter.ai.baseclass.BaseClass` for more detail.

Load AI model
-------------

Now you can start download AI model to be used from the repository, by calling :func:`decenter.ai.appconfig.AppConfig.set_model_url` ::

  MODEL_URL = "http://182.252.132.43/decenter_data/ckpt/vgg_16.ckpt"

  app.get_app_config().set_model_url(MODEL_URL)
  app.download_model()

This method will download AI model from the designated URL to local volume, and load it to memory. By default, model file(s) will be downloaded to '/model' directory, and if the file with the same name exists, it will not download the model file. Currently only file names are compared, and other measures such as MD5 will be added. If you want to avoid download AI models every time container restarts, mounting a local volume to the '/model' directory can be a good exercise.

Open External Interfaces (Flask App)
------------------------------------

Flask interfaces are defined in decenter.ai.flask module, and you can find details in :ref:`decenter.ai.flask`. To add a custom interfaces and handlers, you have to retrieve flask app instance from flask module first. After that, you can add Flask interface to that instance.

To get Flask app instance, you can call :func:`decenter.ai.flask.DecenterFlask.get_flask_app` on DecenterFlask instance. Here is a sample code to add custom handler for Flask app. ::

  msg_handler = init_handler(app)

  flaskapp = msg_handler.get_flask_app()

  @flaskapp.route('/test')
  def test():
      return 'custom msg handler test page'

Start you application and Flask server
--------------------------------------

Now you are ready to run your application. Here's an example code for all of the above ::

  from decenter.ai.baseclass import BaseClass

  class MyClass ( BaseClass ):
    def __init__(self):
      # for example, you can create TF session here.
      self.sess = tf.Session()
      # don't forget to methods on parent class.
      super(MyClass, self).__init__()

    # override these method to load your AI model
    def load_ai_mode():
      saver = tf.train.Saver()
      saver.restore(self.sess, "model_file")

    # here, you do open the input file, preprocess it, feed to the AI model and compute. Return value has to be suitable to be sent over HTTP.
    def compute_ai():
      result = self.sess.run()
      return result

  ...

  # Create instance of AI application logic.
  app = MyClass()

  # set configuration if needed.
  app.get_app_config().set_model_url(MODEL_URL)
  app.get_app_config().set_input_source("http://182.252.132.43/decenter_data/images/kite.jpg")
  app.load_ai_model()

  # init Flask message handler
  msg_handler = init_handler(app)

  flaskapp = msg_handler.get_flask_app()

  # if you want to add more interfaces, add it here.
  @flaskapp.route('/test')
  def test():
      return 'custom msg handler test page'

  # start Flask server to open RESTful interface.
  flaskapp.run(host="0.0.0.0")


Test your application logic
===========================

You can test your application with a web browser or curl or anything which can handle HTTP message. List of supported HTTP endpoints can be found here: http://182.252.132.43/decenter/decenter.ai.flask.html#restful-interface

Open a webbrowser, and go to this URL to find whether it works properly. ::

  http://127.0.0.1:5000/hello

To set the source to be analyzed, use the following URL. ::

  http://127.0.0.1:5000/setinput?input=[input source]

  example: http://127.0.0.1:5000/setinput?input=http://server/image.jpg

To get the inference result, invoke AI computation with the following URL. Inference result will be sent back with HTTP response. ::

  http://127.0.0.1:5000/compute
