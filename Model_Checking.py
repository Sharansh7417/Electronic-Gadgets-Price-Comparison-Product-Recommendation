import pickle


df=pickle.load(open('product_list.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))

def recom_function(model_name):
    print(f"Request for {model_name}")
    Trimed_name=model_name[:18]
    print(f"Trim the Request to -->>>>{Trimed_name}")
    # first_index=int(new['row_id'][new['Product_name'].str.contains(f'{model_name}')].values[0])
    print(df['row_id'][df['Product_name'].str.contains(f'{Trimed_name}')])
    first_index = df['row_id'][df['Product_name'].str.contains(f'{Trimed_name}')].index[0]

    distance = sorted(list(enumerate(similarity[first_index])), reverse=True, key=lambda x: x[1])[1:10]
    return distance



if __name__ == "__main__":
    # use of Debugging
    while(True):
        try:
            sear=input("enter..")
            result=recom_function(sear)
        except:
            print("nothing.....")
        print(result)