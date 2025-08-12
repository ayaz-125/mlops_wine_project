# from src.ml_project import logger 

# logger.info("This is the main file and we are making it from the project")
# logger.info("This is another file and we have to make the certain changes into this file ")
# logger.info("This is the third file and we have to make some changes into this file and we are not")

from src.ml_project.utils.common import *
# from pathlib import Path

# -------------------for checking read_yaml function 
# filepath = Path("schema.yaml")
# nam = read_yaml(filepath)
# print(nam.data_in)
# print(nam.value)



# -------------------for checking create_dir function
# dir_p = create_dir(["ayaz"])


# ----------------for checking save_json function
# person_data = {
#     "name": "Amit",
#     "age": 25,
#     "skills": ["Python", "Machine Learning", "AWS"]
# }

# # Save it
# save_json(Path("ayaz.json"), person_data)

# print("JSON file saved!")


# ---------------------for cheking load_json function 
# pa = Path("ayaz.json")
# lo = load_json(pa)
# print(lo.name)
# print(f"the age of {lo.name} is {lo.age}")


model_params = {
    "learning_rate": 0.01,
    "n_estimators": 100,
    "max_depth": 5
}

# Save it as a binary file
# save_bin(Path("model_params.pkl"), model_params)

# print("Binary file saved!")


# ------------example for load_bin and save_bin
# model = Path("model_params.pkl")
# lo = load_bin(model)
# print(lo)
# print(type(lo))
# # print(lo['learning_rate'])

# lr = lo.get('learning_rate', None)  # Default to None if missing
# lr = lo.get('n_estimators', None)  # Default to None if missing
# print(lr)


# ----------------example for the get size function 
# add = Path("src/ml_project/utils/common.py")
# size = getsize(add)
# print(size)