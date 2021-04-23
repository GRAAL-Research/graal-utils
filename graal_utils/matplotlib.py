import os
try:
    import matplotlib.pyplot as plt
except ImportError:
    plt = None

DEFAULT_EXTENSIONS = ('pdf', 'png')

def save_and_close_figure(fig, save_path, name, extensions=DEFAULT_EXTENSIONS):
    if plt is None:
        raise ImportError("Matplotlib does not seem to be installed.")

    for ext in extensions:
        fig.savefig(os.path.join(save_path, f'{name}.{ext}'))
    plt.close(fig)
