# Parsing-xml-file-using-python..
# Overview of Parser:
Parsing an XML file involves analyzing the structure and content of an XML document and turning 
it into a more easily understandable format, such as a tree or a list of objects. This process is useful 
for extracting specific data from an XML file, as well as for manipulating and modifying the 
contents of the file. There are several tools and libraries available for parsing XML files, including 
DOM (Document Object Model) parsers, SAX (Simple API for XML) parsers, and XML Pull 
parsers. Each of these approaches has its own strengths and weaknesses, and the best choice will 
depend on the specific requirements of the task at hand. Regardless of the approach taken, proper 
handling of errors and edge cases is important to ensure that the XML file is parsed accurately and 
efficiently.
# In this assignment you are required to parse an xml file (provided in attachment) file using 
python or any language of your preference.
# The data to be extracted from file includes:
1. Book_Id
2. Author_Name 
3. Title
4. Genre 
5. Price
6. Publish_date
7. Description

# Working;

The name selected for the xml file is compiler.xml. There are different methods available for extraction but the method used here is by loop in which the text of the provided tags is printed and stored, the loop will continue to run for the number of tags . All the data will be stored at the end and each book provides details.
XML is an inherently hierarchical data format, and the most natural way to represent it is with a tree. ET has two classes for this purpose - ElementTree represents the whole XML document as a tree, and Element represents a single node in this tree. Interactions with the whole document (reading and writing to/from files) are usually done on the ElementTree level. Interactions with a single XML element and its sub-elements are done on the Element level.
