print('AAAAAA')

import matplotlib
matplotlib.use('pgf')

import matplotlib.pyplot as plt

plt.rcParams.update({
    'backend': 'pgf',
    'pgf.texsystem': 'lualatex',
    'font.family': "serif",
    'text.usetex': True,
    # "pgf.rcfonts": False,
    # 'text.latex.preamble': r"\usepackage{lmodern}",
    'font.size': 5,
    'figure.dpi': 300
})
