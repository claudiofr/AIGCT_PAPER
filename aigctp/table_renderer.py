import os


class TableRenderer:
    def __init__(self, output_dir):
        self._outdir = output_dir

    def align_left(self, s):
        return ['text-align: left' for _ in s]

    def render_label_stats(self, label_stats, file_name):
        styles = [{'selector': 'th, td',
                    'props': [
                          ('text-align', 'right'),
                          ('padding', '100px'),
                          ('margin', '5px'),
                          ('border', '1px solid black')]},
                    {'selector': 'table',
                    'props': [
                          ('border-collapse', 'separate'),
                          ('border-spacing', '15px 5px')]},
                    {'selector': 'tbody',
                         'props': [('text-align', 'right')]}
                ]
        styles = [{'selector': 'th, td',
                    'props': [
                          ('text-align', 'right'),
                          ('padding', '10px'),
                          ('margin', '5px'),
                          ]},
                    {'selector': 'table',
                    'props': [
                          ('border-collapse', 'separate'),
                          ('border-spacing', '15px 5px')]},
                ]
        styles = [{'selector': 'th, td',
                    'props': [
                          ('text-align', 'right'),
                          ('padding', '5px'),
                          ('margin', '1px'),
                          ]},
                    {'selector': 'table',
                    'props': [
                          ('border-collapse', 'separate'),
                          ('border-spacing', '15px')]},
                ]
        styles1 = [
            {'selector': 'th',
             'props': [('text-align', 'center'),
                       ('border-collapse', 'separate'), 
                       ('border-spacing', '100px')]}, # Adjust '20px' to your desired spacing
            {'selector': 'tbody',
             'props': [('text-align', 'right'),
                       ('border-collapse', 'separate'), 
                       ('border-spacing', '100px')]} # Adjust '20px' to your desired spacing
        ]
        styles = [{'selector': 'table',
                   'props': [
                       ('background-color', 'whitesmoke')
                   ]},
            {'selector': 'td',
                    'props': [
                          #('text-align', 'right'),
                          # ('padding', '5px'),
                          # ('margin', '1px'),
                          # ('background-color',  'whitesmoke'),
                          ]},
                    {'selector': 'th',
                     'props': [('border-bottom', '1px solid black'),
                              ('text-align', 'center'),]},
                     {'selector': 'th, td',
                      'props': [('background-color','whitesmoke'),
                                ('border-color', '5px black')
                                ]},
                    {'selector': 'td',
                     'props': [('padding', '5px solid black')]},
                     {'selector': 'caption',
                      'props': [('font-size','125%'),
                                ('margin-bottom', '15px')]}
                ]
        style = (label_stats.style.set_table_styles(styles).hide()
            .relabel_index(
            ["Task", "Variant Total", "(+) Labels", "(-) Labels",
             "Genes", "VEPs"], axis=1).set_caption(
            "Variant, Gene, and VEP Counts by Task"))
        #style = style.apply(self.align_left, subset=["TASK_CODE"])
        #style = style.apply(self.align_left, subset=["TASK_CODE"])
        style = style.set_properties(subset=["TASK_CODE"], **{"text-align": "left"})
        style = style.set_properties(
            subset=["NUM_VARIANTS",
            "NUM_POSITIVE_LABELS", "NUM_NEGATIVE_LABELS",
            "NUM_GENES", "NUM_SCORE_SOURCES"], **{"text-align": "right"})
        #style = style.set_properties(**{'border-color': 'whitesmoke'})
        file_name = os.path.join(self._outdir, file_name)
        style.to_html(file_name)

