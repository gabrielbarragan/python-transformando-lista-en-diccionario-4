def nested_list_to_dict(nested_list: list= []) -> list:
    """"""

    my_list_result=[]
    for lista in nested_list:
        my_dict= {field[0]:field[1] for field in lista}
        my_list_result.append(my_dict)
        

    return my_list_result

