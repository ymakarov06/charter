#vThis code imports and merges the school-level data from NCES Common Core of Data (CCD).
# The year range is 1999 through 2018. The files are avsilable here - https://nces.ed.gov/ccd/files.asp
# Note that the format varies from year to year. 
# I found it easier to use SAS files for 1999-2007 data and switched to text files in later years.
# Starting from 2015, we have multiple files by topic and their structure became a bit more complex.

# Config
import os
os.chdir('C:/Users/ymakarov/Desktop/python_folder/nces/')
import pandas as pd

# Keep a list of our variables of interest. 
# Unfortunately, labels changed from year to year, so this will have to be adjusted.
columns = ['NCESSCH', 'SCHNAM', 'LSTREE', 'LCITY', 'LSTATE', 'LZIP', 'LATCOD', 'LONCOD', # school ID and location
           'TYPE', 'STATUS', 'LOCALE', 'GSLO', 'GSHI', 'TITLEI', 'CHARTR', # school status
           'FTE', 'TOTFRL', 'MEMBER', 'ASIAN', 'HISP', 'BLACK', 'WHITE' # headcounts
          ]

# 1999
# Adjust columns
columns_temp1 = ['NCESSCH']
columns_temp2 = {}

for i in columns[1:]:
    i2 = i + '98'
    columns_temp1.append(i2)
    columns_temp2[i2] = i
    
columns_temp1.remove('LATCOD98')
columns_temp1.remove('LONCOD98')

# Import
schools1999_1 = pd.read_sas('data/1999/sc981ckn.sas7bdat', format = 'sas7bdat', encoding = 'latin-1')
schools1999_2 = pd.read_sas('data/1999/sc981cow.sas7bdat', format = 'sas7bdat', encoding = 'latin-1')
schools1999_3 = pd.read_sas('data/1999/sc981cai.sas7bdat', format = 'sas7bdat', encoding = 'latin-1')

# Combne
schools1999 = pd.concat([schools1999_1, schools1999_2, schools1999_3], axis = 0, ignore_index = True)

# Keep only relevant variables
schools1999 = schools1999[columns_temp1]

# Rename columns
schools1999.rename(columns = columns_temp2, inplace = True)


# 2000
# Adjust columns
columns_temp1 = ['NCESSCH']
columns_temp2 = {}

for i in columns[1:]:
    i2 = i + '99'
    columns_temp1.append(i2)
    columns_temp2[i2] = i
    
columns_temp1.remove('LATCOD99')
columns_temp1.remove('LONCOD99')

# Import
schools2000_1 = pd.read_sas('data/2000/sc991bai.sas7bdat', format = 'sas7bdat', encoding = 'latin-1')
schools2000_2 = pd.read_sas('data/2000/sc991bkn.sas7bdat', format = 'sas7bdat', encoding = 'latin-1')
schools2000_3 = pd.read_sas('data/2000/sc991bow.sas7bdat', format = 'sas7bdat', encoding = 'latin-1')

# Combine
schools2000 = pd.concat([schools2000_1, schools2000_2, schools2000_3], axis = 0, ignore_index = True)

# Keep only relevant variables
schools2000 = schools2000[columns_temp1]

# Rename columns
schools2000.rename(columns = columns_temp2, inplace = True)


# 2001
# Adjust columns
columns_temp1 = ['NCESSCH']
columns_temp2 = {}

for i in columns[1:]:
    i2 = i + '00'
    columns_temp1.append(i2)
    columns_temp2[i2] = i
    
# Import    
schools2001_1 = pd.read_sas('data/2001/sc001aai.sas7bdat', format = 'sas7bdat', encoding = 'latin-1')
schools2001_2 = pd.read_sas('data/2001/sc001akn.sas7bdat', format = 'sas7bdat', encoding = 'latin-1')
schools2001_3 = pd.read_sas('data/2001/sc001aow.sas7bdat', format = 'sas7bdat', encoding = 'latin-1')

# Combine
schools2001 = pd.concat([schools2001_1, schools2001_2, schools2001_3], axis = 0, ignore_index = True)

# Limit to relevant variables
schools2001 = schools2001[columns_temp1]

# Rename columns
schools2001.rename(columns = columns_temp2, inplace = True)


# 2002
# Adjust columns
columns_temp1 = ['NCESSCH']
columns_temp2 = {}

for i in columns[1:]:
    i2 = i + '01'
    columns_temp1.append(i2)
    columns_temp2[i2] = i
    
# Import    
schools2002_1 = pd.read_sas('data/2002/sc011aai.sas7bdat', format = 'sas7bdat', encoding = 'latin-1')
schools2002_2 = pd.read_sas('data/2002/sc011akn.sas7bdat', format = 'sas7bdat', encoding = 'latin-1')
schools2002_3 = pd.read_sas('data/2002/sc011aow.sas7bdat', format = 'sas7bdat', encoding = 'latin-1')

# Combine
schools2002 = pd.concat([schools2002_1, schools2002_2, schools2002_3], axis = 0, ignore_index = True)

# Limit to relevant variables
schools2002 = schools2002[columns_temp1]

# Rename columns
schools2002.rename(columns = columns_temp2, inplace = True)


# 2003
# Adjust columns
columns_temp1 = ['NCESSCH']
columns_temp2 = {}

for i in columns[1:]:
    i2 = i + '02'
    columns_temp1.append(i2)
    columns_temp2[i2] = i
    
# Import    
schools2003_1 = pd.read_sas('data/2003/sc021aai.sas7bdat', format = 'sas7bdat', encoding = 'latin-1')
schools2003_2 = pd.read_sas('data/2003/sc021akn.sas7bdat', format = 'sas7bdat', encoding = 'latin-1')
schools2003_3 = pd.read_sas('data/2003/sc021aow.sas7bdat', format = 'sas7bdat', encoding = 'latin-1')

# Combine
schools2003 = pd.concat([schools2003_1, schools2003_2, schools2003_3], axis = 0, ignore_index = True)

# Limit to relevant variables
schools2003 = schools2003[columns_temp1]

# Rename columns
schools2003.rename(columns = columns_temp2, inplace = True)

# 2004
# Adjust columns
columns_temp1 = ['NCESSCH']
columns_temp2 = {}

for i in columns[1:]:
    i2 = i + '03'
    columns_temp1.append(i2)
    columns_temp2[i2] = i
    
# Import
schools2004_1 = pd.read_sas('data/2004/sc031aai.sas7bdat', format = 'sas7bdat', encoding = 'latin-1')
schools2004_2 = pd.read_sas('data/2004/sc031akn.sas7bdat', format = 'sas7bdat', encoding = 'latin-1')
schools2004_3 = pd.read_sas('data/2004/sc031aow.sas7bdat', format = 'sas7bdat', encoding = 'latin-1')

# Combine
schools2004 = pd.concat([schools2004_1, schools2004_2, schools2004_3], axis = 0, ignore_index = True)

# Limit to relevant variables
schools2004 = schools2004[columns_temp1]

# Rename columns
schools2004.rename(columns = columns_temp2, inplace = True)


# 2005
# Adjust columns
columns_temp1 = ['NCESSCH']
columns_temp2 = {}

for i in columns[1:]:
    i2 = i + '04'
    columns_temp1.append(i2)
    columns_temp2[i2] = i
    
# Import    
schools2005_1 = pd.read_sas('data/2005/sc041bai.sas7bdat', format = 'sas7bdat', encoding = 'latin-1')
schools2005_2 = pd.read_sas('data/2005/sc041bkn.sas7bdat', format = 'sas7bdat', encoding = 'latin-1')
schools2005_3 = pd.read_sas('data/2005/sc041bow.sas7bdat', format = 'sas7bdat', encoding = 'latin-1')

# Combine
schools2005 = pd.concat([schools2005_1, schools2005_2, schools2005_3], axis = 0, ignore_index = True)

# Limit to relevant variables
schools2005 = schools2005[columns_temp1]

# Rename columns
schools2005.rename(columns = columns_temp2, inplace = True)


# 2006
# Adjust columns
columns_temp1 = ['NCESSCH']
columns_temp2 = {}

for i in columns[1:]:
    i2 = i + '05'
    columns_temp1.append(i2)
    columns_temp2[i2] = i
    
# Import    
schools2006_1 = pd.read_sas('data/2006/sc051aai.sas7bdat', format = 'sas7bdat', encoding = 'latin-1')
schools2006_2 = pd.read_sas('data/2006/sc051akn.sas7bdat', format = 'sas7bdat', encoding = 'latin-1')
schools2006_3 = pd.read_sas('data/2006/sc051aow.sas7bdat', format = 'sas7bdat', encoding = 'latin-1')

# Combine
schools2006 = pd.concat([schools2006_1, schools2006_2, schools2006_3], axis = 0, ignore_index = True)

# Limit to relevant variables
schools2006 = schools2006[columns_temp1]

# Rename columns
schools2006.rename(columns = columns_temp2, inplace = True)


# 2007
# Adjust columns
columns_temp1 = ['NCESSCH']
columns_temp2 = {}

for i in columns[1:]:
    i2 = i + '06'
    columns_temp1.append(i2)
    columns_temp2[i2] = i
    
# Import    
schools2007_1 = pd.read_sas('data/2007/sc061cai.sas7bdat', format = 'sas7bdat', encoding = 'latin-1')
schools2007_2 = pd.read_sas('data/2007/sc061ckn.sas7bdat', format = 'sas7bdat', encoding = 'latin-1')
schools2007_3 = pd.read_sas('data/2007/sc061cow.sas7bdat', format = 'sas7bdat', encoding = 'latin-1')

# Combine
schools2007 = pd.concat([schools2007_1, schools2007_2, schools2007_3], axis = 0, ignore_index = True)
schools2007.rename(columns = {'ULOCAL06': 'LOCALE06'}, inplace = True)

# Limit to relevant variables
schools2007 = schools2007[columns_temp1]

# Rename variables
schools2007.rename(columns = columns_temp2, inplace = True)


# 2008
# Adjust columns
columns_temp1 = ['NCESSCH']
columns_temp2 = {}

for i in columns[1:]:
    i2 = i + '07'
    columns_temp1.append(i2)
    columns_temp2[i2] = i
    
# Import    
schools2008 = pd.read_csv('data/2008/sc071b.txt', sep = "\t", engine = 'python')
schools2008.rename(columns = {'ULOCAL07': 'LOCALE07'}, inplace = True)

# Limit to relevant variables
schools2008 = schools2008[columns_temp1]

# Rename columns
schools2008.rename(columns = columns_temp2, inplace = True)


# 2009
# Adjust columns
columns_temp1 = ['NCESSCH']
columns_temp2 = {}

for i in columns[1:]:
    i2 = i + '08'
    columns_temp1.append(i2)
    columns_temp2[i2] = i
    
# Import    
schools2009 = pd.read_csv('data/2009/sc081b.txt', sep = "\t", engine = 'python')
schools2009.rename(columns = {'ULOCAL08': 'LOCALE08'}, inplace = True)

# Limit to relevant variables
schools2009 = schools2009[columns_temp1]

# Rename columns
schools2009.rename(columns = columns_temp2, inplace = True)


# 2010
# Adjust columns
columns_temp1 = ['NCESSCH']
columns_temp2 = {}

for i in columns[1:]:
    i2 = i + '09'
    columns_temp1.append(i2)
    columns_temp2[i2] = i
    
# Import    
schools2010 = pd.read_csv('data/2010/sc092a.txt', sep = "\t", engine = 'python')
schools2010.rename(columns = {'ULOCAL09': 'LOCALE09'}, inplace = True)

# Limit to relevant variables
schools2010 = schools2010[columns_temp1]

# Rename columns
schools2010.rename(columns = columns_temp2, inplace = True)


# 2011
# Import
schools2011 = pd.read_csv('data/2011/sc102a.txt', sep = "\t", engine = 'python')
schools2011.rename(columns = {'ULOCAL': 'LOCALE'}, inplace = True)

# Limit to relevant variables
schools2011 = schools2011[columns]


# 2012
# Import
schools2012 = pd.read_csv('data/2012/sc111a_supp.txt', sep = "\t", engine = 'python')
schools2012.rename(columns = {'ULOCAL': 'LOCALE'}, inplace = True)

# Limit to relevant variables
schools2012 = schools2012[columns]


# 2013
# Import
schools2013 = pd.read_csv('data/2013/sc122a.txt', sep = "\t", engine = 'python')
schools2013.rename(columns = {'ULOCAL': 'LOCALE'}, inplace = True)

# Limit to relevant variables
schools2013 = schools2013[columns]


# 2014
# Import
schools2014 = pd.read_csv('data/2014/sc132a.txt', sep = "\t", engine = 'python')
schools2014.rename(columns = {'ULOCAL': 'LOCALE'}, inplace = True)

# Limit to relevant variables
schools2014 = schools2014[columns]


# The following years have thematic files. Keep the lists of relevant variables.
cols_dir = ['NCESSCH', 'SCH_NAME', 'LSTREET1', 'LCITY', 'LSTATE',
            'LZIP', 'SCH_TYPE', 'SY_STATUS', 'CHARTER_TEXT', 'GSLO', 'GSHI']
cols_memb = ['NCESSCH', 'MEMBER', 'AS', 'HP', 'HI', 'BL', 'WH']
cols_staff = ['NCESSCH', 'FTE']
cols_char = ['NCESSCH', 'TITLEI']
cols_frl = ['NCESSCH', 'TOTFRL']
rename = {'SCH_NAME': 'SCHNAM', 'LSTREET1': 'LSTREE', 'SCH_TYPE': 'TYPE', 'SY_STATUS': 'STATUS',
          'CHARTER_TEXT': 'CHARTR', 'HI': 'HISP', 'BL': 'BLACK', 'WH': 'WHITE'}


# 2015
# Import

# directory
directory2015 = pd.read_csv('data/2015/ccd_sch_029_1415_w_0216601a.txt', sep = "\t", engine = 'python')
directory2015 = directory2015[cols_dir]
    
# membership
membership2015 = pd.read_csv('data/2015/ccd_sch_052_1415_w_0216161a.txt', sep = "\t", engine = 'python')
membership2015 = membership2015[cols_memb]

# staff
staff2015 = pd.read_csv('data/2015/ccd_sch_059_1415_w_0216161a.txt', sep = "\t", engine = 'python')
staff2015 = staff2015[cols_staff]

# school characteristics
chars2015 = pd.read_csv('data/2015/ccd_sch_129_1415_w_0216161a.txt', sep = "\t", engine = 'python')
chars2015 = chars2015[cols_char]

# FRL
frl2015 = pd.read_csv('data/2015/ccd_sch_033_1415_w_0216161a.txt', sep = "\t", engine = 'python')
frl2015 = frl2015[cols_frl]
    
# Merge
schools2015 = directory2015.merge(membership2015, on = 'NCESSCH', how = 'outer')
schools2015 = schools2015.merge(staff2015, on = 'NCESSCH', how = 'outer')
schools2015 = schools2015.merge(chars2015, on = 'NCESSCH', how = 'outer')
schools2015 = schools2015.merge(frl2015, on = 'NCESSCH', how = 'outer')

# Rename columns
schools2015.rename(columns = rename, inplace = True)
schools2015['ASIAN'] = schools2015['AS'] + schools2015['HP']
schools2015.drop(['AS', 'HP'], axis = 1, inplace = True)


# 2016
# Import

# directory
directory2016 = pd.read_csv('data/2016/ccd_sch_029_1516_w_2a_011717.csv', sep = ",", engine = 'python')
directory2016 = directory2016[cols_dir]

# membership
membership2016 = pd.read_csv('data/2016/ccd_sch_052_1516_w_2a_011717.csv', sep = ",", engine = 'python')
membership2016 = membership2016[cols_memb]

# staff
staff2016 = pd.read_csv('data/2016/ccd_sch_059_1516_w_2a_011717.csv', sep = ",", engine = 'python')
staff2016 = staff2016[cols_staff]

# school characteristics
chars2016 = pd.read_csv('data/2016/ccd_sch_129_1516_w_2a_011717.csv', sep = ",", engine = 'python')
chars2016 = chars2016[cols_char]

# FRL
frl2016 = pd.read_csv('data/2016/ccd_sch_033_1516_w_2a_011717.csv', sep = ",", engine = 'python')
frl2016 = frl2016[cols_frl]

# merge
schools2016 = directory2016.merge(membership2016, on = 'NCESSCH', how = 'outer')
schools2016 = schools2016.merge(staff2016, on = 'NCESSCH', how = 'outer')
schools2016 = schools2016.merge(chars2016, on = 'NCESSCH', how = 'outer')
schools2016 = schools2016.merge(frl2016, on = 'NCESSCH', how = 'outer')

# Rename columns
schools2016.rename(columns = rename, inplace = True)
schools2016['ASIAN'] = schools2016['AS'] + schools2016['HP']
schools2016.drop(['AS', 'HP'], axis = 1, inplace = True)


# 2017
# Import

# directory
directory2017 = pd.read_csv('data/2017/ccd_sch_029_1617_w_1a_11212017.csv', sep = ',', engine = 'python')
directory2017 = directory2017[cols_dir]

# membership
# The file is large, so I import it in chunks and subset along the way.
memb_iter = pd.read_csv('data/2017/ccd_sch_052_1617_l_2a_11212017.csv', sep = ",", engine = 'python',
                       iterator = True, chunksize = 10000)
membership2017 = pd.concat([chunk[(chunk['TOTAL_INDICATOR'] == 'Derived - Subtotal by Race/Ethnicity and Sex minus Adult Education Count') | 
            (chunk['TOTAL_INDICATOR'] == 'Education Unit Total')] for chunk in memb_iter])
    
# Not interested in segmentation by gender
membership2017 = membership2017[['NCESSCH', 'RACE_ETHNICITY', 'STUDENT_COUNT', 'TOTAL_INDICATOR']]
membership2017 = membership2017.groupby(['NCESSCH', 'RACE_ETHNICITY']).agg('sum').reset_index()
    
# Keep records for relevant groups
membership2017 = membership2017[(membership2017['RACE_ETHNICITY'] == 'White') |
                               (membership2017['RACE_ETHNICITY'] == 'No Category Codes') |
                               (membership2017['RACE_ETHNICITY'] == 'Hispanic/Latino') |
                               (membership2017['RACE_ETHNICITY'] == 'Asian') |
                               (membership2017['RACE_ETHNICITY'] == 'Native Hawaiian or Other Pacific Islander') |
                               (membership2017['RACE_ETHNICITY'] == 'Black or African American')]

# Clean up
membership2017['RACE_ETHNICITY'] = membership2017['RACE_ETHNICITY'].map({'White': 'WH', 'No Category Codes': 'MEMBER',
                                'Hispanic/Latino': 'HI', 'Asian': 'AS', 'Native Hawaiian or Other Pacific Islander': 'HP',
                                'Black or African American': 'BL'})

# Reshape wide
membership2017 = membership2017.pivot(index = 'NCESSCH', columns = 'RACE_ETHNICITY', values = 'STUDENT_COUNT').reset_index()

    
# staff
staff2017 = pd.read_csv('data/2017/ccd_sch_059_1617_l_2a_11212017.csv', sep = ",", engine = 'python')
staff2017.rename(columns = {'TEACHERS': 'FTE'}, inplace = True)
staff2017 = staff2017[cols_staff]

# school characteristics
chars2017 = pd.read_csv('data/2017/ccd_sch_129_1617_w_1a_11212017.csv', sep = ",", engine = 'python')
chars2017.rename(columns = {'TITLEI_STATUS': 'TITLEI'}, inplace = True)
chars2017 = chars2017[['NCESSCH', 'TITLEI']]
   
# FRL
frl2017 = pd.read_csv('data/2017/ccd_sch_033_1617_l_2a_11212017.csv', sep = ",", engine = 'python')
frl2017 = frl2017[(frl2017['LUNCH_PROGRAM'] == "Reduced-price lunch qualified") |
        (frl2017['LUNCH_PROGRAM'] == "Free lunch qualified")]
frl2017 = frl2017.groupby('NCESSCH').agg('sum').reset_index()
frl2017.rename(columns = {'STUDENT_COUNT': 'TOTFRL'}, inplace = True)
frl2017 = frl2017[cols_frl]
    
# merge
schools2017 = directory2017.merge(membership2017, on = 'NCESSCH', how = 'outer')
schools2017 = schools2017.merge(staff2017, on = 'NCESSCH', how = 'outer')
schools2017 = schools2017.merge(chars2017, on = 'NCESSCH', how = 'outer')
schools2017 = schools2017.merge(frl2017, on = 'NCESSCH', how = 'outer')

# Rename columns
schools2017.rename(columns = rename, inplace = True)
schools2017['ASIAN'] = schools2017['AS'] + schools2017['HP']
schools2017.drop(['AS', 'HP'], axis = 1, inplace = True)


# 2018
# Import

# directory
directory2018 = pd.read_csv('data/2018/ccd_sch_029_1718_w_1a_083118.csv', sep = ',', engine = 'python')
directory2018 = directory2018[cols_dir]

# membership
memb_iter = pd.read_csv('data/2018/ccd_SCH_052_1718_l_1a_083118.csv', sep = ",", engine = 'python',
                       iterator = True, chunksize = 10000)
membership2018 = pd.concat([chunk[(chunk['TOTAL_INDICATOR'] == 'Derived - Subtotal by Race/Ethnicity and Sex minus Adult Education Count') | 
            (chunk['TOTAL_INDICATOR'] == 'Education Unit Total')] for chunk in memb_iter])
    
# Not interested in segmentation by gender
membership2018 = membership2018[['NCESSCH', 'RACE_ETHNICITY', 'STUDENT_COUNT', 'TOTAL_INDICATOR']]
membership2018 = membership2018.groupby(['NCESSCH', 'RACE_ETHNICITY']).agg('sum').reset_index()
    
# Keep relevant student groups
membership2018 = membership2018[(membership2018['RACE_ETHNICITY'] == 'White') |
                               (membership2018['RACE_ETHNICITY'] == 'No Category Codes') |
                               (membership2018['RACE_ETHNICITY'] == 'Hispanic/Latino') |
                               (membership2018['RACE_ETHNICITY'] == 'Asian') |
                               (membership2018['RACE_ETHNICITY'] == 'Native Hawaiian or Other Pacific Islander') |
                               (membership2018['RACE_ETHNICITY'] == 'Black or African American')]

# Clean up
membership2018['RACE_ETHNICITY'] = membership2018['RACE_ETHNICITY'].map({'White': 'WH', 'No Category Codes': 'MEMBER',
                                'Hispanic/Latino': 'HI', 'Asian': 'AS', 'Native Hawaiian or Other Pacific Islander': 'HP',
                                'Black or African American': 'BL'})

# Reshape wide
membership2018 = membership2018.pivot(index = 'NCESSCH', columns = 'RACE_ETHNICITY', values = 'STUDENT_COUNT').reset_index()

# staff
staff2018 = pd.read_csv('data/2018/ccd_sch_059_1718_l_1a_083118.csv', sep = ",", engine = 'python')
staff2018.rename(columns = {'TEACHERS': 'FTE'}, inplace = True)
staff2018 = staff2018[cols_staff]

# school characteristics
chars2018 = pd.read_csv('data/2018/ccd_sch_129_1718_w_1a_083118.csv', sep = ",", engine = 'python')
chars2018.rename(columns = {'TITLEI_STATUS': 'TITLEI'}, inplace = True)
chars2018 = chars2018[['NCESSCH', 'TITLEI']]

# FRL
frl2018 = pd.read_csv('data/2018/ccd_sch_033_1718_l_1a_083118.csv', sep = ",", engine = 'python')
frl2018 = frl2018[(frl2018['LUNCH_PROGRAM'] == "Reduced-price lunch qualified") |
(frl2018['LUNCH_PROGRAM'] == "Free lunch qualified")]
frl2018 = frl2018.groupby('NCESSCH').agg('sum').reset_index()
frl2018.rename(columns = {'STUDENT_COUNT': 'TOTFRL'}, inplace = True)
frl2018 = frl2018[cols_frl]
    
# merge
schools2018 = directory2018.merge(membership2018, on = 'NCESSCH', how = 'outer')
schools2018 = schools2018.merge(staff2018, on = 'NCESSCH', how = 'outer')
schools2018 = schools2018.merge(chars2018, on = 'NCESSCH', how = 'outer')
schools2018 = schools2018.merge(frl2018, on = 'NCESSCH', how = 'outer')

# Rename columns
schools2018.rename(columns = rename, inplace = True)
schools2018['ASIAN'] = schools2018['AS'] + schools2018['HP']
schools2018.drop(['AS', 'HP'], axis = 1, inplace = True)


# Merge all years
schools1999['Year'] = 1999
schools2000['Year'] = 2000
schools2001['Year'] = 2001
schools2002['Year'] = 2002
schools2003['Year'] = 2003
schools2004['Year'] = 2004
schools2005['Year'] = 2005
schools2006['Year'] = 2006
schools2007['Year'] = 2007
schools2008['Year'] = 2008
schools2009['Year'] = 2009
schools2010['Year'] = 2010
schools2011['Year'] = 2011
schools2012['Year'] = 2012
schools2013['Year'] = 2013
schools2014['Year'] = 2014
schools2015['Year'] = 2015
schools2016['Year'] = 2016
schools2017['Year'] = 2017
schools2018['Year'] = 2018


schools_all = pd.concat([schools1999, schools2000, schools2001, schools2002, schools2003,
                        schools2004, schools2005, schools2006, schools2007, schools2008,
                        schools2009, schools2010, schools2011, schools2012, schools2013,
                        schools2014, schools2015, schools2016, schools2017, schools2018],
                         axis = 0, ignore_index = True)


# Some quality checks
schools_all.info()
schools_all.groupby(['NCESSCH', 'Year']).ngroups == schools_all.shape[0] # unique at school-year level

# Export
schools_all.to_csv("data/all_schools.csv")

###END###