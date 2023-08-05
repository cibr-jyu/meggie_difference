from meggie.utilities.messaging import messagebox
from meggie.mainwindow.dynamic import Action

class Difference(Action):
    """ Creates a difference object.
    """
    def run(self):
        subject_name = self.experiment.active_subject.name

        message = 'Hello {}!'.format(subject_name)
        messagebox(self.window, message)
