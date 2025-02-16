import mysql.connector
import re

from flask import jsonify
from sqlalchemy.orm import query_expression



def Query_Formation(query):
    search=query
    sql1='''with cte as (select Website,(select  row_id from dfid d where ( product_name like '''
    sql2=''' ) and d.website = w.website limit 1) id from websitename w) select d.product_name,d.product_link,d.image_link,d.Product_price,d.Product_ratings,d.Website,d.Category from dfid d inner join cte c on d.row_id=c.id;'''
    conditions = '"'

    for i in search.split()[0:3]:
        conditions+=f'%{i}'

    conditions+='%"'
    return sql1+conditions+sql2

def search_item(query):
    mydb = mysql.connector.connect(
        host="localhost",
        username="root",
        password="",
        database="projectsearchengine"
    )
    mycursor = mydb.cursor()
    sql=Query_Formation(query)
    mycursor.execute(sql)
    result=mycursor.fetchall()
    mycursor.close()
    return result

# recommend Product
def recommend_info(row_index):
    mydb = mysql.connector.connect(
        host="localhost",
        username="root",
        password="",
        database="projectsearchengine"
    )
    mycursor = mydb.cursor()
    product_info=[]
    for i in row_index:
        sql=f'''select d.product_name,d.product_link,d.image_link,d.Product_price,d.Product_ratings,d.Website,d.Category from dfid d where row_id={i};'''
        mycursor.execute(sql)
        result=mycursor.fetchall()
        product_info.extend(result)
    mycursor.close()

    return product_info


if(__name__)=="__main__":
    pass
    # use for Debugging 2
    # result1=recommend_info([3630, 5, 14, 63, 743, 3622, 3660, 795, 3625])
    # print(result1)
    # #
    # print("Then Above one is list and below one is items of list")
    #
    # print('\n')
    # for i in result1:
    #     print(i)
    #
    # print("length of each item",len(result1[0]))
    # result=jsonify(result)
    # print("After Jsonify")
    # print(result)
    # print(type(result))
#
#




# search=input("Search..")
# name_pattern=r'\b[a-zA-Z]+\b'
# model_pattern=r'\b[a-zA-Z0-9]+\b'
# characters=re.findall(name_pattern,search)
# model=re.findall(model_pattern,search)
#
#
# print(characters)
# print(model)
# print(search)
# Search..s24 Samgoung list apple 15 apple15pro
# ['Samgoung', 'list', 'apple']
# ['s24', 'Samgoung', 'list', 'apple', '15', 'apple15pro']
# s24 Samgoung list apple 15 apple15pro