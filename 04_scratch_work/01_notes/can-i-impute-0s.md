I want to impute my NAs with 0s so that I can do math across my columns. What I did here was run this code

`for i in list(meyer.columns):` \n `a = list(meyer[i].unique())` \n `if 0 in a:` \n `print(i)`

to print out the name of every column that has 0s in it, pre-MY-imputation. (Note that all of the AUTHOR's imputations are already present in the dataset.) I then looked up each variable in the 831 page documentation to see how many missing values it has (because if it has none, then imputation is a moot point), and what the naturally-occurring 0s mean. For some columns, it would be fine to impute missing values with 0s, even if there are already extent 0s. For others though, if a value of 0 is meaningful, it could introduce a ton of error into the model to impute 0s all over the place.

|     | column          | how many NAs does it have?        | Is it ok to impute as 0s?                                                                                     |
|--------------|--------------|----------------------|----------------------|
| 1   | gurban_i        | 0                                 | na                                                                                                            |
| 2   | gmilesaway2     | 18                                | no, but it would be if I reverse coded what's there                                                           |
| 3   | w1q01           | 14, plus 2 "don't know"           | it'd be better not to, but it wouldn't break everything. it'd be better to impute these like the rest, though |
| 4   | w1q02           | 12, plus 48 "don't know"          | same as w1q02                                                                                                 |
| 5   | w1q72           | 31                                | no. 0 poor mental health days is meaningful. better to impute.                                                |
| 6   | w1q111          | 1007, plus 1 implausible actual 0 | no, it's an age Q                                                                                             |
| 7   | w1q146a         | 16                                | no, impute; mode=1                                                                                            |
| 8   | w1q146b         | 15                                | no, impute                                                                                                    |
| 9   | w1q146c         | 19                                | no, impute                                                                                                    |
| 10  | w1q146d         | 24                                | technically no, but mode=0. see if you can logically impute from other Qs                                     |
| 11  | w1q146e         | 17                                | tech no, but mode=0                                                                                           |
| 12  | w1q146f         | 18                                | tech no, but mode=0                                                                                           |
| 13  | w1q146g         | 18                                | tech no, but mode=0                                                                                           |
| 14  | w1q146h         | 15                                | tech no, but mode=0                                                                                           |
| 15  | w1q146i         | 16                                | tech no, but mode=0                                                                                           |
| 16  | w1q146j         | 16                                | tech no, but mode=0                                                                                           |
| 17  | w1q146k         | 16                                | tech no, but mode=0                                                                                           |
| 18  | w1q146l         | 17                                | tech no, but mode=0                                                                                           |
| 19  | w1poverty_i     | 27                                | not sure, see documentation                                                                                   |
| 20  | w1conversion    | no                                | na                                                                                                            |
| 21  | w1conversionhc  | no                                | na                                                                                                            |
| 22  | w1conversionrel | no                                | na                                                                                                            |
| 23  | w1ace_i         | no                                | already imputed a lot                                                                                         |
| 24  | w1ace_emo_i     | no                                | already imputed a lot                                                                                         |
| 25  | w1ace_inc_i     | no                                | already imputed a lot                                                                                         |
| 26  | w1ace_ipv_i     | no                                | already imputed a lot                                                                                         |
| 27  | w1ace_men_i     | no                                | already imputed a lot                                                                                         |
| 28  | w1ace_phy_i     | no                                | already imputed a lot                                                                                         |
| 29  | w1ace_sep_i     | no                                | already imputed a lot                                                                                         |
| 30  | w1ace_sex_i     | no                                | already imputed a lot                                                                                         |
| 31  | w1ace_sub_i     | no                                | already imputed a lot                                                                                         |
| 32  | w1auditc_i      | no                                | na                                                                                                            |
| 33  | w1dudit_i       | no                                | already imputed a lot                                                                                         |
| 34  | w1kessler6_i    | no                                | na                                                                                                            |
