import docx


# For Word documents, there are three types of styles: 
# * Paragraph styles can be applied to Paragraph objects, 
# * character styles can be applied to Run objects, 
# * & linked styles can be applied to both kinds of objects. 
# 
# You can give both Paragraph and Run objects styles by setting their style attribute to a string. 
# This string should be the name of a style. 
# If style is set to None, then there will be no style associated with the Paragraph or Run object.


# The string values for the default Word styles:
styles = {
    1: ['Normal', 'BodyText', 'MacroText', 'BodyText2', 'BodyText3'], 
    2: ['TOCHeading', 'Heading1', 'Heading2', 'Heading3', 'Heading4'],
    3: ['Heading5', 'Heading6', 'Heading7', 'Heading8', 'Heading9'],
    4: ['ListBullet', 'ListBullet2', 'ListBullet3'],
    5: ['ListContinue', 'ListContinue2', 'ListContinue3'],
    6: ['List', 'List2', 'List3', 'ListParagraph', 'ListNumber', 'ListNumber2','ListNumber3'],
    7: ['NoSpacing', 'Title'],
    8: ['Quote', 'Caption', 'Subtitle', 'IntenseQuote']
}

# def style_docx(filename):
#     doc = docx.Document(filename)






 








