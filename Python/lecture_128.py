import os

for key in ["HOME","SHELL"]:
    value= os.getenv(key)
    print(f"{key} = {value if value else "Not set"}")

env_keys= list(os.environ.keys())
print(f"we have {len(env_keys)} environment variiable available!")

for key in env_keys[:5]:
    print(key)