import html
a_string = "<ethical>"
encoded_string = html.escape(a_string)
print(encoded_string)



import html
a_string = " &lt;ethical&gt;"
decoded_string = html.unescape(a_string)
print(decoded_string)
