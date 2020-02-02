#share_amount
import sys
def share_amount(total_amount):
    try:
        a = b = round(total_amount/3,2)
        c = round(total_amount - a - b,2)
        return a,b,c
    except Exception as e:
        return e

total_amount = 1000
print("""---practice1:share_amount---""")
print(share_amount(total_amount))


#list
import sys
def summarg(dogs):
    try:
        str = []
        for name in dogs:
            name = """\'""" + name + """\'"""
            str.append(name)

        new_str = ','.join(str)
        sentence_start = "这里是宠物之家，我们这里很多狗，包含"
        sentence_end = "种类型的狗"
        type_count = len(dogs)
        final_str = """{sentence_start}{new_str}{type_count}{sentence_end}""".format(sentence_start=sentence_start,sentence_end=sentence_end,new_str=new_str,type_count=type_count)
        return final_str
    except Exception as e:
        return e

dogs = ['金毛', '吉娃娃', '泰迪', '哈斯奇','萨摩耶']

print("""---practice2: update list---""")
print(summarg(dogs))



#dict
import json
import sys

template = {
  "id": 7890,
  "category": {
    "id": 12,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 2344,
      "name": "string"
    }
  ],
  "status": "available"
}


def print_json(x):
  print(json.dumps(x, indent=4, ensure_ascii=False))

def add_tags(items, is_clear):
  try:
    if is_clear:
      template["tags"].clear()
    template["tags"].append(items)
    return template
  except Exception as e:
    return e

dict = {"id":23, "name":"ceshi"}
print("""---practice3: update dict---""")
print("""1.The original teamplate body is as below:""")
print_json(template)

add_tags(dict,False)
print("""2. Not clear tags, the body is as below:""")
print_json(template)

add_tags(dict,True)
print("""3. Clear tags, the body is as below:""")
print_json(template)