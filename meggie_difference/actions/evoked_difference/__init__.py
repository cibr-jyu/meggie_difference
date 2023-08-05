from meggie.utilities.messaging import messagebox
from meggie.utilities.threading import threaded
from meggie.mainwindow.dynamic import Action
from meggie.mainwindow.dynamic import subject_action

from meggie_difference.utilities.dialogs.differenceDialogMain import DifferenceDialog

class EvokedDifference(Action):
    """ Creates a difference object.
    """

    @subject_action
    def handler(self, subject, params):
        """
        """
        @threaded
        def difference_fun():
            pass

        difference_fun(do_meanwhile=self.window.update_ui)
        subject.save()

    def run(self):
        subject_name = self.experiment.active_subject.name

        conditions = []

        difference_dialog = DifferenceDialog(
            self.window, self.experiment, conditions, self.handler)
        difference_dialog.show()
