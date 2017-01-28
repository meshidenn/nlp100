# -*- coding: utf-8 -*-

import pydot

edges=[(1,2), (1,3), (1,4), (3,4)]
g=pydot.graph_from_edges(edges)
g.write_jpeg('graph_from__dot.jpg', prog='dot')
