
import  math
import  json
import  requests


#作业1
def share_amount(total_amount=1000,weight=[5,5,5]):
    percent_list= []
    index_num=0
    weight_total=sum(weight)

    temp= 100/weight_total
    one_percent=temp/100
    print(one_percent)
    for  i  in weight:
        index_num += 1
        print(index_num)
        print(len(weight))
        if index_num == len(weight):
            break
        x= i*one_percent
        xvalue= round(x*total_amount,2)
        percent_list.append(xvalue)


    percent_list.append(round(1000-sum(percent_list),2))
    print(percent_list)
    return  percent_list

share_amount(total_amount=1000,weight=[7,5,17])





def  cal_page(total=10,page_size=3):

    page=math.ceil(total/page_size)
    print(page)
    return  page


cal_page()
#作业2
def  summarg(dogs):

    dogs_name=','.join(dogs)
    base_name='这里是宠物之家，我们这里有很多狗，包含'
    base_num= base_name.index('包含')
    print(base_num)
    dogs_count= dogs_name.count(',')+1
    print(dogs_count)
    last_str= "{base_name}{dogs_name}{dogs_count}种类型的狗".format(base_name=base_name,dogs_name=dogs_name,dogs_count=dogs_count)
    print(last_str)
    return  last_str
summarg(['中华田园犬','狼狗','及呜哇哇','茶杯犬'])

#作业3
tag_example= {
  "id": 4335,
  "category": {
    "id": 1234,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 7890,
      "name": "string"
    }
  ],
  "status": "available"
}
def  print_json(x):

    print(json.dumps(x,indent=4,ensure_ascii=False))


def  add_tags(item=dict(id=2,name='名字'),is_clear=False):

    temp_dict = {}
    for k, v in item.items():
        dict_kv = {k: v}
        temp_dict.update(dict_kv)

    if  is_clear==False:
        tag_example['tags'].append(temp_dict)
    else:
        print("==================")
        #tag_example['tags']=[]
        tag_example['tags']=[temp_dict]

    print_json(tag_example)

    return  tag_example

url= "https://petstore.swagger.io/v2/pet"

tags_instance= add_tags(dict(id='212',name='noname'),is_clear=True)

req= requests.post(url,json=tags_instance, verify=False)

print(req.url)
print_json(req.json())