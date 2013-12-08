Usage
=====

.. function:: signapadpy.create_image(lines, [size, [padding, [center, [line_color, [line_width, [bg_color, [mode]]]]]]])

Use ``create_image`` to generate an image from the lines supplied by
Signature Pad.

Parameters:

    - ``lines``: the lines from Signature Pad
    - ``size``: the desired size of the image. Defaults to the size of the signature. Specify a size to scale the image
    - ``padding``: optional padding; no padding is applied by default
    - ``center``: the signature will be centered within the image by default
    - ``line_color``: defaults to ``#000``
    - ``line_width``: defaults to a single pixel
    - ``bg_color``: defaults to ``#fff``
    - ``mode``: defaults to RGB

.. code-block:: python

    from signapadpy import create_image, Padding

    lines = [{'lx': 0, 'ly': 10, 'mx': 5, 'my': 15}, ...]
    image = create_image(lines)

This will generate the image as is with a size corresponding to the size of the signature.

If you want to scale the signature to a specific size, just pass it:

.. code-block:: python

    image = create_image(lines, (640, 480))

Maybe add some padding as well:

.. code-block:: python

    top = 10
    right = 10
    bottom = 10
    left = 10
    padding = Padding(top, right, bottom, left)
    image = create_image(lines, (620, 460), padding)

Note that padding adds to the size of the image. The code above will still generate an image of 640x480 pixels.
