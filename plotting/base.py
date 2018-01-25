import matplotlib.pyplot as plt
import seaborn as sns


def plotting_base(plot_func, *args, despine=True,
                  figsize=(6, 5), dpi=100, fontsize=14,
                  xlabel=None, ylabel=None, xlim=None, ylim=None,
                  xticks=None, yticks=None, ticksize=(6, 1),
                  xtick_labels=None, ytick_labels=None, borderwidth=1,
                  title=None, add_legend=True, filename=None, **kwargs):
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
    add_legend : 'Bool', default = 'False'
        If 'True' a legend will be added at 'legendlocation'.
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

    if add_legend:
        if isinstance(add_legend, list):
            plt.legend(add_legend, bbox_to_anchor=(1.05, 1), loc=2,
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
