#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2014 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

from gnuradio import gr
from gnuradio import blocks

class file_source2(gr.hier_block2):
    """
    docstring for block file_source2
    """
    def __init__(self, itemsize, filename):
        gr.hier_block2.__init__(self,
            "file_source2",
        gr.io_signature(0, 0, 0),
        gr.io_signature2(2, 2, itemsize[0], itemsize[1]))

        self.file_source0 = blocks.file_source(
                itemsize=itemsize[0],
                filename=filename[0]
        )
        
        self.file_source1 = blocks.file_source(
                itemsize=itemsize[1],
                filename=filename[1]
        )

        self.connect(self.file_source0, (self, 0))
        self.connect(self.file_source1, (self, 1))
