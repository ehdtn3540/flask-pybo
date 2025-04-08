import markdown

def format_datetime(value, fmt='%Y년 %m월 %d일 %p %I:%M'):
    return value.strftime(fmt)

def markdown_filter(content):
	return markdown.markdown(content, extensions=["nl2br", "fenced_code"])
