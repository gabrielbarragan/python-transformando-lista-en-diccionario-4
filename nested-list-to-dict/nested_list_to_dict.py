def nested_list_to_dict(nested_list: list= []) -> list:
    """"""

    my_list_result= [{field[0]:field[1] for field in lista} for lista in nested_list] 

    return my_list_result
