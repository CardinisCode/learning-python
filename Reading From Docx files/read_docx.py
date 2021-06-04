import docx


# This will read a docx file, 1 paragraph at a time & add it to a list. 
def getText(filename):
    doc = docx.Document(filename)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n\n'.join(full_text)


# Now to print the contents of our docx file:
print(getText('restyled.docx'))


# Some possible modifications to the above function:

# 1)    To indent each paragraph:
#       full_text.append(' ' + para.text)

# 2)    To add a double space in between paragraphs:
#       Update the join call:
#           return '\n\n'.join(full_text)


