article = "At a high-profile Libertarian conference, everyone agrees government should be smaller, but what should replace it is much more contested."
substitutions = {
    "high-profile":"Pit of Despair",
    "should":"totally",
    "what" : "who",
    "replace":"fly",
    "contested":"interesting"
}

for key, value in substitutions.items():
  article = article.replace(key, value)
print(article)

