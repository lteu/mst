# import plotly.express as px
# import pandas as pd

# schools = ["Brown", "NYU", "Notre Dame", "Cornell", "Tufts", "Yale",
#            "Dartmouth", "Chicago", "Columbia", "Duke", "Georgetown",
#            "Princeton", "U.Penn", "Stanford", "MIT", "Harvard"]
# n_schools = len(schools)

# men_salary = [72, 67, 73, 80, 76, 79, 84, 78, 86, 93, 94, 90, 92, 96, 94, 112]
# women_salary = [92, 94, 100, 107, 112, 114, 114, 118, 119, 124, 131, 137, 141, 151, 152, 165]

# df = pd.DataFrame(dict(school=schools*2, salary=men_salary + women_salary,
#                        gender=["Men"]*n_schools + ["Women"]*n_schools))

# # Use column names of df for the different parameters x, y, color, ...
# fig = px.scatter(df, x="salary", y="school", color="gender",
#                  title="Gender Earnings Disparity",
#                  labels={"salary":"Annual Salary (in thousands)"} # customize axis label
#                 )

# fig.show()


import plotly.express as px
df = px.data.gapminder()

print(df)
# fig = px.scatter(df, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
#            size="pop", color="continent", hover_name="country",
#            log_x=True, size_max=55, range_x=[100,100000], range_y=[25,90])

fig = px.scatter(df, x="gdpPercap", y="pop", animation_frame="year", animation_group="country",
           size="lifeExp", color="continent", hover_name="country",
           log_x=True, size_max=55, range_x=[100,100000], range_y=[1282697,13311143])

fig.show()