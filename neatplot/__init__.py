"""
Neat plotting utilities for Python.
"""

__version__ = "0.1.0"

import pathlib
from typing import Union, Any, NoReturn

import matplotlib.pyplot as plt
from matplotlib.figure import Figure


def set_style(style_str: str = 'default') -> NoReturn:
    """Set the matplotlib plotting style.

    Args:
        style_str: string for style file.
    """
    if style_str == 'default':
        plt.style.use((pathlib.Path(__file__).parent / 'matplotlibrc').resolve())
    elif style_str == 'fonts':
        plt.style.use((pathlib.Path(__file__).parent / 'matplotlibrc_fonts').resolve())
    elif style_str == 'notex':
        set_style()
        update_rc_notex()
    elif style_str == 'fontsnotex':
        set_style('fonts')
        update_rc_notex()


def save_figure(
    file_name: str = 'figure',
    ext_list: Union[list, str, None] = 'png',
    fig: Figure = None,
    white_background: bool = True,
) -> NoReturn:
    """Save matplotlib figure for all extensions in ext_list.

    Args:
        file_name: name of saved image file.
        ext_list: list of strings (or single string) denoting file type.
        fig: matplotlib Figure.
        white_background: set background of image to white if True.
    """

    # If 'all' keyword, use all extensions
    if ext_list == 'all':
        ext_list = ['pdf', 'png', 'svg']

    # If ext_list is a single str
    if isinstance(ext_list, str):
        ext_list = [ext_list]

    # Set facecolor and edgecolor
    (fc, ec) = ('w', 'w') if white_background else ('none', 'none')

    # Save each type in ext_list
    pre = fig if fig else plt
    for ext in ext_list:
        save_str = file_name + '.' + ext
        pre.savefig(save_str, bbox_inches='tight', facecolor=fc, edgecolor=ec)
        print(f'Saved figure {save_str}')


def update_rc(key_str: str, value: Any) -> NoReturn:
    """Update matplotlibrc parameters.

    Args:
        key_str: string for a matplotlibrc parameter.
        value: associated value to set the matplotlibrc parameter.
    """
    plt.rcParams.update({key_str: value})


def update_rc_notex() -> NoReturn:
    """Update matplotlibrc parameters for running without latex."""
    update_rc('text.usetex', False)
    update_rc('mathtext.fontset', 'stix')
