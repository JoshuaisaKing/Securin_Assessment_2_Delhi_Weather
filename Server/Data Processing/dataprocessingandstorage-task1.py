import json

def read_file(path):
    with open(path,'r') as file:
        for i in file:
            print(i)


def convert_to_json(path,end_path):
    with open(path,'r') as file:
        for i in file:
            with open(end_path,'a') as file1:
                file1.write(json.dumps(i))

path = r'C:\Users\JoshDev\Desktop\Securin\Server\Data Processing\testset.csv'

#read_file(path)

end_path = r'C:\Users\JoshDev\Desktop\Securin\Server\Data Processing\endset.json'

convert_to_json(path,end_path)
