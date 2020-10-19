import matplotlib.pyplot as plt

# def add_labelplot(fig, title, xlabel=False, fontsize=8):
#     ax = fig.add_subplot(111, frameon=False)
#
#     secaxy = ax.secondary_yaxis('right')
#
#     secaxy.set_ylabel(title, labelpad=8)
#     secaxy.set_yticklabels([])
#
#     plt.tick_params(labelcolor='none', top=False, bottom=False, left=False, right=False)
#     plt.ylabel(label_ct)
#
#     return ax
#
# # Get handles and labels from last subplot.
# handles, labels = plt.gca().get_legend_handles_labels()
#
# # Add a new subplot for x and y labels.
# ax = add_labelplot(fig, title, show_xlabel)
#
# if legend:
#     factor = 1.3
#     new_height = size[1] * factor
#
#     fig.set_size_inches(size[0], new_height)
#
#     # Fix margins.
#     topmargin = (-size[1] * (1 - margins['top']) + new_height) / new_height
#     bottommargin = (-size[1] * (1 - margins['bottom']) + new_height) / new_height
#
#     margins['top'] = topmargin
#     margins['bottom'] = bottommargin
#
#     ax.legend(handles, labels, ncol=3, loc='center', bbox_to_anchor=(0.5, -0.5), fontsize=8)
