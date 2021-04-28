def print_term_directory(file = None,term = None):
    path = []
    if type(file) == dict and term in file.keys():
        [path.append(k) for k,v in file.items() if k == term]
    else:
        for k,v in file.items():
            if type(v) == dict and term in v.keys():
                path.append(k)
                terms_found = [path.append(k2) for k2,v2 in v.items() if k2 == term]
            elif type(v) == list:
                path.append(k)
                terms_found = [path.append(k2) for k2 in v if k2 == term]
    return type(terms_found),path