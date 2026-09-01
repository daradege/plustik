🎯 Defined Messages
===========

how to define static commands in plustik

.. toctree::
   :maxdepth: 2
   :caption: Static messages example



.. code-block:: python

    from plustik import Client, Message

    bot = Client("YOUR_BOT_TOKEN")

    bot.defined_messages = {
        "/start": "Hello! welcome to Plustik!",
        "/help": "I cannot help you now :)"
    }

    bot.check_defined_message = True

    bot.run()