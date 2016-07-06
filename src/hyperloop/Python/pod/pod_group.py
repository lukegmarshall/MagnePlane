"""
Group for Pod components containing the following components:
Vehicle Cycle, Pod Mach (Aero), DriveTrain group, Geometry, Levitation group, and Weight
"""
from openmdao.api import Group
from hyperloop.Python.pod.pod_mass import PodMass
from hyperloop.Python.pod.drivetrain.Drivetrain import Drivetrain
from hyperloop.Python.pod.compressor_mass import CompressorMass
from hyperloop.Python.pod.cycle_vehicle import CompressionCycle
from hyperloop.Python.pod.pod_geometry import PodGeometry
from hyperloop.Python.pod.magnetic_levitation.levitation_group import LevGroup


class PodGroup(Group):

    def __init__(self):
        super(PodGroup, self).__init__()

        self.add('pod_mass', PodMass())
        self.add('drivetrain', Drivetrain())
        self.add('levitation_group', LevGroup())
        self.add('compressor_mass', CompressorMass)
        self.add('compression_cycle', CompressionCycle)
        self.add('pod_geometry', PodGeometry)

        self.connect('compression_cycle.shaft.Nmech', 'drivetrain.motor.speed')

if __name__ == "__main__":

    prob = Problem()
    root = prob.root = Group()

    prob.setup()
    prob.root.list_connections()
    prob.run()

    print('Tube Temperature: %f' % prob['Tube.Thermal.tubetemp'])
    print(':%f' % prob['Cycle.'])
    print(':%f' % prob['Aero.'])
    print('%f' % prob['Geometry.'])
    print('%f' % prob['LevGroup.'])
    print('%f' % prob['Weight.'])