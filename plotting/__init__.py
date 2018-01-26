from .lines import (COLORS, riffle_lines, get_COLORS,
                    line_plot, error_plot, dual_plot)
from .dataframes import (pivot_timeseries, box_plot, point_plot, dist_plot,
                         bar_plot, ts_plot)

import matplotlib as mpl
import seaborn as sns

sns.set_style("white")
sns.set_style("ticks")
mpl.rcParams['font.sans-serif'] = 'Arial'
mpl.rcParams['pdf.fonttype'] = 42
