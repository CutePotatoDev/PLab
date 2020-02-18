import plotille


class Plot(plotille.Figure):
    def __init__(self, width=None, height=None, legend=False):
        """ Simple plot's maker.
        """
        super().__init__()

        if width is not None:
            self.width = width

        if height is not None:
            self.height = height

        self.color_mode = 'byte'
        self._legend = legend

    def __str__(self):
        return self.show(self._legend)
