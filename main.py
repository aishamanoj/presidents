import pandas as pd
import re

#please change file path for each data set before running
presidents = pd.read_excel(
    r'/Users/eliang/Desktop/Final Project/econ and president data/Presidents.xls')
gdp = pd.read_csv(
    r'/Users/eliang/Desktop/Final Project/econ and president data/gdp.csv')
cpi = pd.read_csv(r'/Users/eliang/Desktop/Final Project/econ and president data/cpi.csv')
ue = pd.read_csv(r'/Users/eliang/Desktop/Final Project/econ and president data/ue.csv')

# clean presidents data
presidents_df = presidents.drop(
    columns=['Age at inauguration', 'State elected from', '# of electoral votes', '# of popular votes',
             'National total votes', 'Total electoral votes', 'Rating points', 'Occupation', 'College',
             '% electoral', '% popular'])


fi
def list2string(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    return str1.join(s)


def gdp_math(start_date, end_date):
    start_subdf = gdp.loc[gdp['DATE'] == start_date]
    start_gdp_val = int(start_subdf['GDPC1'].values)
    end_subdf = gdp.loc[gdp['DATE'] == end_date]
    end_gdp_val = int(end_subdf['GDPC1'].values)
    if end_gdp_val > start_gdp_val:
        return True
    else:
        return False




def cpi_math(start_date, end_date):
    start_subdf = cpi.loc[cpi['DATE'] == start_date]
    start_cpi_val = int(start_subdf['CPIAUCSL'].values)
    end_subdf = cpi.loc[cpi['DATE'] == end_date]
    end_cpi_val = int(end_subdf['CPIAUCSL'].values)
    if end_cpi_val > start_cpi_val:
        return True
    else:
        return False


# want false for this one
def ue_math(start_date, end_date):
    start_subdf = ue.loc[ue['DATE'] == start_date]
    start_ue_val = int(start_subdf['UNRATE'].values)
    end_subdf = ue.loc[ue['DATE'] == end_date]
    end_ue_val = int(end_subdf['UNRATE'].values)
    if end_ue_val > start_ue_val:
        return True
    else:
        return False


def one_president(presidents_df, year):
    str_year = str(year)
    int_year = int(year)
    end_year = int_year + 4
    double_term = int_year + 8
    start_subdf = presidents_df.loc[presidents_df['Year first inaugurated'] == int_year]
    president_val = start_subdf.values.tolist()
    if president_val[0][1] > 4.0:
        final1 = []
        for item in president_val[0]:
            final1.append(item)
        final1.append(gdp_math(str_year + '-04-01', str(double_term) + '-01-01'))
        final1.append(cpi_math(str_year + '-04-01', str(double_term) + '-01-01'))
        final1.append(ue_math(str_year + '-04-01', str(double_term) + '-01-01'))
        return final1
    else:
        final = []
        for item in president_val[0]:
            final.append(item)
        final.append(gdp_math(str_year + '-04-01', str(end_year) + '-01-01'))
        final.append(cpi_math(str_year + '-04-01', str(end_year) + '-01-01'))
        final.append(ue_math(str_year + '-04-01', str(end_year) + '-01-01'))
        return final





def write_to_input_file(presidents, year):
    f = open("input1.txt", "a")
    temp1 = (one_president(presidents, str(year)))

    for item in temp1:
        f.write(str(item) + ", ")
    f.write("\n")
    f.close()


def big_input():
    write_to_input_file(presidents_df, '1977')
    write_to_input_file(presidents_df, '1981')
    write_to_input_file(presidents_df, '1989')
    write_to_input_file(presidents_df, '1993')
    write_to_input_file(presidents_df, '2001')
    write_to_input_file(presidents_df, '2009')
    f = open("input1.txt", "r")
    return f

def mapper():
    data = big_input().read()
    line=data.split('\n')
    myList = [line.split(', ')[0] for line in myList]
    print(myList)

    for x in line:
        print(x)
        for a in x:
            print(a)
    """
    for words in data:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        for word in words:
            print('%s%s%d' % (word, separator, 1))"""


mapper()
