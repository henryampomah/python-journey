from countries import countries

land = [country for country in countries if 'land' in country]
print(land)
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[::-1]  
print(fruits[::-1])

from countries_data import countries

all_languages = set()
for country in countries:
    for language in country['languages']:
        all_languages.add(language)

print(f"Total number of unique languages: {len(all_languages)}")


language_counts = {}
for country in countries:
    for language in country['languages']:
        if language in language_counts:
            language_counts[language] += 1
        else:
            language_counts[language] = 1

top_10 = sorted(language_counts.items(), key=lambda x: x[1], reverse=True)[:10]

print("Top 10 most spoken languages:")
for i, (language, count) in enumerate(top_10, 1):
    print(f"{i}. {language}: {count} countries")