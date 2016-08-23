static_data = {
    'title': 'Hunger games',
    'author': 'Suzzane Collins',
    'publish_year': 2008,
}

set_response(HttpResponse(status_code=200, content=static_data, content_type='application/json'))
