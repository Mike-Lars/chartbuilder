import datetime


def datetime_object_builder(df, sy, sm, sd, ey, em, ed):
    if sy == None or sm == None or sd == None:
        s_obj = df['date'][0]
    else:
        s_obj = datetime.date(sy, sm, sd) 
    if ey == None or em == None or ed == None:
        e_obj = datetime.date(2027, 12, 31)
    else:
        e_obj = datetime.date(ey, em, ed)
        
    return(s_obj, e_obj)
