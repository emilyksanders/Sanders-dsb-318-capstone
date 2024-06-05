# Written Tuesday, June 4, 2024
# FOR Wednesday, June 5, 2024

# Much of this was copied from impt_misc

# The simple imputer stuff

s_median = ["w1q50", "w1q48", "w1q51", "w1q112", 
  "w1q49", "w1q47", "w1q46", "w1q45", "w1q146c", 
  "w1q162", "w1q181", "w1q146f", "w1q146g", "w1q146e"]
  
s_mode = ["w1q175", "w1q72", "w1q142d", "w1q65", "w1q52", 
  "w1q142i", "w1q142g", "w1q180", "w1q69", "w1q135d", 
  "w1q142h", "w1q135b", "w1q135c", "w1q135e", "w1q142b", 
  "w1q142e", "w1q142f", "w1q142j", "w1q142a", "w1q142k", 
  "w1q19c", "w1q19d", "w1q19b", "w1q19a", "w1q75", 
  "w1q78", "w1q79", "w1q76"]

s_median_new = [''.join([x, '_ei']) for x in s_median]
s_mode_new = [''.join([x, '_ei']) for x in s_mode]





# Right here I need to figure out how to deal with the 97s-99s.





# Safety first
# meyer.to_csv('meyer_much_imputation_done_but_not_si_yet.csv', index = False)

# I think the cleanest way to do this without it breaking everything is to
# break the dataframe apart, use the 2 SIs separately, then re-merge.
# Let me check that the studyID will be suitable for merging on.

meyer.shape # 1507 rows (250 columns)
meyer['studyid'].nunique() # 1507 unique values

# split the df up for imputing
meyer_median = meyer[s_median+['studyid']]
meyer_mode = meyer[s_mode+['studyid']]

# new column names
s_median_new.append('studyid')
s_mode_new.append('studyid')
meyer_median.columns = s_median_new
meyer_mode.columns = s_mode_new

# do the imputation!
meyer_median = pd.DataFrame(
  si_med.fit_transform(meyer_median), columns = si_med.get_feature_names_out())

meyer_mode = pd.DataFrame(
  si_mode.fit_transform(meyer_mode), columns = si_mode.get_feature_names_out())

# is it really that easy?
meyer_median.isna().sum().sum()
meyer_mode.isna().sum().sum()

mme = meyer_median.describe()
mmo = meyer_mode.describe()

# No!  No, it is not!!
# The stupid 97s, 98s, and 99s are at it again!
