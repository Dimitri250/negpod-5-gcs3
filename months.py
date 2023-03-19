long_months = ['january', 'march', 'may', 'july', 'august', 'october', 'december']
short_months = ['april', 'june', 'september', 'november']

month = input("Enter a month: ").lower()

if month == "february":
    print(f'{month} has 28 or 29 days.')
elif month in long_months:
    print(f'{month} has 31 days.')
elif month in short_months:
    print(f'{month} has 30 days.')
else:
    print(f'{month} is not a valid month. These are the months I know: {", ".join(long_months)}, { ", ".join(short_months) } and february.' )

