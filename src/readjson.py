#coding=utf-8 
#import pdb


def read_json(filename):

    import json
    with open(filename) as json_data:
        d = json.load(json_data)
        json_data.close()
    
    #result = d['resultData']["t172021094005.cm3"]["0xilovexxx"] 
    result = d['resultData'] 
    for k, v in result.iteritems():
        result = v 
        break;
    for k, v in result.iteritems():
        result = v 
        break;

    cpu, cpu_time   = parse( sorted(result["cpu"].items())  )
    mem, mem_time   = parse( sorted(result["mem"].items())  ) 
    load, load_time = parse( sorted(result["load5"].items()))
    
    return cpu, cpu_time, mem, mem_time, load, load_time 


def parse(data):
    from datetime import datetime
    import time
    data_list = [] 
    time_list = [] 
    for item in data:
        t = time.mktime(datetime.strptime(item[0], "%Y-%m-%d %H:%M:%S").timetuple())
        time_list.append( t )
        data_list.append(float(item[1]))

    return (data_list, time_list)
