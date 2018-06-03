"""
Factitious CA to test non-uniform buffer interactions.

Experiment classes included.

"""
from xentica import core
from xentica import seeds
from xentica.core import color_effects
from xentica.core.variables import DeferredExpression


class ShiftingSands(core.CellularAutomaton):
    """
    CA for non-uniform buffer interactions test.

    It emits the whole value to a constant direction, then absorbs
    surrounding values by summing them.

    """

    state = core.IntegerProperty(max_val=1)

    class Topology:
        """2D Moore neighborhood, wrapped to a 3-torus."""

        dimensions = 2
        lattice = core.OrthogonalLattice()
        neighborhood = core.MooreNeighborhood()
        border = core.TorusBorder()

    def emit(self):
        """Emit the whole value to a constant direction."""
        direction = 0
        for i in range(len(self.buffers)):
            if i == direction:
                self.buffers[i].state = self.main.state
            else:
                # TODO: direct assignment ``self.buffers[i].state = 0``
                self.buffers[i].state = DeferredExpression("0")

    def absorb(self):
        """Absorb surrounding values by summing them."""
        new_val = core.IntegerVariable()
        for i in range(len(self.buffers)):
            new_val += self.neighbors[i].buffer.state
        # TODO: direct assignment ``self.main.state = new_val``
        self.main.state = new_val + 0 * self.main.state

    @color_effects.MovingAverage
    def color(self):
        """Render contrast black & white cells."""
        r = self.main.state * 255
        g = self.main.state * 255
        b = self.main.state * 255
        return (r, g, b)


class ShiftingSandsExperiment(core.Experiment):
    """Vanilla experiment with randomly initialized area."""

    word = "LET IT SHIFT"
    size = (640, 360, )
    zoom = 3
    pos = [0, 0]
    seed = seeds.patterns.BigBang(
        pos=(320, 180),
        size=(100, 100),
        vals={
            "state": seeds.random.RandInt(0, 1),
        }
    )


def main():
    import moire
    ca = ShiftingSands(ShiftingSandsExperiment)
    gui = moire.GUI(runnable=ca)
    gui.run()


if __name__ == "__main__":
    main()