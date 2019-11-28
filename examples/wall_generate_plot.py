from math import pi

from compas.geometry import Rotation

import compas_assembly

from compas_assembly.datastructures import Assembly
from compas_assembly.datastructures import assembly_transform
from compas_assembly.plotter import AssemblyPlotter

FILE = compas_assembly.get('wall.json')

assembly = Assembly.from_json(FILE)

R = Rotation.from_axis_and_angle([1.0, 0, 0], -pi / 2)
assembly_transform(assembly, R)

plotter = AssemblyPlotter(assembly, figsize=(16, 6), tight=True)
plotter.assembly_plotter.defaults['vertex.fontsize'] = 10

plotter.draw_blocks(
    edgecolor='#444444',
    edgewidth=0.5
)
plotter.show()
