🎯 Echo bot
===========

how to code an echo bot in plustik (threaded automatically)

.. toctree::
   :maxdepth: 2
   :caption: Echo bot example

.. code-block:: python

    from plustik import Client, Message

    client = Client("YOUR_BOT_TOKEN")

    @client.on_message()
    def message_handler(message: Message):
        message.reply(message.text)

    client.run()