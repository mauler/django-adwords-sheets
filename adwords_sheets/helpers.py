#!/usr/bin/env python
#-*- coding:utf-8 -*-

import csv


CSV_HEAD_TRANSLATE = {
    'Dia': "date",
    'Status da campanha': 'campaign_state',
    'Campanha': 'campaign',
    'Or\xc3\xa7amento': 'budget',
    'Status': 'budget_status',
    'Cliques': 'clicks',
    'Impress\xc3\xb5es': 'impressions',
    'CTR': 'ctr',
    'CPC m\xc3\xa9dio': 'avg_cpc',
    'Custo': 'cost',
    'Posi\xc3\xa7\xc3\xa3o m\xc3\xa9d.': 'avg_position',
    'Marcadores': 'labels'
}


# TODO: Colocar no django-cemese
def csv2rows(csvfile):
    reader = csv.reader(csvfile)
    rows = [i for i in reader][1:-4]
    head = rows[0]
    csvrows = rows[1:]
    index2key = {}
    key2index = {}
    for index, cell in enumerate(head):
        index2key[index] = CSV_HEAD_TRANSLATE[cell]
        key2index[cell] = index
    rows = []
    for row in csvrows:
        values = {}
        for index, cell in enumerate(row):
            values[index2key[index]] = cell
        rows.append(values)
    return rows


if __name__ == "__main__":
    import doctest
    doctest.testmod()

