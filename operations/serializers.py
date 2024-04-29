def orm_result_row_to_dict(result_row, fields):
    return {field: getattr(result_row, field) for field in fields}


def orm_result_list_to_dict(result_list, fields):
    return [
        {field: getattr(row, field) for field in fields}
        for row in result_list
    ]
