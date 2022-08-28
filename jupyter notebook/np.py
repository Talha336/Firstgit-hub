import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style= "whitegrid" , color_codes= True)
boat = sns.load_dataset("titanic")
sns.boxplot(x= "class" , y = "fare" ,  data = boat , linewidth = 2.5 )



