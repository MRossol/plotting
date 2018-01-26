"""
Plotting dataframe data with seaborn and pandas
"""
import itertools
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def pivot_timeseries(df, var_name, timezone=None):
    sns_df = []
    for name, col in df.iteritems():
        col = col.to_frame()
        col.columns = [var_name]
        col['source'] = name
        col['year'] = col.index.year
        col['month'] = col.index.month
        col['hour'] = col.index.hour
        if timezone is not None:
            td = pd.to_timedelta('{:}h'.format(timezone))
            col['local_hour'] = (col.index + td).hour

        sns_df.append(col)

    return pd.concat(sns_df)


def df_base(plot_func, *args, despine=True,
            figsize=(6, 5), dpi=100, fontsize=14,
            xlabel=None, ylabel=None, xlim=None, ylim=None,
            xticks=None, yticks=None, ticksize=(6, 1),
            xtick_labels=None, ytick_labels=None, borderwidth=1,
            title=None, legend=True, filename=None, **kwargs):
    """
    Parameters
    ----------
    plot_func : 'function'
        Plotting function
    * args
        Args for plot_func
    despine : 'bool'
        Despine axis in seaborn
    figsize : 'Tuple', default = '(8,6)'
        Width and height of figure
    dpi : 'Int', default = '100'
        DPI resolution of figure.
    fontsize : 'Int'
        Font size to be used for axes labels, ticks will be 2 points smaller
    xlabel : 'String'
        Label for x-axis.
    ylabel : 'String'
        Label for y-axis.
    xlim : 'tuple', len(xlim) == 2
        Upper and lower limits for the x-axis.
    ylim : 'tuple', len(ylim) == 2
        Upper and lower limits for the y-axis.
    xticks : 'ndarray'
        List of ticks to use on the x-axis. Should be within the bounds set by
        xlim.
    yticks : 'ndarray'
        List of ticks to use on the y-axis. Should be within the bound set by
        ylim.
    ticksize : 'ndarray', default '[8,2]'
        Length and width of ticks.
    xtick_labels : 'list'
        List of custome xticks. Note len(xticks) == len(xtick_labels)
    ytick_labels : 'list'
        List of custome yticks. Note len(yticks) == len(ytick_labels)
    boarderwidth : 'Int'
        Linewidth of plot frame
    title : 'str'
        Plot title
    legend : 'Bool'|'list'
        If True, use df labels, or list of legend labels
    filename : 'String', default = None.
        Name of file/path to save the figure to.
    **kwargs
        kwargs for plot_func
    """
    fig = plt.figure(figsize=figsize, dpi=dpi)
    axis = fig.add_subplot(111)

    plot_func(axis, *args, **kwargs)

    if despine:
        sns.despine(offset=10, trim=False)

    if title is not None:
        axis.set_title(title, fontsize=fontsize + 2)

    if xlabel is not None:
        axis.set_xlabel(xlabel, fontsize=fontsize)
    else:
        axis.xaxis.label.set_size(fontsize)

    if ylabel is not None:
        axis.set_ylabel(ylabel, fontsize=fontsize)
    else:
        axis.yaxis.label.set_size(fontsize)

    if xlim is not None:
        axis.set_xlim(xlim)

    if ylim is not None:
        axis.set_ylim(ylim)

    axis.tick_params(axis='both', labelsize=fontsize - 2,
                     width=ticksize[1], length=ticksize[0])

    if xticks is not None:
        axis.set_xticks(xticks)
        if xtick_labels is not None:
            axis.set_xticklabels(xtick_labels)

    if yticks is not None:
        axis.set_yticks(yticks)
        if ytick_labels is not None:
            axis.set_yticklabels(ytick_labels)

    for ax in ['top', 'bottom', 'left', 'right']:
        axis.spines[ax].set_linewidth(borderwidth)

    if legend:
        if isinstance(legend, list):
            plt.legend(legend, bbox_to_anchor=(1.05, 1), loc=2,
                       borderaxespad=0., prop={'size': fontsize - 2})
        else:
            plt.legend(bbox_to_anchor=(1.05, 1), loc=2,
                       borderaxespad=0., prop={'size': fontsize - 2})

    fig.tight_layout()
    if filename is not None:
        plt.savefig(filename, dpi=dpi, transparent=True,
                    bbox_inches='tight')
    else:
        plt.show()

    plt.close()

def box_plot(df, **kwargs):
    def plot_func(axis, df, **kwargs):
        meanprops = dict(marker='o', markeredgecolor='black',
                         markerfacecolor="None", markersize=5)
        sns.boxplot(data=df, ax=axis, meanprops=meanprops, **kwargs)

    df_base(plot_func, df, **kwargs)


def dist_plot(df, **kwargs):
    def plot_func(axis, df, **kwargs):
        fit = kwargs.get('fit', None)
        del kwargs['fit']
        palette = itertools.cycle(sns.color_palette())
        if isinstance(df, pd.DataFrame):
            for label, series in df. iteritems():
                if fit is not None:
                    sns.distplot(series, kde=False, fit=fit,
                                 fit_kws={"color": next(palette)},
                                 label=label, **kwargs)
                else:
                    sns.distplot(series, label=label, **kwargs)
        else:
            if fit is not None:
                sns.distplot(df, kde=False, fit=fit,
                             fit_kws={"color": next(palette)},
                             **kwargs)
            else:
                sns.distplot(df, **kwargs)

    df_base(plot_func, df, **kwargs)


def point_plot(df, **kwargs):
    def plot_func(axis, df, **kwargs):
        sns.pointplot(data=df, ax=axis, **kwargs)

    df_base(plot_func, df, **kwargs)


def bar_plot(df, **kwargs):
    def plot_func(axis, df, **kwargs):
        sns.barplot(data=df, ax=axis, **kwargs)

    df_base(plot_func, df, **kwargs)


def ts_plot(df, **kwargs):
    def plot_func(axis, df, **kwargs):
        df.plot(ax=axis, **kwargs)

    df_base(plot_func, df, **kwargs)
