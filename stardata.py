import numpy
import pandas

class DataGenerator(object):

    def create_dimension(self, d_specs, num):

        columns = [item for item in d_specs]
        rows = [num for num in range(1, num)]

        df_dim = pandas.DataFrame(columns = columns[::-1], index = rows)

        for key in columns:
            df_dim[key].ix[:] = d_specs[key]

        return df_dim

    def create_fact(self, d_fact_specs, num):

        columns = [item for item in d_fact_specs]
        #columns.append('date')
        rows = [num for num in range(1,num+1)]

        df_fact = pandas.DataFrame(columns = columns, index = rows)

        for key in columns:
            df_fact[key].ix[:] = d_fact_specs[key]

        return df_fact


if __name__ == '__main__':

    data = DataGenerator()

    # 10 million customers
    num_cust = 10000000
    d_cust = {
        'key': range(1, num_cust),
        'id': [str('C'+str(item)) for item in range(1, num_cust)]
        #'cust_geo': ['NE','NW','SE','SW','MW']
    }

    # 2 million products
    num_prod = 2000000
    d_prod = {
        'key': range(1, num_prod),
        'id': [str('P'+str(item)) for item in range(1, num_prod)]
    }


    df_cust = data.create_dimension(d_cust, num_cust)
    df_cust.to_csv('dimcust.csv', header=['key','id'], index=False)

    df_prod = data.create_dimension(d_prod, num_prod)
    df_prod.to_csv('dimprod.csv', header=['key','id'], index=False)

    # 50 million orders daily
    fact_rows = 5000000
    date = ['20150105']

    for date in date:
        d_fact = {
            #'fact_columns' : ['cust_key', 'prod_key', 'date', 'qty_ordered', 'unit_price'],
            'cust_key': list(numpy.random.randint(1, num_cust, size=fact_rows)),
            'prod_key': list(numpy.random.randint(1, num_prod, size=fact_rows)),
            'qty_ordered': list(numpy.random.randint(1, 25, size=fact_rows)),
            'unit_price': list(numpy.random.randint(10, 500, size=fact_rows)),
            'date': [date]*fact_rows
        }

        df_orders = data.create_fact(d_fact, fact_rows)
        df_orders.to_csv('factorders_'+str(date)+'.csv', index=False)

    #print d_fact['cust_key']
    #print len(d_cust)
    #print [item for item in d_cust]

