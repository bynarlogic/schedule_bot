from re import search, sub, split

def format_dates(statement):
    pattern = r'(\d{2}|\d{1})(-|\/)(\d{2}|\d{1})(-|\/)\d{4}'

    bad_date_format = search(pattern, statement.text)
    if bad_date_format:
        date = bad_date_format.group()
        m, d, y = split(r"\/|-", date)
        date = "-".join([y,m,d])
        statement.text =  sub(pattern, date, bad_date_format.string)

    return statement

def capitalize_months(statement):
    jan_apr = r'\b(jan|january)\b|\b(feb|february)\b|\b(mar|march)\b|\b(apr|april)\b'
    may_aug = r'\b(may)\b|\b(jun|june)\b|\b(jul|july)\b|\b(aug|august)\b'
    sept_dec = r'\b(sept|september)\b|\b(oct|october)\b|\b(nov|november)\b|\b(dec|december)\b'
    pattern = jan_apr+may_aug+sept_dec

    month = search(pattern, statement.text)

    if month:
        capitalized_month = month.group().capitalize()
        statement.text = sub(pattern, capitalized_month, month.string)

    return statement