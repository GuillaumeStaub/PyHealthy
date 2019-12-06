import click
from install.progress_bar import ProgressBar
from install import install as install_main
from user_interface.menu import main as menu_main

@click.command()
@click.option('--count', default = 100,show_default=True, type=int ,help ="Number of product by category")
@click.option('--install', is_flag=True, help='Permet d\'installer les packages')
def main(install, count):
    """Command to initialize the database.
     By default the program starts but always checks
     if the database is initialized.
    """
    if install:
        install_main.main(count)
    else:
        menu_main()
        


if __name__ == "__main__":
    main()