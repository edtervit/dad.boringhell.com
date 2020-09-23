import push_live



base_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>Ned's Race Reminder</title>
</head>
<body>
    <h1>Ned's Race Reminder</h1>
</body>
</html> '''

final_html = base_html

wr = open('index.html', 'w')
wr.write(final_html)

##Enbale to push final html file to live server
#push_live.upload_index()