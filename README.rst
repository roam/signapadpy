==========
Signapadpy
==========

`Signature Pad <http://thomasjbradley.ca/lab/signature-pad/>`_ is a nice tool
that allows users to provide a drawn signature. Because of the flakiness of
some browsers, it's probably recommend to generate an actual image of the
signature on the server. And that's what signapadpy does with a little help
of `Pillow <http://python-imaging.github.io/>`_ (or PIL).

First install it::

    pip install signapadpy

Next, import what you need (padding is optional)::

    from signapadpy import create_image, Padding

Then load the lines of the signature you want to convert into an image::

    lines = load_signature_pad_output(from_something)

And create the image::

    image = create_image(lines)

The image is an instance of PIL's (or Pillow's) ``Image``, so you can choose to display it::

    image.show()

Or save it::

    image.save('signature.png')

If you'd like to render the image with Django, you could do it like this::

    from django.http import HttpResponse
    from django.shortcuts import get_object_or_404

    from signapadpy import create_image


    def view_signature(request, pk):
        # Django view, assuming a Sigature model with a lines attribute
        signature = get_object_or_404(Signature, pk=pk)
        return signature_to_response(signature.lines)

    def signature_to_response(lines):
        image = create_image(lines)
        response = HttpResponse(mimetype='image/png')
        image.save(response, 'PNG')
        return response
