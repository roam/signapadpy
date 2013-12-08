# -*- coding: utf-8 -*-
from __future__ import (unicode_literals, print_function, division,
                        absolute_import)

from signapadpy import create_image, Padding


# A sample of a signature generated with Signature Pad. Not the most
# beautiful render, but it'll do.
sample = [{"lx":23,"ly":38,"mx":23,"my":37},
{"lx":23,"ly":38,"mx":23,"my":38},
{"lx":24,"ly":37,"mx":23,"my":38},
{"lx":25,"ly":36,"mx":24,"my":37},
{"lx":26,"ly":34,"mx":25,"my":36},
{"lx":27,"ly":34,"mx":26,"my":34},
{"lx":27,"ly":33,"mx":27,"my":34},
{"lx":27,"ly":32,"mx":27,"my":33},
{"lx":28,"ly":31,"mx":27,"my":32},
{"lx":29,"ly":29,"mx":28,"my":31},
{"lx":30,"ly":28,"mx":29,"my":29},
{"lx":31,"ly":28,"mx":30,"my":28},
{"lx":31,"ly":26,"mx":31,"my":28},
{"lx":32,"ly":26,"mx":31,"my":26},
{"lx":32,"ly":24,"mx":32,"my":26},
{"lx":33,"ly":24,"mx":32,"my":24},
{"lx":34,"ly":21,"mx":33,"my":24},
{"lx":35,"ly":20,"mx":34,"my":21},
{"lx":35,"ly":18,"mx":35,"my":20},
{"lx":36,"ly":15,"mx":35,"my":18},
{"lx":37,"ly":13,"mx":36,"my":15},
{"lx":38,"ly":12,"mx":37,"my":13},
{"lx":38,"ly":10,"mx":38,"my":12},
{"lx":39,"ly":10,"mx":38,"my":10},
{"lx":39,"ly":12,"mx":39,"my":10},
{"lx":39,"ly":13,"mx":39,"my":12},
{"lx":40,"ly":13,"mx":39,"my":13},
{"lx":40,"ly":16,"mx":40,"my":13},
{"lx":40,"ly":17,"mx":40,"my":16},
{"lx":40,"ly":18,"mx":40,"my":17},
{"lx":41,"ly":19,"mx":40,"my":18},
{"lx":41,"ly":21,"mx":41,"my":19},
{"lx":42,"ly":21,"mx":41,"my":21},
{"lx":42,"ly":24,"mx":42,"my":21},
{"lx":43,"ly":24,"mx":42,"my":24},
{"lx":43,"ly":26,"mx":43,"my":24},
{"lx":43,"ly":28,"mx":43,"my":26},
{"lx":43,"ly":29,"mx":43,"my":28},
{"lx":43,"ly":30,"mx":43,"my":29},
{"lx":44,"ly":31,"mx":43,"my":30},
{"lx":44,"ly":32,"mx":44,"my":31},
{"lx":45,"ly":32,"mx":44,"my":32},
{"lx":46,"ly":28,"mx":45,"my":32},
{"lx":47,"ly":25,"mx":46,"my":28},
{"lx":48,"ly":24,"mx":47,"my":25},
{"lx":48,"ly":23,"mx":48,"my":24},
{"lx":48,"ly":22,"mx":48,"my":23},
{"lx":48,"ly":21,"mx":48,"my":22},
{"lx":49,"ly":20,"mx":48,"my":21},
{"lx":49,"ly":18,"mx":49,"my":20},
{"lx":49,"ly":17,"mx":49,"my":18},
{"lx":50,"ly":16,"mx":49,"my":17},
{"lx":50,"ly":14,"mx":50,"my":16},
{"lx":50,"ly":13,"mx":50,"my":14},
{"lx":50,"ly":12,"mx":50,"my":13},
{"lx":50,"ly":11,"mx":50,"my":12},
{"lx":51,"ly":11,"mx":50,"my":11},
{"lx":52,"ly":14,"mx":51,"my":11},
{"lx":54,"ly":17,"mx":52,"my":14},
{"lx":55,"ly":19,"mx":54,"my":17},
{"lx":56,"ly":22,"mx":55,"my":19},
{"lx":57,"ly":24,"mx":56,"my":22},
{"lx":58,"ly":26,"mx":57,"my":24},
{"lx":58,"ly":27,"mx":58,"my":26},
{"lx":59,"ly":29,"mx":58,"my":27},
{"lx":60,"ly":31,"mx":59,"my":29},
{"lx":61,"ly":32,"mx":60,"my":31},
{"lx":62,"ly":32,"mx":61,"my":32},
{"lx":87,"ly":29,"mx":87,"my":28},
{"lx":87,"ly":29,"mx":87,"my":29},
{"lx":87,"ly":27,"mx":87,"my":29},
{"lx":87,"ly":25,"mx":87,"my":27},
{"lx":87,"ly":24,"mx":87,"my":25},
{"lx":87,"ly":22,"mx":87,"my":24},
{"lx":86,"ly":20,"mx":87,"my":22},
{"lx":85,"ly":20,"mx":86,"my":20},
{"lx":85,"ly":19,"mx":85,"my":20},
{"lx":84,"ly":19,"mx":85,"my":19},
{"lx":83,"ly":19,"mx":84,"my":19},
{"lx":82,"ly":19,"mx":83,"my":19},
{"lx":80,"ly":19,"mx":82,"my":19},
{"lx":79,"ly":19,"mx":80,"my":19},
{"lx":78,"ly":19,"mx":79,"my":19},
{"lx":76,"ly":19,"mx":78,"my":19},
{"lx":73,"ly":19,"mx":76,"my":19},
{"lx":70,"ly":19,"mx":73,"my":19},
{"lx":69,"ly":19,"mx":70,"my":19},
{"lx":67,"ly":20,"mx":69,"my":19},
{"lx":67,"ly":21,"mx":67,"my":20},
{"lx":66,"ly":21,"mx":67,"my":21},
{"lx":66,"ly":22,"mx":66,"my":21},
{"lx":65,"ly":22,"mx":66,"my":22},
{"lx":64,"ly":24,"mx":65,"my":22},
{"lx":64,"ly":26,"mx":64,"my":24},
{"lx":64,"ly":27,"mx":64,"my":26},
{"lx":63,"ly":29,"mx":64,"my":27},
{"lx":63,"ly":30,"mx":63,"my":29},
{"lx":63,"ly":31,"mx":63,"my":30},
{"lx":63,"ly":32,"mx":63,"my":31},
{"lx":63,"ly":33,"mx":63,"my":32},
{"lx":63,"ly":34,"mx":63,"my":33},
{"lx":65,"ly":35,"mx":63,"my":34},
{"lx":66,"ly":35,"mx":65,"my":35},
{"lx":67,"ly":36,"mx":66,"my":35},
{"lx":68,"ly":37,"mx":67,"my":36},
{"lx":69,"ly":37,"mx":68,"my":37},
{"lx":70,"ly":37,"mx":69,"my":37},
{"lx":72,"ly":38,"mx":70,"my":37},
{"lx":73,"ly":38,"mx":72,"my":38},
{"lx":74,"ly":38,"mx":73,"my":38},
{"lx":76,"ly":39,"mx":74,"my":38},
{"lx":77,"ly":39,"mx":76,"my":39},
{"lx":78,"ly":39,"mx":77,"my":39},
{"lx":79,"ly":39,"mx":78,"my":39},
{"lx":79,"ly":38,"mx":79,"my":39},
{"lx":81,"ly":38,"mx":79,"my":38},
{"lx":82,"ly":38,"mx":81,"my":38},
{"lx":82,"ly":37,"mx":82,"my":38},
{"lx":83,"ly":37,"mx":82,"my":37},
{"lx":84,"ly":37,"mx":83,"my":37},
{"lx":85,"ly":36,"mx":84,"my":37},
{"lx":85,"ly":35,"mx":85,"my":36},
{"lx":86,"ly":34,"mx":85,"my":35},
{"lx":87,"ly":34,"mx":86,"my":34},
{"lx":87,"ly":32,"mx":87,"my":34},
{"lx":87,"ly":31,"mx":87,"my":32},
{"lx":88,"ly":30,"mx":87,"my":31},
{"lx":88,"ly":29,"mx":88,"my":30},
{"lx":88,"ly":28,"mx":88,"my":29},
{"lx":88,"ly":27,"mx":88,"my":28},
{"lx":88,"ly":26,"mx":88,"my":27},
{"lx":88,"ly":25,"mx":88,"my":26},
{"lx":94,"ly":22,"mx":94,"my":21},
{"lx":94,"ly":22,"mx":94,"my":22},
{"lx":96,"ly":20,"mx":94,"my":22},
{"lx":96,"ly":21,"mx":96,"my":20},
{"lx":96,"ly":23,"mx":96,"my":21},
{"lx":96,"ly":24,"mx":96,"my":23},
{"lx":96,"ly":25,"mx":96,"my":24},
{"lx":96,"ly":26,"mx":96,"my":25},
{"lx":96,"ly":28,"mx":96,"my":26},
{"lx":96,"ly":29,"mx":96,"my":28},
{"lx":96,"ly":30,"mx":96,"my":29},
{"lx":96,"ly":31,"mx":96,"my":30},
{"lx":96,"ly":32,"mx":96,"my":31},
{"lx":96,"ly":33,"mx":96,"my":32},
{"lx":97,"ly":34,"mx":96,"my":33},
{"lx":98,"ly":34,"mx":97,"my":34},
{"lx":99,"ly":35,"mx":98,"my":34},
{"lx":99,"ly":36,"mx":99,"my":35},
{"lx":101,"ly":36,"mx":99,"my":36},
{"lx":102,"ly":36,"mx":101,"my":36},
{"lx":103,"ly":36,"mx":102,"my":36},
{"lx":104,"ly":36,"mx":103,"my":36},
{"lx":105,"ly":36,"mx":104,"my":36},
{"lx":105,"ly":37,"mx":105,"my":36},
{"lx":107,"ly":37,"mx":105,"my":37},
{"lx":108,"ly":37,"mx":107,"my":37},
{"lx":109,"ly":37,"mx":108,"my":37},
{"lx":109,"ly":36,"mx":109,"my":37},
{"lx":110,"ly":34,"mx":109,"my":36},
{"lx":111,"ly":34,"mx":110,"my":34},
{"lx":111,"ly":33,"mx":111,"my":34},
{"lx":111,"ly":32,"mx":111,"my":33},
{"lx":112,"ly":32,"mx":111,"my":32},
{"lx":112,"ly":31,"mx":112,"my":32},
{"lx":112,"ly":30,"mx":112,"my":31},
{"lx":112,"ly":29,"mx":112,"my":30},
{"lx":113,"ly":29,"mx":112,"my":29},
{"lx":113,"ly":28,"mx":113,"my":29},
{"lx":113,"ly":27,"mx":113,"my":28},
{"lx":113,"ly":26,"mx":113,"my":27},
{"lx":113,"ly":25,"mx":113,"my":26},
{"lx":113,"ly":23,"mx":113,"my":25},
{"lx":114,"ly":23,"mx":113,"my":23},
{"lx":114,"ly":22,"mx":114,"my":23},
{"lx":114,"ly":21,"mx":114,"my":22},
{"lx":114,"ly":20,"mx":114,"my":21},
{"lx":137,"ly":21,"mx":137,"my":20},
{"lx":137,"ly":21,"mx":137,"my":21},
{"lx":137,"ly":18,"mx":137,"my":21},
{"lx":137,"ly":17,"mx":137,"my":18},
{"lx":134,"ly":17,"mx":137,"my":17},
{"lx":132,"ly":17,"mx":134,"my":17},
{"lx":130,"ly":16,"mx":132,"my":17},
{"lx":129,"ly":16,"mx":130,"my":16},
{"lx":128,"ly":16,"mx":129,"my":16},
{"lx":126,"ly":16,"mx":128,"my":16},
{"lx":125,"ly":16,"mx":126,"my":16},
{"lx":124,"ly":16,"mx":125,"my":16},
{"lx":124,"ly":17,"mx":124,"my":16},
{"lx":122,"ly":17,"mx":124,"my":17},
{"lx":121,"ly":18,"mx":122,"my":17},
{"lx":120,"ly":18,"mx":121,"my":18},
{"lx":119,"ly":20,"mx":120,"my":18},
{"lx":117,"ly":20,"mx":119,"my":20},
{"lx":117,"ly":21,"mx":117,"my":20},
{"lx":116,"ly":21,"mx":117,"my":21},
{"lx":116,"ly":23,"mx":116,"my":21},
{"lx":115,"ly":24,"mx":116,"my":23},
{"lx":114,"ly":26,"mx":115,"my":24},
{"lx":113,"ly":27,"mx":114,"my":26},
{"lx":113,"ly":28,"mx":113,"my":27},
{"lx":115,"ly":28,"mx":113,"my":28},
{"lx":117,"ly":28,"mx":115,"my":28},
{"lx":118,"ly":28,"mx":117,"my":28},
{"lx":119,"ly":28,"mx":118,"my":28},
{"lx":120,"ly":28,"mx":119,"my":28},
{"lx":121,"ly":28,"mx":120,"my":28},
{"lx":123,"ly":28,"mx":121,"my":28},
{"lx":125,"ly":28,"mx":123,"my":28},
{"lx":126,"ly":28,"mx":125,"my":28},
{"lx":127,"ly":28,"mx":126,"my":28},
{"lx":128,"ly":28,"mx":127,"my":28},
{"lx":129,"ly":28,"mx":128,"my":28},
{"lx":130,"ly":28,"mx":129,"my":28},
{"lx":130,"ly":29,"mx":130,"my":28},
{"lx":131,"ly":29,"mx":130,"my":29},
{"lx":131,"ly":30,"mx":131,"my":29},
{"lx":132,"ly":30,"mx":131,"my":30},
{"lx":132,"ly":32,"mx":132,"my":30},
{"lx":132,"ly":33,"mx":132,"my":32},
{"lx":133,"ly":34,"mx":132,"my":33},
{"lx":133,"ly":35,"mx":133,"my":34},
{"lx":133,"ly":36,"mx":133,"my":35},
{"lx":133,"ly":37,"mx":133,"my":36},
{"lx":132,"ly":38,"mx":133,"my":37},
{"lx":130,"ly":38,"mx":132,"my":38},
{"lx":129,"ly":38,"mx":130,"my":38},
{"lx":128,"ly":38,"mx":129,"my":38},
{"lx":127,"ly":38,"mx":128,"my":38},
{"lx":126,"ly":37,"mx":127,"my":38},
{"lx":125,"ly":37,"mx":126,"my":37},
{"lx":124,"ly":37,"mx":125,"my":37},
{"lx":123,"ly":37,"mx":124,"my":37},
{"lx":122,"ly":37,"mx":123,"my":37},
{"lx":121,"ly":37,"mx":122,"my":37},
{"lx":120,"ly":37,"mx":121,"my":37},
{"lx":144,"ly":20,"mx":144,"my":19},
{"lx":144,"ly":20,"mx":144,"my":20},
{"lx":145,"ly":20,"mx":144,"my":20},
{"lx":145,"ly":22,"mx":145,"my":20},
{"lx":145,"ly":23,"mx":145,"my":22},
{"lx":144,"ly":23,"mx":145,"my":23},
{"lx":144,"ly":24,"mx":144,"my":23},
{"lx":144,"ly":25,"mx":144,"my":24},
{"lx":144,"ly":26,"mx":144,"my":25},
{"lx":144,"ly":27,"mx":144,"my":26},
{"lx":143,"ly":27,"mx":144,"my":27},
{"lx":143,"ly":29,"mx":143,"my":27},
{"lx":143,"ly":30,"mx":143,"my":29},
{"lx":142,"ly":31,"mx":143,"my":30},
{"lx":142,"ly":32,"mx":142,"my":31},
{"lx":142,"ly":33,"mx":142,"my":32},
{"lx":142,"ly":34,"mx":142,"my":33},
{"lx":142,"ly":35,"mx":142,"my":34},
{"lx":144,"ly":35,"mx":142,"my":35},
{"lx":145,"ly":35,"mx":144,"my":35},
{"lx":146,"ly":36,"mx":145,"my":35},
{"lx":147,"ly":36,"mx":146,"my":36},
{"lx":148,"ly":36,"mx":147,"my":36},
{"lx":149,"ly":36,"mx":148,"my":36},
{"lx":150,"ly":36,"mx":149,"my":36},
{"lx":151,"ly":36,"mx":150,"my":36},
{"lx":152,"ly":36,"mx":151,"my":36},
{"lx":154,"ly":36,"mx":152,"my":36},
{"lx":155,"ly":36,"mx":154,"my":36},
{"lx":156,"ly":36,"mx":155,"my":36},
{"lx":157,"ly":36,"mx":156,"my":36},
{"lx":158,"ly":36,"mx":157,"my":36},
{"lx":159,"ly":36,"mx":158,"my":36},
{"lx":160,"ly":36,"mx":159,"my":36},
{"lx":159,"ly":36,"mx":160,"my":36},
{"lx":146,"ly":28,"mx":146,"my":27},
{"lx":146,"ly":28,"mx":146,"my":28},
{"lx":147,"ly":27,"mx":146,"my":28},
{"lx":149,"ly":27,"mx":147,"my":27},
{"lx":152,"ly":27,"mx":149,"my":27},
{"lx":153,"ly":27,"mx":152,"my":27},
{"lx":154,"ly":27,"mx":153,"my":27},
{"lx":156,"ly":27,"mx":154,"my":27},
{"lx":145,"ly":23,"mx":145,"my":22},
{"lx":145,"ly":23,"mx":145,"my":23},
{"lx":146,"ly":22,"mx":145,"my":23},
{"lx":148,"ly":22,"mx":146,"my":22},
{"lx":155,"ly":20,"mx":148,"my":22},
{"lx":157,"ly":20,"mx":155,"my":20},
{"lx":158,"ly":20,"mx":157,"my":20},
{"lx":159,"ly":20,"mx":158,"my":20},
{"lx":161,"ly":20,"mx":159,"my":20},
{"lx":164,"ly":21,"mx":161,"my":20},
{"lx":166,"ly":21,"mx":164,"my":21},
{"lx":168,"ly":21,"mx":166,"my":21},
{"lx":169,"ly":21,"mx":168,"my":21},
{"lx":170,"ly":21,"mx":169,"my":21}]


# Padding to apply
padding = Padding(20, 20, 20, 20)
# Generate an image with the default size (based on the signature lines)
size = None # (198, 50)
line_color = '#03c'
line_width = 2
image = create_image(sample, size, padding, line_color=line_color,
                     line_width=line_width)
# Show it!
image.show()
