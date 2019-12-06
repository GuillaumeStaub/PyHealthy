from threading import Thread
from time import sleep
from tqdm import tqdm


class ProgressBar(Thread):
    """This class inherits the Thread class.
      Indeed this package allows to manage a loading bar.
      This loading bar rotates in the background
      (hence the interest of Thread to make multitasking),
      during this time the program performs the installation
      (data download, cleaning, creation tables, insert table ...).
       The loading time is calculated on the average rate of treatment
        of a single product.

    Args:
        Thread (class): Allows parallel programming
    """

    def __init__(self, count):
        """time_progressbar is the calculation made for the treatment of a product.
         Killed makes it possible to interrupt the thread in case of error
          encountered during the script

        Args:
            count (int): Number of products requested
        """
        super().__init__()
        self.time_progressbar = int((0.05*count)*2)
        self.killed = False

    def run(self):
        """A loop that runs a number of times predefined by self.time_progressbar
         each turn the bar advances.
        """
        for _ in tqdm(range(self.time_progressbar),
                      desc="Téléchargement des données en cours"):
            if not self.killed:
                sleep(0.5)
            else:
                break

    def kill(self):
        """Method that stops the load bar in case of an error.
        """
        self.killed = True


if __name__ == "__main__":
    pass
