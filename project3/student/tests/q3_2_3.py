test = {   'name': 'q3_2_3',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> # this test just checks that your classify_feature_row works correctly.;\n'
                                               '>>> def check(r):\n'
                                               '...     t = test_my_features.row(r)\n'
                                               "...     return classify(t, train_my_features, train_movies.column('Genre'), 13) == classify_feature_row(t);\n"
                                               '>>> all([check(i) for i in np.arange(13)])\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
