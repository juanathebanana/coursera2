import pandas as pd
import pickle
data = pd.read_csv("/home/juana/Downloads/appendix.csv")


df_new = data.drop_duplicates(subset=['Course Number', 'Course Title'], keep=False)
df_new['Weight Avg'] = ((df_new['Participants (Course Content Accessed)'] / df_new['Participants (Course Content Accessed)'].sum())*0.60) + (df_new['% Posted in Forum']*0.30)+(df_new['% Certified']*0.10)

subject_list = list(df_new['Course Subject'].unique())
subject_dict = {'a': subject_list[0], 'b': subject_list[1], 'c': subject_list[2], 'd': subject_list[3]}
"""
print('Course categories: \n')
print('a) ', subject_dict['a'])
print('b) ', subject_dict['b'])
print('c) ', subject_dict['c'])
print('d) ', subject_dict['d'])

print('Course categories: \n')
print('a) ', subject_dict['a'])
print('b) ', subject_dict['b'])
print('c) ', subject_dict['c'])
print('d) ', subject_dict['d'])
"""


def recommend(course_subject):
    filter_subject = df_new['Course Subject'] == course_subject

    print('\n Top 5 Rated Courses in %a \n' % course_subject)
    df_rated = df_new[filter_subject].sort_values(by=['Weight Avg'], ascending=False).head()
    print(df_rated[['Course Number', 'Course Title']])

    print('\nTop 5 Popular Courses in %a \n' % course_subject)
    df_popular = df_new[filter_subject].sort_values(by=['Participants (Course Content Accessed)'],
                                                    ascending=False).head()
    print(df_popular[['Course Number', 'Course Title']])


primo=recommend(subject_dict['a'])


pickle.dump(df_new.to_dict(),open('subject_dict.pkl','wb')) #contains the dataframe in dict
pickle.dump(primo,open('df_new.pkl','wb'))

pickle.dump(recommend,open('modello.pkl','wb'))