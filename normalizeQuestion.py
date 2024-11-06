import re

def preprocess_query(query):
    # make all characters become lowercase
    query = query.lower()
    
    # eliminate every suffix expression
    query = re.sub(r"(là gì\?)|(như thế nào\?)", "", query)
    
    #eliminate punctuations
    query = re.sub(r"[^\w\s]", "", query) 
    
    #eliminate spaces
    query = query.strip()
    
    return query

# s = input("Enter query: ")
# s = preprocess_query(s)
# print(s)