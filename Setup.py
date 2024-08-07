from setuptools import find_packages,setup

end_char_txt = '-e .'

def get_requirements (file_path:str):
    re_list=[]

    with open(file_path,'r') as file:
        for f in file:
            re_list.append(f.strip())

    if end_char_txt in re_list:
        re_list.remove(end_char_txt)
        
    return re_list

# Triggered by code:  pip install -r "requirements.txt" in directory

setup(
name = 'llm_env', #env name
author= 'Apshetty',
author_email='apoorvagetseducated@gmail.com',
packages= find_packages(),
install_requires = get_requirements('Requirements.txt') #Fetch the required packages like pandas, seaborn etc from the txt
)

# Navigate to this folder after you create the env and write python setup.py install 